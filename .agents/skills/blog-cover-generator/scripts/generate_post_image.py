#!/usr/bin/env python3
"""
Post Image Studio - Blog Cover & Thumbnail Generator (Python CLI & Module)
Generates high-resolution blog post covers, header banners, and thumbnails
optimized for Naver Blog, Tistory, GitBook, Quartz, etc.
"""

import os
import math
import argparse
from typing import Tuple, List, Optional, Dict, Any
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Platform Dimensions Definition
PLATFORM_DIMENSIONS = {
    'naver-header': {'width': 1920, 'height': 1080, 'label': '네이버 블로그 상단 커버 (16:9)'},
    'naver-thumb-sq': {'width': 1080, 'height': 1080, 'label': '네이버 블로그 대표 썸네일 (1:1)'},
    'naver-thumb-43': {'width': 1200, 'height': 900, 'label': '네이버 모바일 피드 썸네일 (4:3)'},
    'tistory-header': {'width': 1280, 'height': 720, 'label': '티스토리 본문 상단 배너 (16:9)'},
    'tistory-thumb': {'width': 800, 'height': 800, 'label': '티스토리 대표 썸네일 (1:1)'},
    'gitbook-cover': {'width': 1200, 'height': 400, 'label': 'GitBook 문서 헤더 커버 (3:1)'},
    'quartz-cover': {'width': 1200, 'height': 510, 'label': 'Quartz 지식 베이스 헤더 (2.35:1)'},
    'og-card': {'width': 1200, 'height': 630, 'label': 'SNS OG 공유 카드 (1.91:1)'},
    'custom-wide': {'width': 1260, 'height': 540, 'label': '시네마틱 울트라와이드 (21:9)'}
}

