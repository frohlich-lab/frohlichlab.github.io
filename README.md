# The Fröhlich Lab main website

Our website, https://www.frohlichlab.com, is a [GitHub Pages](https://pages.github.com/) site built with [Jekyll](https://jekyllrb.com/) and a small hand-written stylesheet, originally pulled from [Trevor Bedford's site](http://bedford.io) and the [Drummond Lab site](http://drummondlab.org).

# Editing the site

Here's a step-by-step guide to making modifications to the site, focused initially on adding typical content. You'll need a working Unix-like environment and working knowledge of Git, [Markdown](https://daringfireball.net/projects/markdown/syntax), HTML, and Unix commands.

## Clone the repository

If you're a member of the [Fröhlich Lab organization](https://github.com/frohlich-lab), you have access to the website repository.

To clone the repository, making a local copy on your machine:

	git clone https://github.com/frohlich-lab/frohlichlab.github.io.git

Enter your local repository and check out a new branch `<my-feature>` from the `main` branch, where you'll make changes. Replace `<my-feature>` with a short, informative description of what you will change.

	cd frohlichlab.github.io
	git checkout -b <my-feature> main

## Setup dependencies

The site is built with Ruby 3.3 (the same version the deployment uses). On macOS, install it with [Homebrew](https://brew.sh) and put it on your `PATH` (e.g. in `~/.zshrc`):

	brew install ruby@3.3
	export PATH="$(brew --prefix ruby@3.3)/bin:$PATH"

On Linux, install Ruby 3.3 with your package manager or a version manager such as `rbenv`. Then install the gems listed in `Gemfile` at the versions pinned in `Gemfile.lock`:

	bundle install

## Preview the site locally

	bundle exec jekyll serve

and open http://127.0.0.1:4000. The site is rebuilt automatically whenever you save a file (changes to `_config.yml` need a restart). If port 4000 is taken, add `--port 4001`.

## Overview of the structure

A site is a collection of HTML pages. For our site (and many others), there are page types, like a paper page, or a lab member page, which are the same in design but different in content. In the web-accessible site, these are indeed different pages. However, they are _generated_ from a single template file filled in with information from many member-specific Markdown files (or, for papers, BibTeX entries). This generation is done every time the site changes by a GitHub Actions workflow.

- `_layouts/` – the page templates (`default` is the frame with navigation bar and footer; `paper`, `member`, `post` and `project` (tools and research topics) are used by the respective Markdown files).
- `_includes/` – reusable snippets and longer texts: `home.md` (home page text), `research.md` (research page intro), `post_list.html` (news/blog listing), `icon.html` (inline SVG icons), `link_item.html` (sidebar links on member, paper and tool pages).
- `about.md`, `join.md` – the About and Join pages.
- `<section>/index.html` – the overview pages (`research`, `papers`, `tools`, `team`, `news`, `blog`).
- `news/_posts/`, `blog/_posts/` – dated posts.
- `_team/`, `_tools/`, `_research/` – one Markdown file per lab member, tool and research topic (Jekyll collections, configured in `_config.yml`).
- `assets/` – images, PDFs and the stylesheet (`assets/themes/lab/css/style.css`).
- `_design/` – Illustrator sources for the logo and artwork (not published).

## How to add content

For most common actions---adding a lab member, tool, or news item---you'll be making a new Markdown file in the proper folder, naming it properly, and filling in the required fields. In almost all cases, you can (and should!) copy an existing item, change the name, and change its content, rather than trying to write a Markdown document from scratch.

For example, suppose you want to add a news item, which will appear on the front page, announcing that you have created a yeast strain capable of secreting high-quality chardonnay. Go into the `news/_posts` folder. Copy one of the existing items into a new file named with today's date (it matters!) and a brief title:

	cp 2022-11-09-postdoc-hiring-2022-11.md 2023-01-31-wine-yeast.md

The date in the file name is the post's date; the rest becomes its URL (here `/news/wine-yeast`), so pick a title that hasn't been used before in that folder (otherwise one post silently replaces the other on the site). Now edit the new file to make the content what you want. By the time you're done, hopefully you have something like this:

	---
	layout: post
	title: "New yeast strain makes chardonnay"
	tags:
	  - publication
	---
	Today we are thrilled to announce a new strain of yeast that secretes beautifully oaked chardonnay. See more details in our [preprint](http://biorxiv.org/content/10.1101/0000000)!

Posts that recur, like hiring ads, need the year and month in the title as well, e.g. `2026-02-02-phd-hiring-2026-02.md` (URL `/news/phd-hiring-2026-02`). The newest PhD and postdoc ads also carry `redirect_from: /news/phd-hiring` (or `/news/postdoc-hiring`), so those short links always lead to the latest ad: move that line from the previous ad to the new one. To check that no two files share a URL, run `bundle exec jekyll doctor`; GitHub runs it on every pull request and push, and the build fails if it finds a conflict.

Now add it to the repository, commit and push your branch:

	git add 2023-01-31-wine-yeast.md
	git commit -m "announcing new yeast strain"
	git push -u origin <my-feature>

This new announcement won't yet be public. The section after next shows you how to do that.

Blog posts (`blog/_posts`) work the same way.

Team members, tools and research topics have no date in their file name: for members and tools the file name is the URL (`_team/Jana.md` becomes `/team/Jana`). Copy an existing file in `_team/` (`layout: member`) or `_tools/` (`layout: project`). Research topics in `_research/` only appear on the research page and have no page of their own. Team members are listed by their `joined:` date (set `alum: true` and `last_seen:` when someone leaves); tools and research topics by their `order:` number. Link to them from other pages with `{% link _team/Jana.md %}`.

## Adding a paper

There is no Markdown file per paper. The paper pages, the papers list, and the paper lists on the home, team and tool pages are all built from `papers/_posts/bibliography.bib` by `_plugins/papers.rb` every time the site is built.

1. Add a BibTeX entry to `papers/_posts/bibliography.bib` (an export from the journal or bioRxiv is a good start). It needs `author`, `title`, `journal`, `year`, `month` and `day` (numbers, used for ordering), `doi` and `abstract`. `volume`, `number` and `pages` are shown if present.
2. Add `eprint = {...}` with a link to the full-text PDF and, if there is code, `code = {https://github.com/...}`.
3. Optionally, put the PDF at `assets/pdfs/papers/<bibkey>.pdf`; it is then linked instead of `eprint`.
4. To abbreviate the journal name in the papers list, add it to `_data/journals.yml`. Entries whose journal is one of the preprint servers listed there (bioRxiv, arXiv, medRxiv) are marked as preprints.

The page URL is `/papers/<first author last name>-<bibkey>`, for example `/papers/persson-petab-sciml`. When a preprint is published, update its entry but keep the key, so the URL stays the same. LaTeX accents such as `Fr{\"o}hlich` are converted; plain Unicode works too. Team pages list every paper whose author list contains the member's last name.

Check the result with `bundle exec jekyll serve`; a missing required field stops the build with an error naming the entry.

## Updating the public site

All edits should be made on your feature branch. Once your edits are done, preview the site locally (see above) and look at anything you've changed to make sure it's good to go.

Then create a [pull request](https://github.com/frohlich-lab/frohlichlab.github.io/compare) on github.com with `main` as base branch. GitHub will automatically build the site to check that everything is in order and request a review for the changes. After the pull request is merged into `main`, the GitHub Actions workflow (`.github/workflows/jekyll.yml`) builds the site and deploys it to GitHub Pages. Check that the public site https://www.frohlichlab.com looks the way you intend. Changes won't be immediate though, so wait a minute or two for the deployment to finish (see the Actions tab).

## Changing look and feel

Fonts, colors, spacing, and similar stylings are separate from the templates. Like most sites, we use Cascading Style Sheets (CSS): a single plain-CSS file, `assets/themes/lab/css/style.css`, with no framework and no build step. Colours and the font are CSS custom properties at the top of the file; layout uses CSS grid and flexbox with the same breakpoints Bootstrap had (768/992/1200 px). Icons are inline SVGs: `{% include icon.html name="github" %}` (see `_includes/icon.html` for the available names).

### To-dos

See Issues on [the site](https://github.com/frohlich-lab/frohlichlab.github.io).


## License

[MIT](http://opensource.org/licenses/MIT)
