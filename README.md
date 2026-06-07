# Starkapin's Blog

개인 개발 지식과 일상을 기록하는 블로그 저장소입니다.

본 블로그는 GitHub Pages와 Jekyll을 기반으로 구축되었으며, SEO(검색 엔진 최적화)가 적용되어 있습니다.

## 🚀 시작하기

### 로컬 환경에서 실행하기

블로그를 로컬 환경에서 테스트하고 실행하려면 다음 명령어를 사용합니다.

```bash
# 의존성 패키지 설치
bundle install

# 로컬 서버 실행
bundle exec jekyll serve
```

서버가 실행되면 [http://localhost:4000](http://localhost:4000)에서 블로그를 확인할 수 있습니다.

## 📝 포스트 작성 방법

새로운 글을 작성하려면 `_posts` 디렉토리에 `YYYY-MM-DD-title.md` 형식으로 파일을 생성합니다.

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

## 🛠️ SEO 및 설정 변경

`_config.yml` 파일에서 다음 설정을 변경할 수 있습니다.

- **Google Search Console 등록**: `google_site_verification`에 인증 코드를 입력합니다.
- **네이버 웹마스터 도구 등록**: `naver_site_verification`에 인증 코드를 입력합니다.

## 📄 라이선스

- 소스 코드: [MIT License](LICENSE.md)에 따라 라이선스가 부여됩니다.
- 웹사이트 콘텐츠: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 라이선스를 따릅니다.
