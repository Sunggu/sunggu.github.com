# Binarygap Log

한걸음 차근차근 걸어가며 그 간극을 메꾸듯이, 꾸준하고 성실하게 성장하며 기록하는 Colin의 블로그 저장소입니다.

본 블로그는 GitHub Pages와 Jekyll을 기반으로 구축되었으며, SEO(검색 엔진 최적화)가 적용되어 있습니다.

## 시작하기

### 로컬 환경에서 실행하기

블로그를 로컬 환경에서 테스트하고 실행하려면 다음 명령어를 사용합니다.

```bash
# 의존성 패키지 설치
bundle install

# 로컬 서버 실행
bundle exec jekyll serve
```

서버가 실행되면 [http://localhost:4000](http://localhost:4000)에서 블로그를 확인할 수 있습니다.

## 포스트 작성 방법

새로운 글을 작성하려면 `_posts` 디렉토리에 `YYYY-MM-DD-001-title.md` 형식으로 파일을 생성합니다.

```markdown
---
layout: post
title: "포스트 제목"
date: YYYY-MM-DD HH:MM:SS +0900
categories: [카테고리명]
tags: [태그1, 태그2]
---

여기에 본문을 작성합니다.
```

### 글끼리 연결할 때

`_posts` 안의 글에서 다른 포스트로 링크할 때는 Jekyll의 `{% raw %}{% post_url ... %}{% endraw %}` 태그를 사용합니다.

```markdown
[소설 설정 - 그랜드 타임라인]({% raw %}{% post_url moon-sherpa/2026-07-13-004-grand-timeline %}{% endraw %})
```

- 링크 텍스트나 `{% raw %}{% post_url ... %}{% endraw %}` 부분을 백틱으로 감싸지 않습니다.
- `/grand-timeline` 같은 직접 경로보다 `post_url`을 쓰면 permalink 변경에도 안전합니다.

## 소설 등록 방법

`novels` 페이지에 작품을 보이게 하려면 포스트만 추가하는 것으로는 부족하고, 작품 대표 페이지도 함께 필요합니다.

작동 방식:

- `_pages/*.md`에 `layout: novel-main` 페이지를 둡니다.
- 그 페이지의 `novel_series` 값과 각 포스트의 `series` 값이 정확히 같아야 합니다.
- `novels` 페이지는 `layout: novel-main`인 페이지들을 모아서 자동으로 목록을 만듭니다.
- 각 에피소드는 `series_order` 값으로 정렬됩니다.

작성 규칙:

- 포스트 파일명은 `YYYY-MM-DD-001-title.md` 형식을 사용합니다.
- `series_order`는 1부터 시작하는 숫자로 적습니다.
- 영문 작품은 `series`, `novel_series`, 대표 페이지 제목을 모두 영어 문자열로 맞춥니다.
- 시리즈 내비게이션이나 목차가 있는 경우, 파일명과 `series_order`를 서로 맞춰서 관리합니다.

예시:

```yaml
---
layout: novel-main
title: "English Learning"
novel_series: "English Learning"
permalink: /novels/english-learning/
nav_exclude: true
---
```

```yaml
---
layout: post
title: "Episode 1"
series: "English Learning"
series_order: 1
---
```

## SEO 및 설정 변경

`_config.yml` 파일에서 다음 설정을 변경할 수 있습니다.

- **Google Search Console 등록**: `google_site_verification`에 인증 코드를 입력합니다.
- **네이버 웹마스터 도구 등록**: `naver_site_verification`에 인증 코드를 입력합니다.

## 라이선스

- 소스 코드: [MIT License](LICENSE.md)에 따라 라이선스가 부여됩니다.
- 웹사이트 콘텐츠: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 라이선스를 따릅니다.
