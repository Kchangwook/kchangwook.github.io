---
title: Docker 멀티 스테이지 빌드로 이미지 크기 줄이기
date: 2026-11-20 19:00:00 +0900
categories: [DevOps, Docker]
tags: [docker, devops, ci-cd]
---

빌드 도구와 런타임 환경을 분리하는 Docker Multi-stage Build 패턴을 사용하면 최종 컨테이너 이미지 크기를 크게 줄일 수 있습니다.

## Dockerfile 예시

```dockerfile
# Stage 1: Build
FROM gradle:8-jdk21 AS builder
WORKDIR /app
COPY . .
RUN gradle bootJar --no-daemon

# Stage 2: Runtime
FROM eclipse-temurin:21-jre-alpine
WORKDIR /app
COPY --from=builder /app/build/libs/*.jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]
```

## 장점

1. 빌드 도구(JDK, Gradle, 소스 코드)가 최종 이미지에 포함되지 않아 보안 면에서 유리
2. 레이어 캐시를 활용하면 CI/CD 배포 속도와 이미지 pull 시간이 단축됨

> 샘플 게시글입니다. 실제 운영 글 작성 시 삭제하거나 수정해서 사용하세요.
{: .prompt-info }
