---
layout: default
title: "Novels"
permalink: /novels/
---

<div class="narou-portal-container">
    {% assign all_novels = site.pages | where: "layout", "novel-main" %}
    {% assign novel_pages = all_novels | sort: "title" %}
    {% for np in novel_pages %}
        {% assign episodes = site.posts | where: "series", np.novel_series | sort: "series_order" %}
        {% assign total_eps = episodes | size %}
        {% assign last_ep = episodes | last %}

        <div class="narou-portal-item">
            <div class="narou-item-header">
                <h3 class="narou-item-title">
                    <a href="{{ np.url | relative_url }}">{{ np.title }}</a>
                </h3>
                <span class="narou-item-author">저자: {{ np.author | default: "Colin" }}</span>
            </div>
            
            <div class="narou-item-genre">
                장르: {{ np.genre | default: "소설" }} | 총 {{ total_eps }}화 연재 중
            </div>

            <div class="narou-item-synopsis">
                {{ np.description | escape | truncate: 180 }}
            </div>

            {% if last_ep %}
                <div class="narou-item-latest">
                    최신화: <a href="{{ last_ep.url | relative_url }}">{{ last_ep.series_order }}화 - {{ last_ep.title }}</a>
                    <span class="narou-latest-date">({{ last_ep.date | date: "%Y/%m/%d" }})</span>
                </div>
            {% endif %}
        </div>
    {% endfor %}
</div>

<style>
/* 소설가가 되자 포털 스타일 소설 리스트 */
.narou-portal-container {
    margin-top: 1rem;
}

.narou-portal-title {
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 1.4rem;
    font-weight: 700;
    color: #111;
    border-bottom: 2px solid #222;
    padding-bottom: 0.5rem;
    margin-bottom: 1.5rem;
}

.narou-portal-item {
    border-bottom: 1px solid #ccc;
    padding: 1.2rem 0;
}

.narou-portal-item:last-child {
    border-bottom: none;
}

.narou-item-header {
    clear: both;
    margin-bottom: 0.3rem;
}

.narou-item-header:after {
    content: "";
    display: table;
    clear: both;
}

.narou-item-title {
    margin: 0 !important;
    font-size: 1.15rem !important;
    font-weight: 700;
    float: left;
}

.narou-item-title a {
    color: #002c53 !important;
    text-decoration: none;
}

.narou-item-title a:hover {
    text-decoration: underline !important;
}

.narou-item-author {
    float: right;
    font-size: 0.85rem;
    color: #555;
    margin-top: 0.2rem;
}

.narou-item-genre {
    font-size: 0.8rem;
    color: #666;
}

.narou-item-synopsis {
    font-size: 0.88rem;
    color: #333;
    line-height: 1.6;
    margin-bottom: 0.6rem;
    margin-top: 0.4rem;
}

.narou-item-latest {
    font-size: 0.8rem;
    color: #444;
}

.narou-item-latest a {
    color: #002c53 !important;
    font-weight: bold;
}

.narou-latest-date {
    font-size: 0.75rem;
    color: #777;
    margin-left: 4px;
}
</style>
