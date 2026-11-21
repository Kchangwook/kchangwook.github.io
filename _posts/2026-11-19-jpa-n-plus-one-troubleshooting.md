---
title: JPA N+1 문제 원인과 해결 방법 비교
date: 2026-11-19 14:30:00 +0900
categories: [Backend, Spring, JPA]
tags: [spring, jpa, performance, backend]
---

연관 엔티티를 조회할 때 흔히 발생하는 JPA N+1 문제의 원인과 대표적인 해결 전략을 비교합니다.

## 1. N+1 문제가 발생하는 이유

1번의 목록 조회 쿼리 이후, 각 엔티티의 지연 로딩(`LAZY`) 연관 객체를 순회할 때마다 추가 쿼리가 N번 실행됩니다.

## 2. 해결 방법

### Fetch Join

```java
@Query("select o from Order o join fetch o.member")
List<Order> findAllWithMember();
```

- 단일 쿼리로 연관 데이터를 함께 가져옴
- 컬렉션(`OneToMany`) 페치 조인 시 페이징(`Pageable`)과 함께 사용하면 메모리 페이징 경고가 발생하므로 주의

### `@BatchSize` / `default_batch_fetch_size`

```yaml
spring:
  jpa:
    properties:
      hibernate:
        default_batch_fetch_size: 100
```

- `IN` 절로 묶어 조회하므로 컬렉션 페이징에도 안전하게 적용 가능

> 샘플 게시글입니다. 실제 운영 글 작성 시 삭제하거나 수정해서 사용하세요.
{: .prompt-tip }
