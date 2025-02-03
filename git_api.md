# GitHub API를 사용하여 사용자 정보 확인하기

GitHub API는 GitHub 플랫폼에서 다양한 데이터를 가져오거나 조작하는 데 사용할 수 있는 RESTful API입니다. 이 문서에서는 GitHub 사용자 정보를 확인하는 방법에 대해 설명합니다.

## 1. GitHub API 개요

GitHub API는 여러 엔드포인트를 통해 GitHub의 다양한 리소스를 조회하거나 수정할 수 있게 해줍니다. 사용자 정보 조회를 위한 API는 `GET /users/{username}` 엔드포인트를 사용합니다. 이 API를 통해 특정 GitHub 사용자의 정보를 JSON 형식으로 반환받을 수 있습니다.

## 2. 사용자 정보 가져오기

GitHub 사용자 정보를 조회하기 위해서는 `GET /users/{username}` 엔드포인트를 사용합니다. 이 요청을 통해 반환되는 정보는 사용자의 프로필, 공개 저장소, 팔로워 수, 팔로우 수 등 다양한 정보를 포함합니다.

### 주요 반환 정보

- **login**: GitHub 사용자 이름
- **id**: 사용자의 고유 식별자
- **avatar_url**: 사용자 프로필 이미지 URL
- **html_url**: 사용자의 GitHub 프로필 페이지 URL
- **followers_url**: 사용자의 팔로워 목록 URL
- **following_url**: 사용자가 팔로우하는 사람 목록 URL
- **repos_url**: 사용자의 공개 저장소 목록 URL
- **public_repos**: 사용자가 만든 공개 저장소의 수
- **followers**: 사용자의 팔로워 수
- **following**: 사용자가 팔로우하는 사람 수
- **created_at**: 사용자의 계정 생성 일자
- **updated_at**: 사용자의 정보가 마지막으로 업데이트된 일자

## 3. 오류 처리

GitHub API는 다양한 오류 상황에 대해 HTTP 상태 코드를 반환합니다.

- **404 Not Found**: 요청한 사용자가 존재하지 않는 경우
- **403 Forbidden**: 요청이 제한된 경우 (예: 요청 횟수 초과)
- **500 Internal Server Error**: 서버 내부 오류가 발생한 경우

### 오류 응답 예시

존재하지 않는 사용자를 요청한 경우, GitHub은 `404 Not Found` 상태 코드와 함께 아래와 같은 메시지를 반환합니다:

```json
{
  "message": "Not Found",
  "documentation_url": "https://docs.github.com/rest/reference/users#get-a-user"
}
```

## 4. 인증
API 호출을 인증 없이 사용할 수 있지만, 요청 제한에 도달하면 API 호출이 제한될 수 있습니다. 인증을 사용하면 더 많은 요청을 처리할 수 있습니다.

- Basic Authentication: GitHub 사용자명과 비밀번호를 사용한 인증
- OAuth Tokens: OAuth 토큰을 사용하여 인증

## 5. API 호출 제한
GitHub API는 인증되지 않은 요청에 대해 시간당 60회 호출을 허용합니다. 인증을 통해 최대 5000회까지 요청을 보낼 수 있습니다.

- 인증되지 않은 호출: 시간당 60회
- 인증된 호출: 시간당 5000회
## 6. 참고 자료
GitHub API 공식 문서: https://docs.github.com/rest/reference/users
인증 방법 및 토큰 생성: https://docs.github.com/authentication

## 결론
GitHub API의 GET /users/{username} 엔드포인트를 사용하면 특정 사용자의 정보를 쉽게 조회할 수 있습니다. 이 API는 사용자 이름, 프로필 이미지, 팔로워 수, 공개 저장소 등의 유용한 정보를 제공합니다. 인증을 통해 더 많은 요청을 처리할 수 있으며, 다양한 오류 코드와 상태를 통해 API 호출 상태를 파악할 수 있습니다.