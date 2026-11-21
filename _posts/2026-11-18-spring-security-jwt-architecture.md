---
title: Spring Security와 JWT 기반 인증 아키텍처 정리
date: 2026-11-18 10:00:00 +0900
categories: [Backend, Spring, Security]
tags: [spring, security, jwt, backend]
---

Spring Security 환경에서 세션을 사용하지 않는(Stateless) JWT 인증 구조를 구성할 때 핵심이 되는 필터 체인과 토큰 검증 흐름을 정리합니다.

## 1. SecurityFilterChain 기본 설정

`SessionCreationPolicy.STATELESS`로 설정하고, `UsernamePasswordAuthenticationFilter` 앞에 커스텀 JWT 필터를 등록합니다.

```java
@Bean
public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
    return http
        .csrf(AbstractHttpConfigurer::disable)
        .sessionManagement(sm -> sm.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
        .authorizeHttpRequests(auth -> auth
            .requestMatchers("/api/auth/**").permitAll()
            .anyRequest().authenticated()
        )
        .addFilterBefore(jwtAuthenticationFilter, UsernamePasswordAuthenticationFilter.class)
        .build();
}
```

## 2. Access Token과 Refresh Token 분리

- **Access Token**: 짧은 만료 시간(예: 15~30분)으로 API 인가에 사용
- **Refresh Token**: HttpOnly 쿠키 또는 서버 저장소(Redis)와 함께 관리하여 재발급 및 강제 만료 지원

> 샘플 게시글입니다. 실제 운영 글 작성 시 삭제하거나 수정해서 사용하세요.
{: .prompt-info }
