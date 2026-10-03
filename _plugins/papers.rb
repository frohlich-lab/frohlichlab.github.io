# frozen_string_literal: true

# Turns every entry of the BibTeX file configured as `papers.bibliography` in
# _config.yml into a post in the `papers` category.
#
# The posts get the same file names (and therefore URLs) and front matter that
# the old convert_bib.py script used to write into papers/_posts/, so layouts
# and pages keep using site.categories.papers and {% post_url papers/... %}.
#
# Fields read from each entry:
#   author, title, journal, year, month, day, doi, abstract  (required)
#   volume, number, pages, eprint (full-text PDF URL), code (repository URL)
# A local PDF at <papers.pdf_dir>/<bibkey>.pdf takes precedence over eprint.
# Journal abbreviations and preprint servers live in _data/journals.yml.

require "bibtex"
require "latex/decode"

module LabPapers
  REQUIRED_FIELDS = %i[author title journal year month day doi abstract].freeze
  TILDE = "\u{E000}" # placeholder that keeps "~" away from the LaTeX decoder

  class PaperPost < Jekyll::Document
    def initialize(path, site:, data:, content:)
      super(path, site: site, collection: site.posts)
      @bib_data = data
      @bib_content = content
    end

    # Front matter and body come from the BibTeX entry, not from a file on disk.
    def read_content(**)
      self.content = @bib_content
      merge_data!(@bib_data, source: "bibliography")
    end
  end

  class Generator < Jekyll::Generator
    safe true
    priority :highest

    def generate(site)
      config = site.config.fetch("papers", {})
      @bib_path = config.fetch("bibliography", "papers/_posts/bibliography.bib")
      @pdf_dir = config.fetch("pdf_dir", "assets/pdfs/papers")
      journals = site.data.fetch("journals", {})
      @abbreviations = journals.fetch("abbreviations", {})
      @preprint_servers = journals.fetch("preprint_servers", [])

      text = File.read(site.in_source_dir(@bib_path), encoding: "utf-8")
      check_unique_keys(text)
      BibTeX.parse(text).entries.each_value do |entry|
        post = build_post(site, entry)
        post.read
        site.posts.docs << post if site.publisher.publish?(post)
      end
      site.posts.docs.sort!
    end

    private

    # bibtex-ruby silently renames a repeated key (and shifts the keys of
    # later entries to make room), which would change paper URLs.
    def check_unique_keys(text)
      keys = text.scan(/^\s*@\s*(?!string\b|comment\b|preamble\b)\w+\s*\{\s*([^,\s]+)\s*,/i).flatten
      duplicates = keys.tally.select { |_, count| count > 1 }.keys
      return if duplicates.empty?

      raise Jekyll::Errors::FatalException, "#{@bib_path}: duplicate key(s) #{duplicates.join(', ')}"
    end

    def build_post(site, entry)
      missing = REQUIRED_FIELDS.reject { |field| entry.field?(field) }
      fail_entry(entry, "is missing #{missing.join(', ')}") unless missing.empty?

      year, month, day = date_parts(entry)
      first_author = surname(entry.author.first)
      journal = decode(entry.journal)
      basename = format("%04d-%02d-%02d-%s-%s", year, month, day,
                        transliterate(first_author.downcase), entry.key)

      data = {
        "layout"   => "paper",
        "title"    => decode(entry.title),
        "authors"  => entry.author.map { |name| "#{surname(name)} #{initials(name)}".strip }.join(", "),
        "year"     => year,
        "ref"      => "#{first_author} et al. #{year}. #{@abbreviations.fetch(journal, journal)}",
        "journal"  => journal,
        "doi"      => raw(entry, :doi),
        "volume"   => raw(entry, :volume),
        "issue"    => raw(entry, :number),
        "pages"    => raw(entry, :pages),
        "preprint" => @preprint_servers.include?(journal),
        "code"     => raw(entry, :code),
      }.merge(full_text(site, entry))

      PaperPost.new(site.in_source_dir("papers/_posts", "#{basename}.md"),
                    site: site, data: data,
                    content: "# Abstract\n\n#{decode(entry.abstract)}\n")
    end

    def full_text(site, entry)
      local_pdf = File.join(@pdf_dir, "#{entry.key}.pdf")
      if File.exist?(site.in_source_dir(local_pdf))
        { "pdf" => "/#{local_pdf}", "pdflink" => nil }
      else
        Jekyll.logger.warn "Papers:", "#{entry.key} has no eprint field or local PDF" unless entry.field?(:eprint)
        { "pdf" => nil, "pdflink" => raw(entry, :eprint) }
      end
    end

    # bibtex-ruby rewrites `month` to a name and keeps the number in month_numeric.
    def date_parts(entry)
      [entry.year, entry[:month_numeric] || entry.month, entry[:day]].map do |part|
        Integer(part.to_s, 10)
      rescue ArgumentError
        fail_entry(entry, "has a non-numeric year, month or day (#{part})")
      end
    end

    # Surname including particles, e.g. "de Pomereu".
    def surname(name)
      [name.von, name.last].compact.map { |part| decode(part) }.join(" ")
    end

    # "Frank T." -> "FT"
    def initials(name)
      decode(name.first).split.map { |part| part[0].upcase }.join
    end

    # BibTeX value -> plain text. Decodes accents and escapes ({\"o}, \&) and
    # drops braces, but keeps quotes, dashes and "~" as typed: abstracts are
    # usually pasted from journal sites rather than written as LaTeX.
    def decode(value)
      text = value.to_s.gsub(/(?<!\\)~/, TILDE)
      LaTeX.decode(text, punctuation: false)
           .gsub(/\\([$%#_&])/, '\1')
           .gsub(/ı(?=\p{Mn})/, "i") # {\'\i} decodes to a dotless i plus accent
           .tr(TILDE, "~")
           .unicode_normalize(:nfc)
           .strip
    end

    def raw(entry, field)
      value = entry[field].to_s.strip
      value.empty? ? nil : value
    end

    # ASCII file names, as the old script produced with unidecode.
    def transliterate(text)
      I18n.config.available_locales = :en
      I18n.transliterate(text)
    end

    def fail_entry(entry, message)
      raise Jekyll::Errors::FatalException, "#{@bib_path}: entry '#{entry.key}' #{message}"
    end
  end
end
