# 영화 추천 커뮤니티 서비스 (Django Skeleton)

## 프로젝트 개요
- 기존 Django skeleton(`mypjt`)을 기반으로 영화 추천 커뮤니티 서비스를 구현했습니다.
- 핵심 목표는 Axios 기반 AJAX 비동기 통신으로, 페이지 새로고침 없이 상태를 갱신하는 것입니다.

## 사용 기술
- Python
- Django 5.2
- JavaScript
- Axios
- Bootstrap 5

## 구현 기능
- 유저 팔로우 AJAX (`/accounts/<user_pk>/follow/`)
  - 팔로우/언팔로우 토글
  - 팔로워/팔로잉 수 실시간 갱신
- 리뷰 좋아요 AJAX (`/community/<review_pk>/like/`)
  - 좋아요/좋아요 취소 토글
  - 좋아요 수 실시간 갱신
- 영화 장르 필터링 AJAX (`/movies/filter-genre/`)
  - 장르 선택 시 필터링된 영화 목록 JSON 응답
  - 목록 영역 부분 갱신
- 영화 추천 기능 (`/movies/recommended/`)
  - 로그인 사용자: 좋아요한 리뷰의 영화 장르 기반 추천
  - 데이터 부족 시: `popularity`, `vote_average` 기반 폴백 추천

## URL 구조
- `accounts/`
  - `/accounts/signup/`
  - `/accounts/login/`
  - `/accounts/logout/`
  - `/accounts/profile/<username>/`
  - `/accounts/<user_pk>/follow/`
- `community/`
  - `/community/`
  - `/community/create/`
  - `/community/<review_pk>/`
  - `/community/<review_pk>/comments/create/`
  - `/community/<review_pk>/like/`
- `movies/`
  - `/movies/`
  - `/movies/filter-genre/`
  - `/movies/recommended/`

## Git branch / commit 전략 예시
- 브랜치 전략
  - `main`: 배포 가능한 안정 브랜치
  - `develop`: 통합 개발 브랜치
  - `feature/ajax-follow-like-filter`: 기능 단위 브랜치
- 커밋 전략 예시
  - `feat(accounts): implement AJAX follow toggle view and profile UI`
  - `feat(community): implement AJAX like toggle for review index`
  - `feat(movies): implement genre filter JSON API and index AJAX rendering`
  - `feat(movies): add recommendation page with internal data-based algorithm`
  - `docs: add project README with setup and feature summary`

## 구현 과정에서 어려웠던 점
- 기존 skeleton의 URL/name/context 구조를 유지하면서 AJAX 응답을 추가해야 했습니다.
- 템플릿 문자열 일부가 깨진 상태여서, 기능 흐름을 해치지 않는 최소 범위 내에서 템플릿을 보완했습니다.
- 일반 요청 흐름(render/redirect)과 AJAX(JsonResponse) 흐름을 동시에 만족하도록 분기 처리가 필요했습니다.

## 새로 배운 점
- Django 함수형 뷰에서 `X-Requested-With` 헤더를 활용한 AJAX 분기 처리 방법
- Axios + CSRF(`X-CSRFToken`) 조합으로 안전한 POST 비동기 요청 처리
- ManyToMany 관계 기반 토글(팔로우, 좋아요)과 즉시 DOM 반영 패턴

## 실행 방법
1. 가상환경 생성
   - `python -m venv venv`
2. 가상환경 활성화 (PowerShell)
   - `.\venv\Scripts\Activate.ps1`
3. 패키지 설치
   - `pip install -r requirements.txt`
4. 마이그레이션
   - `python manage.py migrate`
5. 영화 fixture 로드
   - `python manage.py loaddata movies/fixtures/movies/movies.json`
6. 서버 실행
   - `python manage.py runserver`