# Theme Presets
THEME_PRESETS = {
    'fed-meeting': {
        'name': 'Fed Meeting (Aurora Violet)',
        'bg_type': 'mesh-aurora',
        'bg_colors': ['#3b0764', '#86198f', '#1e1b4b'], # Deep purple, fuchsia, navy
        'accent_color': '#c084fc',
        'title_color': '#ffffff',
        'subtitle_color': '#e9d5ff',
        'badge_bg': 'rgba(30, 27, 75, 0.85)',
        'badge_text': '#c084fc',
        'pattern': 'none',
        'frame': 'none',
        'shadow': 'soft'
    },
    'quartz-minimal': {
        'name': 'Quartz Knowledge (Graphite & Dots)',
        'bg_type': 'gradient-linear',
        'bg_colors': ['#09090b', '#18181b', '#27272a'],
        'accent_color': '#a1a1aa',
        'title_color': '#f4f4f5',
        'subtitle_color': '#a1a1aa',
        'badge_bg': 'rgba(24, 24, 27, 0.9)',
        'badge_text': '#e4e4e7',
        'pattern': 'dots',
        'frame': 'minimal-border',
        'shadow': 'none'
    },
    'gitbook-tech': {
        'name': 'GitBook Tech Docs (Electric Cyan)',
        'bg_type': 'mesh-aurora',
        'bg_colors': ['#030712', '#0e7490', '#0f172a'],
        'accent_color': '#22d3ee',
        'title_color': '#f0fdf4',
        'subtitle_color': '#67e8f9',
        'badge_bg': 'rgba(15, 23, 42, 0.85)',
        'badge_text': '#22d3ee',
        'pattern': 'grid',
        'frame': 'browser-bar',
        'shadow': 'glow'
    },
    'naver-thumb': {
        'name': 'Naver Impact (1:1 Saturated)',
        'bg_type': 'mesh-aurora',
        'bg_colors': ['#0f172a', '#4338ca', '#ea580c'],
        'accent_color': '#fb923c',
        'title_color': '#ffffff',
        'subtitle_color': '#fed7aa',
        'badge_bg': '#ea580c',
        'badge_text': '#ffffff',
        'pattern': 'none',
        'frame': 'glass-card',
        'shadow': 'deep'
    },
    'tistory-editorial': {
        'name': 'Tistory Editorial (Midnight Sunset)',
        'bg_type': 'gradient-linear',
        'bg_colors': ['#09090b', '#4c0519', '#881337'],
        'accent_color': '#fb7185',
        'title_color': '#fff1f2',
        'subtitle_color': '#fda4af',
        'badge_bg': 'rgba(76, 5, 25, 0.85)',
        'badge_text': '#fb7185',
        'pattern': 'dots',
        'frame': 'accent-line',
        'shadow': 'soft'
    },
    'emerald-wealth': {
        'name': 'Emerald Wealth (Macro & Finance)',
        'bg_type': 'mesh-aurora',
        'bg_colors': ['#022c22', '#065f46', '#042f2e'],
        'accent_color': '#34d399',
        'title_color': '#ecfdf5',
        'subtitle_color': '#a7f3d0',
        'badge_bg': 'rgba(2, 44, 34, 0.85)',
        'badge_text': '#34d399',
        'pattern': 'grid',
        'frame': 'minimal-border',
        'shadow': 'soft'
    },
    'cyber-neon': {
        'name': 'Cyberpunk Neon (Hot Pink)',
        'bg_type': 'mesh-aurora',
        'bg_colors': ['#050505', '#9d174d', '#1e1b4b'],
        'accent_color': '#f472b6',
        'title_color': '#ffffff',
        'subtitle_color': '#f472b6',
        'badge_bg': 'rgba(24, 24, 27, 0.9)',
        'badge_text': '#f472b6',
        'pattern': 'crosses',
        'frame': 'browser-bar',
        'shadow': 'glow'
    },
    'swiss-minimal': {
        'name': 'Swiss Monochrome (B&W)',
        'bg_type': 'solid',
        'bg_colors': ['#09090b', '#18181b', '#27272a'],
        'accent_color': '#ffffff',
        'title_color': '#ffffff',
        'subtitle_color': '#a1a1aa',
        'badge_bg': '#ffffff',
        'badge_text': '#000000',
        'pattern': 'none',
        'frame': 'minimal-border',
        'shadow': 'none'
    },
    'binarygap-clean': {
        'name': 'Binarygap Clean Dark (Navy & Slate)',
        'bg_type': 'mesh-aurora',
        'bg_colors': ['#030712', '#0f172a', '#1e293b'],
        'accent_color': '#38bdf8',
        'title_color': '#ffffff',
        'subtitle_color': '#94a3b8',
        'badge_bg': 'rgba(15, 23, 42, 0.85)',
        'badge_text': '#38bdf8',
        'pattern': 'none',
        'frame': 'none',
        'shadow': 'glow'
    },
    'deep-space': {
        'name': 'Deep Space Minimal (Charcoal & Indigo)',
        'bg_type': 'gradient-linear',
        'bg_colors': ['#020617', '#0f172a', '#1e1b4b'],
        'accent_color': '#818cf8',
        'title_color': '#f8fafc',
        'subtitle_color': '#cbd5e1',
        'badge_bg': 'rgba(15, 23, 42, 0.85)',
        'badge_text': '#818cf8',
        'pattern': 'none',
        'frame': 'none',
        'shadow': 'soft'
    }
}


def hex_to_rgb(hex_str: str) -> Tuple[int, int, int]:
    """Convert #rrggbb to RGB tuple."""
    hex_str = hex_str.lstrip('#')
    if len(hex_str) == 3:
        hex_str = ''.join(c * 2 for c in hex_str)
    return int(hex_str[0:2], 16), int(hex_str[2:4], 16), int(hex_str[4:6], 16)


def parse_color_with_alpha(color_str: str) -> Tuple[int, int, int, int]:
    """Parse hex or rgba(...) string to (R, G, B, A)."""
    color_str = color_str.strip()
    if color_str.startswith('rgba'):
        # rgba(r, g, b, a)
        content = color_str[color_str.find('(') + 1 : color_str.find(')')]
        parts = [p.strip() for p in content.split(',')]
        r, g, b = int(parts[0]), int(parts[1]), int(parts[2])
        a = int(float(parts[3]) * 255)
        return (r, g, b, a)
    elif color_str.startswith('#'):
        r, g, b = hex_to_rgb(color_str)
        return (r, g, b, 255)
    return (255, 255, 255, 255)


