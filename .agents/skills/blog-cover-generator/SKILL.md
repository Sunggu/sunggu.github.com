---
name: blog-cover-generator
description: >-
  Generate eye-catching, high-resolution blog post covers, header banners (16:9, 3:1, 2.35:1),
  and square thumbnails (1:1) with modern gradients (Fed Meeting aurora, Quartz minimal, GitBook docs)
  for blog posts in Jekyll, Naver Blog, Tistory, Quartz, or GitBook.
  Use when the user wants to create a post cover image, header banner, or thumbnail from titles and subtitles.
---

# Blog Cover & Thumbnail Generator Skill

This skill generates professional, high-DPI blog covers, header banners, and 1:1 thumbnails using Python (Pillow). It supports multiple themes (including the signature **Fed Meeting Aurora Violet**, Quartz dot-grid, GitBook cyan, Naver high-impact, and Tistory editorial) and platform aspect ratios.

## Prerequisites
Ensure `Pillow` is installed:
```bash
python3 -c "import PIL" || pip install Pillow
```

## Helper Script Location
The script is located at `scripts/generate_post_image.py` within this skill.

## Usage Guide

### 1. Generating a Post Header Banner (16:9 - Fed Meeting Aurora Theme)
Use for post top covers (e.g. Jekyll frontmatter `image`, Naver Blog header, Tistory header):
```bash
python3 <skill_dir>/scripts/generate_post_image.py \
  --title "Post Title Here" \
  --subtitle "Secondary English description or summary" \
  --badge "CATEGORY / TAG" \
  --author "Binary Gap" \
  --theme fed-meeting \
  --platform naver-header \
  --output "assets/images/posts/cover.png"
```

### 2. Generating a Square Thumbnail (1:1 - Naver / Tistory / Social)
```bash
python3 <skill_dir>/scripts/generate_post_image.py \
  --title "2026 하반기 핵심 전략" \
  --subtitle "금리 인하 사이클 완벽 분석" \
  --badge "TOP PICK" \
  --theme naver-thumb \
  --platform naver-thumb-sq \
  --align center \
  --output "assets/images/posts/thumb.png"
```

### 3. Generating a Tech Docs Header (3:1 GitBook / 2.35:1 Quartz)
```bash
python3 <skill_dir>/scripts/generate_post_image.py \
  --title "System Architecture" \
  --subtitle "Distributed Real-Time Pipeline" \
  --badge "TECH SPEC" \
  --theme gitbook-tech \
  --platform gitbook-cover \
  --output "assets/images/posts/gitbook_header.png"
```

## Supported Theme Presets (`--theme`)
- `fed-meeting`: Signature deep purple, fuchsia, and indigo aurora mesh gradient.
- `quartz-minimal`: Charcoal dark mode with dot-matrix pattern and minimal border.
- `gitbook-tech`: Deep navy with electric cyan glow and browser bar.
- `naver-thumb`: High-contrast saturated indigo/orange for eye-catching 1:1 thumbnails.
- `tistory-editorial`: Midnight wine sunset with elegant typography.
- `emerald-wealth`: Forest deep green and emerald for finance/macroeconomics.
- `cyber-neon`: Hot pink and electric blue for coding/devlogs.
- `swiss-minimal`: Clean monochrome black and white.

## Supported Platform Presets (`--platform`)
- `naver-header`: 1920x1080 (16:9)
- `naver-thumb-sq`: 1080x1080 (1:1)
- `naver-thumb-43`: 1200x900 (4:3)
- `tistory-header`: 1280x720 (16:9)
- `tistory-thumb`: 800x800 (1:1)
- `gitbook-cover`: 1200x400 (3:1)
- `quartz-cover`: 1200x510 (2.35:1)
- `og-card`: 1200x630 (1.91:1)

## Inserting into Markdown / Jekyll Posts
When writing posts in `_posts/` or `content/`:
1. Generate the image to `assets/images/posts/<slug>-cover.png`.
2. Insert as frontmatter image:
   ```yaml
   ---
   title: "My Post Title"
   image: /assets/images/posts/my-post-cover.png
   ---
   ```
3. Or insert at the top of the post body:
   ```markdown
   ![Post Cover](/assets/images/posts/my-post-cover.png)
   ```
