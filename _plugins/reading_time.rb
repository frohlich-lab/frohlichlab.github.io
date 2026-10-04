# frozen_string_literal: true

# Liquid filter for the reading time shown on blog posts (_layouts/post.html).
#
#   {{ content | reading_time }}         minutes for the main text, without the
#                                        collapsible boxes (<details>)
#   {{ content | reading_time: "all" }}  minutes with every box read as well
#
# Counts the words of the rendered HTML at 238 words per minute, the average
# silent reading rate for non-fiction (Brysbaert 2019, doi:10.1016/j.jml.2019.104047).
# Always at least one minute.

module LabReadingTime
  WORDS_PER_MINUTE = 238

  def reading_time(html, scope = "main")
    text = html.to_s
    text = text.gsub(%r{<details\b.*?</details>}m, " ") unless scope == "all"
    words = text.gsub(/<[^>]*>/, " ").split.size
    [(words.to_f / WORDS_PER_MINUTE).round, 1].max
  end
end

Liquid::Template.register_filter(LabReadingTime)
