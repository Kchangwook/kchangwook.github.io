---
title: GitHub Pages와 Jekyll Chirpy로 기술 블로그 시작하기
date: 2026-11-21 12:00:00 +0900
categories: [Blog]
tags: [jekyll, chirpy, github-pages]
---

Jekyll Chirpy 테마와 GitHub Actions를 연동해 기술 블로그를 구축하고 커스터마이징한 과정을 기록합니다.

## 구성 요약

- **테마**: `jekyll-theme-chirpy` 7.6
- **배포**: GitHub Actions (`.github/workflows/pages-deploy.yml`)
- **커스터마이징**:
  - 사이드바 계층형 카테고리 트리 (최대 3-depth 지원)
  - 사이드바 내 검색창 이동 및 상단 헤더 최소화

## 글 작성 체크리스트

- 파일명: `_posts/YYYY-MM-DD-slug.md`
- `categories`: `[대분류, 중분류, 소분류]` 형태로 작성하면 사이드바 트리에 자동 반영
- `tags`: 우측 인기 태그 및 검색에 활용

> 샘플 게시글입니다. 자유롭게 수정하거나 삭제해 주세요.
{: .prompt-info }
