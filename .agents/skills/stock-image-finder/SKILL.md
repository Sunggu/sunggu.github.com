---
name: stock-image-finder
description: >-
  Search, discover, and download commercially usable (CC0, Public Domain, Unsplash/Wikimedia)
  free stock images using keywords. Use when the user asks to find images for blog posts,
  insert stock photos into markdown, or download free commercial images.
---

# Stock Image Finder Skill

This skill allows the agent to search and download high-resolution, commercially usable free stock images (CC0, Public Domain, Wikimedia Commons, Unsplash) directly from the command line without opening browser tabs.

## Prerequisites
Uses Python 3 standard library (`urllib`, `json`, `argparse`). No third-party packages required.

## Helper Script Location
The script is located at `scripts/stock_image.py` within this skill.

## Usage Guide

### 1. Search Stock Images by Keyword
Search for relevant images with license metadata, dimensions, and direct URLs:
```bash
python3 <skill_dir>/scripts/stock_image.py "Federal Reserve" --limit 3
```

### 2. Search and Download Directly to a Target Folder
```bash
python3 <skill_dir>/scripts/stock_image.py "Macroeconomics" --download --outdir "assets/images/posts" --limit 2
```

### 3. Get JSON Output for Agent Pipeline Integration
```bash
python3 <skill_dir>/scripts/stock_image.py "Artificial Intelligence" --limit 3 --json
```

## Integrating into Blog & Markdown Posts
1. Download image to post assets folder:
   ```bash
   python3 <skill_dir>/scripts/stock_image.py "Quantum Computing" --download --outdir "assets/images/posts" --limit 1
   ```
2. Insert relative markdown link into the target post:
   ```markdown
   ![Quantum Computing](/assets/images/posts/01_Quantum_Computing.jpg)
   ```
3. Or insert direct URL directly without local download:
   ```markdown
   ![Topic](https://upload.wikimedia.org/wikipedia/commons/...)
   ```
