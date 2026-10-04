# frozen_string_literal: true

# Liquid filter for the word count and reading time on blog posts
# (_layouts/post.html):
#
#   {% assign stats = content | reading_stats %}
#
#   stats.words, stats.minutes  main text, without the collapsible boxes
#                               (<details>)
#   stats.words_expanded,       expanded view: with every box read as well
#   stats.minutes_expanded
#   stats.boxes                 true if the post has any boxes
#
# Word counts come with thousands separators ("2,696"). Reading time is the
# word count at 238 words per minute, the average silent reading rate for
# non-fiction (Brysbaert 2019, doi:10.1016/j.jml.2019.104047), and at least
# one minute.

module LabReadingStats
  WORDS_PER_MINUTE = 238
  BOX = %r{<details\b.*?</details>}m

  def self.count_words(html)
    html.gsub(/<[^>]*>/, " ").split.size
  end

  def self.minutes(words)
    [(words.to_f / WORDS_PER_MINUTE).round, 1].max
  end

  def self.delimit(number)
    number.to_s.reverse.scan(/\d{1,3}/).join(",").reverse
  end

  def reading_stats(html)
    html = html.to_s
    main = LabReadingStats.count_words(html.gsub(BOX, " "))
    all = LabReadingStats.count_words(html)
    {
      "words" => LabReadingStats.delimit(main),
      "minutes" => LabReadingStats.minutes(main),
      "words_expanded" => LabReadingStats.delimit(all),
      "minutes_expanded" => LabReadingStats.minutes(all),
      "boxes" => html.match?(BOX),
    }
  end
end

Liquid::Template.register_filter(LabReadingStats)