def get_font(size: int, bold: bool = False, mono: bool = False) -> ImageFont.FreeTypeFont:
    """Find appropriate system font with fallback."""
    candidate_paths = []
    if bold:
        candidate_paths = [
            "/usr/share/fonts/truetype/nanum/NanumSquareB.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
            "/System/Library/Fonts/AppleSDGothicNeo.ttc",
            "C:\\Windows\\Fonts\\malgunbd.ttf"
        ]
    else:
        candidate_paths = [
            "/usr/share/fonts/truetype/nanum/NanumSquareR.ttf",
            "/usr/share/fonts/truetype/nanum/NanumSquareL.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
            "/System/Library/Fonts/AppleSDGothicNeo.ttc",
            "C:\\Windows\\Fonts\\malgun.ttf"
        ]

    for p in candidate_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue

    # Fallback to default
    try:
        return ImageFont.load_default()
    except Exception:
        return ImageFont.load_default()


def render_mesh_aurora(width: int, height: int, colors: List[str], accent: str) -> Image.Image:
    """Render smooth multi-point Aurora mesh gradient background."""
    # Create base background
    c1 = hex_to_rgb(colors[0])
    c2 = hex_to_rgb(colors[1])
    c3 = hex_to_rgb(colors[2])
    c_acc = hex_to_rgb(accent)

    # Render at half size and upscale with blur for high performance and buttery-smooth gradient
    sw, sh = max(160, width // 4), max(90, height // 4)
    base = Image.new('RGB', (sw, sh), c1)

    # Create glow overlay
    overlay = Image.new('RGBA', (sw, sh), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Spot 1: Top Right Magenta / Violet
    r1 = int(max(sw, sh) * 0.7)
    cx1, cy1 = int(sw * 0.85), int(sh * 0.2)
    for r in range(r1, 0, -6):
        alpha = int(180 * (1.0 - (r / r1) ** 1.5))
        draw.ellipse([cx1 - r, cy1 - r, cx1 + r, cy1 + r], fill=(c2[0], c2[1], c2[2], alpha))

    # Spot 2: Bottom Left Indigo
    r2 = int(max(sw, sh) * 0.65)
    cx2, cy2 = int(sw * 0.25), int(sh * 0.85)
    for r in range(r2, 0, -6):
        alpha = int(190 * (1.0 - (r / r2) ** 1.5))
        draw.ellipse([cx2 - r, cy2 - r, cx2 + r, cy2 + r], fill=(c3[0], c3[1], c3[2], alpha))

    # Spot 3: Center Left Accent
    r3 = int(max(sw, sh) * 0.45)
    cx3, cy3 = int(sw * 0.15), int(sh * 0.3)
    for r in range(r3, 0, -6):
        alpha = int(120 * (1.0 - (r / r3) ** 1.8))
        draw.ellipse([cx3 - r, cy3 - r, cx3 + r, cy3 + r], fill=(c_acc[0], c_acc[1], c_acc[2], alpha))

    base = Image.alpha_composite(base.convert('RGBA'), overlay)
    base = base.filter(ImageFilter.GaussianBlur(radius=sw * 0.18))
    return base.resize((width, height), Image.Resampling.BICUBIC)


def render_linear_gradient(width: int, height: int, colors: List[str], angle_deg: float = 135) -> Image.Image:
    """Render smooth linear gradient."""
    c1 = hex_to_rgb(colors[0])
    c2 = hex_to_rgb(colors[1])
    c3 = hex_to_rgb(colors[2]) if len(colors) > 2 else c2

    sw, sh = 200, 200
    img = Image.new('RGB', (sw, sh), c1)
    draw = ImageDraw.Draw(img)

    rad = math.radians(angle_deg)
    cos_a, sin_a = math.cos(rad), math.sin(rad)

    for y in range(sh):
        for x in range(sw):
            # Normalized projection along angle
            proj = ((x - sw / 2) * cos_a + (y - sh / 2) * sin_a) / (sw * 0.707) + 0.5
            proj = max(0.0, min(1.0, proj))

            if proj < 0.5:
                t = proj / 0.5
                r = int(c1[0] * (1 - t) + c2[0] * t)
                g = int(c1[1] * (1 - t) + c2[1] * t)
                b = int(c1[2] * (1 - t) + c2[2] * t)
            else:
                t = (proj - 0.5) / 0.5
                r = int(c2[0] * (1 - t) + c3[0] * t)
                g = int(c2[1] * (1 - t) + c3[1] * t)
                b = int(c2[2] * (1 - t) + c3[2] * t)

            draw.point((x, y), fill=(r, g, b))

    return img.resize((width, height), Image.Resampling.BICUBIC)


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, max_width: int) -> List[str]:
    """Wrap text to fit inside maximum width."""
    lines = []
    for raw_line in text.split('\n'):
        if not raw_line:
            lines.append('')
            continue

        words = raw_line.split(' ')
        current_line = ''
        for word in words:
            test_line = f"{current_line} {word}".strip() if current_line else word
            bbox = draw.textbbox((0, 0), test_line, font=font)
            w = bbox[2] - bbox[0]
            if w > max_width and current_line:
                lines.append(current_line)
                current_line = word
            else:
                current_line = test_line
        if current_line:
            lines.append(current_line)
    return lines


def create_post_image(
    title: str = "Fed Meeting",
    subtitle: str = "Federal Open Market Committee Meeting",
    badge: str = "MACRO & FINANCE",
    author: str = "Binary Gap",
    date: Optional[str] = None,
    watermark: Optional[str] = None,
    theme: str = "fed-meeting",
    platform: str = "naver-header",
    pattern: Optional[str] = None,
    frame: Optional[str] = None,
    badge_bg: Optional[str] = None,
    badge_text: Optional[str] = None,
    text_align: str = "left",       # left | center | right
    vertical_align: str = "middle", # top | middle | bottom
    custom_width: Optional[int] = None,
    custom_height: Optional[int] = None,
    scale: int = 1
) -> Image.Image:
    """
    Generate a blog cover / thumbnail image.

    Args:
        title: Main post title (supports multi-line with \\n)
        subtitle: Secondary subtitle / english description
        badge: Category / tag badge text
        author: Author signature
        date: Date string (e.g. 2026.08.30)
        watermark: Top-right or bottom-right watermark
        theme: Theme preset name (fed-meeting, quartz-minimal, gitbook-tech, etc.)
        platform: Platform preset key (naver-header, naver-thumb-sq, tistory-header, etc.)
        pattern: Pattern override ('none', 'grid', 'dots', 'crosses')
        frame: Frame override ('none', 'minimal-border', 'browser-bar', 'glass-card', 'accent-line')
        badge_bg: Badge background color override (hex or rgba)
        badge_text: Badge text color override (hex or rgba)
        text_align: 'left', 'center', or 'right'
        vertical_align: 'top', 'middle', or 'bottom'
        custom_width: Override width
        custom_height: Override height
        scale: Scale factor (1 = 1x, 2 = 2x Retina HD)
    """
    preset_theme = THEME_PRESETS.get(theme, THEME_PRESETS['fed-meeting'])
    dim = PLATFORM_DIMENSIONS.get(platform, PLATFORM_DIMENSIONS['naver-header'])

    width = (custom_width or dim['width']) * scale
    height = (custom_height or dim['height']) * scale

    # 1. Render Background
    bg_type = preset_theme.get('bg_type', 'mesh-aurora')
    bg_colors = preset_theme.get('bg_colors', ['#3b0764', '#86198f', '#1e1b4b'])
    accent_hex = preset_theme.get('accent_color', '#c084fc')

    if bg_type == 'mesh-aurora':
        img = render_mesh_aurora(width, height, bg_colors, accent_hex)
    elif bg_type == 'gradient-linear':
        img = render_linear_gradient(width, height, bg_colors, 135)
    else:
        c1 = hex_to_rgb(bg_colors[0])
        img = Image.new('RGB', (width, height), c1)

    img = img.convert('RGBA')
    draw = ImageDraw.Draw(img)

    # 2. Render Patterns
    selected_pattern = pattern if pattern is not None else preset_theme.get('pattern', 'none')
    if selected_pattern == 'dots':
        step = max(24, width // 50)
        dot_r = max(1.5, width / 1000)
        for x in range(step // 2, width, step):
            for y in range(step // 2, height, step):
                draw.ellipse([x - dot_r, y - dot_r, x + dot_r, y + dot_r], fill=(255, 255, 255, 45))
    elif selected_pattern == 'grid':
        step = max(40, width // 30)
        for x in range(0, width, step):
            draw.line([(x, 0), (x, height)], fill=(255, 255, 255, 25), width=1)
        for y in range(0, height, step):
            draw.line([(0, y), (width, y)], fill=(255, 255, 255, 25), width=1)

    # 3. Render Frame Styles
    selected_frame = frame if frame is not None else preset_theme.get('frame', 'none')
    pad_x = int(width * 0.08)
    pad_y = int(height * 0.10)

    if selected_frame == 'minimal-border':
        m = int(min(width, height) * 0.04)
        draw.rounded_rectangle([m, m, width - m, height - m], radius=16 * scale, outline=(255, 255, 255, 40), width=int(1.5 * scale))
    elif selected_frame == 'glass-card':
        m = int(min(width, height) * 0.06)
        card_overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        card_draw = ImageDraw.Draw(card_overlay)
        card_draw.rounded_rectangle([m, m, width - m, height - m], radius=24 * scale, fill=(255, 255, 255, 12), outline=(255, 255, 255, 45), width=int(1.5 * scale))
        img = Image.alpha_composite(img, card_overlay)
        draw = ImageDraw.Draw(img)
    elif selected_frame == 'browser-bar':
        bar_h = max(36 * scale, int(height * 0.07))
        draw.rectangle([0, 0, width, bar_h], fill=(0, 0, 0, 90))
        draw.line([(0, bar_h), (width, bar_h)], fill=(255, 255, 255, 30), width=1)
        # Window buttons
        dot_r = max(5 * scale, int(bar_h * 0.15))
        dot_y = bar_h // 2
        colors = [(255, 95, 86), (255, 189, 46), (39, 201, 63)]
        for i, c in enumerate(colors):
            dx = 24 * scale + i * 16 * scale
            draw.ellipse([dx - dot_r, dot_y - dot_r, dx + dot_r, dot_y + dot_r], fill=c)

    # 4. Typography Layout Calculation
    max_content_w = width - pad_x * 2

    # Responsive Font Sizes
    base_title_size = int(height * 0.11) if height <= 600 else int(height * 0.08)
    title_font_size = max(36 * scale, min(100 * scale, base_title_size))
    subtitle_font_size = max(18 * scale, int(title_font_size * 0.38))
    badge_font_size = max(14 * scale, int(subtitle_font_size * 0.65))

    title_font = get_font(title_font_size, bold=True)
    subtitle_font = get_font(subtitle_font_size, bold=False)
    badge_font = get_font(badge_font_size, bold=True)

    title_lines = wrap_text(draw, title, title_font, max_content_w)
    subtitle_lines = wrap_text(draw, subtitle, subtitle_font, max_content_w) if subtitle else []

    title_line_h = int(title_font_size * 1.25)
    total_title_h = len(title_lines) * title_line_h

    subtitle_line_h = int(subtitle_font_size * 1.35)
    total_subtitle_h = len(subtitle_lines) * subtitle_line_h

    badge_h = 0
    badge_w = 0
    if badge:
        bbox = draw.textbbox((0, 0), badge.upper(), font=badge_font)
        badge_w = (bbox[2] - bbox[0]) + 24 * scale
        badge_h = badge_font_size + 14 * scale

    gap_badge_to_title = 22 * scale if badge else 0
    gap_title_to_sub = 20 * scale if subtitle else 0
    total_block_h = badge_h + gap_badge_to_title + total_title_h + gap_title_to_sub + total_subtitle_h

    # Starting Y position
    if vertical_align == 'top':
        current_y = pad_y + 30 * scale
    elif vertical_align == 'bottom':
        current_y = height - pad_y - total_block_h - 40 * scale
    else:
        current_y = (height - total_block_h) // 2

    # 5. Render Badge
    if badge:
        if text_align == 'center':
            badge_x = (width - badge_w) // 2
        elif text_align == 'right':
            badge_x = width - pad_x - badge_w
        else:
            badge_x = pad_x

        badge_bg_str = badge_bg if badge_bg is not None else preset_theme.get('badge_bg', 'rgba(255,255,255,0.2)')
        badge_text_str = badge_text if badge_text is not None else preset_theme.get('badge_text', '#ffffff')

        badge_bg_rgba = parse_color_with_alpha(badge_bg_str)
        badge_border_rgba = parse_color_with_alpha(accent_hex)
        badge_text_rgba = parse_color_with_alpha(badge_text_str)

        # Draw badge box (clean glass pill or solid pill)
        draw.rounded_rectangle([badge_x, current_y, badge_x + badge_w, current_y + badge_h], radius=8 * scale, fill=badge_bg_rgba, outline=badge_border_rgba, width=max(1, int(1.5 * scale)))

        # Draw badge text
        b_bbox = draw.textbbox((0, 0), badge.upper(), font=badge_font)
        bw_text = b_bbox[2] - b_bbox[0]
        bh_text = b_bbox[3] - b_bbox[1]
        tx = badge_x + (badge_w - bw_text) // 2
        ty = current_y + (badge_h - bh_text) // 2
        draw.text((tx, ty), badge.upper(), font=badge_font, fill=badge_text_rgba)

        current_y += badge_h + gap_badge_to_title

    # 6. Render Title (with Drop Shadow)
    title_color = parse_color_with_alpha(preset_theme.get('title_color', '#ffffff'))
    shadow_mode = preset_theme.get('shadow', 'soft')

    for i, line in enumerate(title_lines):
        bbox = draw.textbbox((0, 0), line, font=title_font)
        line_w = bbox[2] - bbox[0]
        if text_align == 'center':
            lx = (width - line_w) // 2
        elif text_align == 'right':
            lx = width - pad_x - line_w
        else:
            lx = pad_x

        ly = current_y + i * title_line_h

        # Shadow
        if shadow_mode == 'soft':
            draw.text((lx + 2 * scale, ly + 3 * scale), line, font=title_font, fill=(0, 0, 0, 100))
        elif shadow_mode == 'glow':
            acc_rgb = hex_to_rgb(accent_hex)
            draw.text((lx, ly), line, font=title_font, fill=(acc_rgb[0], acc_rgb[1], acc_rgb[2], 140))
        elif shadow_mode == 'deep':
            draw.text((lx + 4 * scale, ly + 5 * scale), line, font=title_font, fill=(0, 0, 0, 200))

        # Main text
        draw.text((lx, ly), line, font=title_font, fill=title_color)

    current_y += total_title_h + gap_title_to_sub

    # 7. Render Subtitle
    if subtitle_lines:
        sub_color = parse_color_with_alpha(preset_theme.get('subtitle_color', '#d8b4fe'))
        for i, line in enumerate(subtitle_lines):
            bbox = draw.textbbox((0, 0), line, font=subtitle_font)
            line_w = bbox[2] - bbox[0]
            if text_align == 'center':
                lx = (width - line_w) // 2
            elif text_align == 'right':
                lx = width - pad_x - line_w
            else:
                lx = pad_x
            ly = current_y + i * subtitle_line_h

            if shadow_mode != 'none':
                draw.text((lx + 1 * scale, ly + 2 * scale), line, font=subtitle_font, fill=(0, 0, 0, 80))
            draw.text((lx, ly), line, font=subtitle_font, fill=sub_color)

    # 8. Render Footer (Author & Date)
    if author or date:
        footer_font_size = max(14 * scale, int(width * 0.013))
        footer_font = get_font(footer_font_size, bold=False)
        footer_text = author or ''
        if date:
            if footer_text:
                footer_text += f"  •  {date}"
            else:
                footer_text = date

        draw.text((pad_x, height - pad_y - footer_font_size), footer_text, font=footer_font, fill=(255, 255, 255, 180))

    if watermark:
        wm_font_size = max(14 * scale, int(width * 0.013))
        wm_font = get_font(wm_font_size, bold=True)
        w_bbox = draw.textbbox((0, 0), watermark.upper(), font=wm_font)
        w_text_w = w_bbox[2] - w_bbox[0]
        draw.text((width - pad_x - w_text_w, height - pad_y - wm_font_size), watermark.upper(), font=wm_font, fill=(255, 255, 255, 120))

    return img.convert('RGB')


def main():
    parser = argparse.ArgumentParser(description="Post Image Studio - Blog Cover & Thumbnail Generator")
    parser.add_argument("--title", "-t", type=str, default="Fed Meeting", help="Main title text")
    parser.add_argument("--subtitle", "-s", type=str, default="Federal Open Market Committee Meeting", help="Subtitle text")
    parser.add_argument("--badge", "-b", type=str, default="MACRO & FINANCE", help="Badge text")
    parser.add_argument("--author", "-a", type=str, default="Binary Gap", help="Author text")
    parser.add_argument("--date", "-d", type=str, default="2026.08.30", help="Date text")
    parser.add_argument("--theme", choices=list(THEME_PRESETS.keys()), default="fed-meeting", help="Theme preset")
    parser.add_argument("--platform", choices=list(PLATFORM_DIMENSIONS.keys()), default="naver-header", help="Platform dimension preset")
    parser.add_argument("--pattern", choices=["none", "grid", "dots", "crosses"], default=None, help="Pattern override")
    parser.add_argument("--frame", choices=["none", "minimal-border", "browser-bar", "glass-card", "accent-line"], default=None, help="Frame override")
    parser.add_argument("--badge-bg", type=str, default=None, help="Badge background color override (hex or rgba)")
    parser.add_argument("--badge-text", type=str, default=None, help="Badge text color override (hex or rgba)")
    parser.add_argument("--align", choices=["left", "center", "right"], default="left", help="Text alignment")
    parser.add_argument("--output", "-o", type=str, default="blog_cover.png", help="Output PNG file path")
    parser.add_argument("--scale", type=int, default=2, help="Scale multiplier (1=1x, 2=2x Retina)")

    args = parser.parse_args()

    print(f"🚀 Generating post image...")
    print(f"  • Title: {args.title}")
    print(f"  • Theme: {args.theme}")
    print(f"  • Platform: {args.platform}")
    print(f"  • Pattern: {args.pattern or 'theme default'}")
    print(f"  • Frame: {args.frame or 'theme default'}")
    print(f"  • Scale: {args.scale}x")

    img = create_post_image(
        title=args.title,
        subtitle=args.subtitle,
        badge=args.badge,
        author=args.author,
        date=args.date,
        theme=args.theme,
        platform=args.platform,
        pattern=args.pattern,
        frame=args.frame,
        badge_bg=args.badge_bg,
        badge_text=args.badge_text,
        text_align=args.align,
        scale=args.scale
    )

    img.save(args.output, "PNG")
    print(f"✅ Image successfully saved to: {args.output} ({img.width}x{img.height})")


if __name__ == "__main__":
    main()
