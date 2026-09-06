# Binarygap Log

Welcome to the repository for **Binarygap Log** — Colin's personal space for deep-dive research, conceptual blueprints, and engineering notes.

This site is powered by **Jekyll** and hosted on **GitHub Pages**, equipped with SEO optimization, RSS feeds, full-text search, and tagging.

---

## Quick Start

### Running Locally

To preview and test the blog locally:

```bash
# Install dependencies
bundle install

# Run local development server
bundle exec jekyll serve
```

Once the server boots up, open [http://localhost:4000](http://localhost:4000) in your browser.

---

## Writing New Posts

To create a new blog post, add a markdown file to the `posts/` (or `_posts/`) directory using the `YYYY-MM-DD-001-title.md` naming format:

```markdown
---
layout: post
title: "Your Post Title"
date: YYYY-MM-DD HH:MM:SS +0900
categories:
  - tech
tags:
  - architecture
  - engineering
---

Write your post content here using standard GitHub Flavored Markdown.
```

---

## License

- Source Code: [MIT License](LICENSE.md)
- Content: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
