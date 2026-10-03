# The Fröhlich Lab main website

Our website, https://www.frohlichlab.com, is a [GitHub Pages](https://pages.github.com/) site built with [Jekyll](https://jekyllrb.com/) and [Bootstrap](https://getbootstrap.com), originally pulled from [Trevor Bedford's site](http://bedford.io) and the [Drummond Lab site](http://drummondlab.org).

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

A site is a collection of HTML pages. For our site (and many others), there are page types, like a paper page, or a lab member page, which are the same in design but different in content. In the web-accessible site, these are indeed different pages. However, they are _generated_ from a single template file filled in with information from many paper- or member-specific Markdown files. This generation is done every time the site changes by a GitHub Actions workflow.

- `_layouts/` – the page templates (`default` is the frame with navigation bar and footer; `paper`, `member`, `post`, `tool` and `project` are used by the respective Markdown files).
- `_includes/` – reusable snippets and longer texts: `home.md` (home page text), `research.md` (research page intro), `post_list.html` (news/blog listing).
- `about.md`, `join.md` – the About and Join pages.
- `<section>/index.html` – the overview pages (`research`, `papers`, `tools`, `team`, `news`, `blog`); the items they list live in `<section>/_posts/`.
- `assets/` – images, PDFs, stylesheets (`assets/themes/lab/css/style.scss`) and the Bootstrap files.
- `_design/` – Illustrator sources for the logo and artwork (not published).

## How to add content

For most common actions---adding a lab member, paper, tool, or news item---you'll be making a new Markdown file in the proper `_posts` folder, naming it properly, and filling in the required fields. In almost all cases, you can (and should!) copy an existing item, change the name, and change its content, rather than trying to write a Markdown document from scratch.

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

The same basic process is used to add team members (`team/_posts`, `layout: member`), tools (`tools/_posts`, `layout: tool`), blog posts (`blog/_posts`) and research topics (`research/_posts`).

## Adding publications

Paper pages in `papers/_posts` are generated from `papers/_posts/bibliography.bib` by `papers/_posts/convert_bib.py` (Python, needs `pybtex`, `setuptools`, `unidecode` and `requests`):

1. Add the BibTeX entry to `bibliography.bib` (with `year`, `month`, `day`, `journal`, `doi`, `abstract`; for preprints also `eprint` with the PDF link).
2. Add the new paper to `CODE_LINKS` in the script (`''` if there is no code), and to `J_ABBREV` if the journal is new.
3. Run the script from that folder; it deletes all `.md` files there and regenerates them from `post.md.template`:

   ```
   cd papers/_posts
   pip3 install pybtex setuptools unidecode requests
   python3 convert_bib.py
   ```

## Updating the public site

All edits should be made on your feature branch. Once your edits are done, preview the site locally (see above) and look at anything you've changed to make sure it's good to go.

Then create a [pull request](https://github.com/frohlich-lab/frohlichlab.github.io/compare) on github.com with `main` as base branch. GitHub will automatically build the site to check that everything is in order and request a review for the changes. After the pull request is merged into `main`, the GitHub Actions workflow (`.github/workflows/jekyll.yml`) builds the site and deploys it to GitHub Pages. Check that the public site https://www.frohlichlab.com looks the way you intend. Changes won't be immediate though, so wait a minute or two for the deployment to finish (see the Actions tab).

## Changing look and feel

Fonts, colors, spacing, and similar stylings are separate from the templates. Like most sites, we use Cascading Style Sheets (CSS), written as [Sass](https://sass-lang.com) in `assets/themes/lab/css/style.scss` on top of Bootstrap 3.

### To-dos

See Issues on [the site](https://github.com/frohlich-lab/frohlichlab.github.io).


## License

[MIT](http://opensource.org/licenses/MIT)
