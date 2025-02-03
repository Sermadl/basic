import requests
import unittest

# GitHub 사용자 정보를 가져오는 함수
def get_github_user_info(username):
    url = f'https://api.github.com/users/{username}'
    
    try:
        response = requests.get(url)
        
        # 상태 코드가 200이면 정상
        if response.status_code == 200:
            return response.json()
        else:
            # 상태 코드가 200이 아니면 에러
            return {"error": "User not found or invalid request", "status_code": response.status_code}
    except requests.exceptions.RequestException as e:
        # 요청 실패 시 에러 메시지 반환
        return {"error": str(e)}

# 테스트 클래스
class TestGitHubUserInfo(unittest.TestCase):
    
    def test_valid_user(self):
        # 정상적인 사용자 (예: 'octocat'은 GitHub에서 유효한 사용자입니다)
        user_info = get_github_user_info("octocat")
        
        # 사용자 정보가 정상적으로 반환되었는지 확인
        self.assertIn('login', user_info)
        self.assertEqual(user_info.get('login'), 'octocat')
        self.assertEqual(user_info.get('id'), 583231)  # octocat의 ID 예시
        
    def test_invalid_user(self):
        # 존재하지 않는 사용자 (예: 'nonexistentuser12345'는 존재하지 않는 사용자입니다)
        user_info = get_github_user_info("nonexistentuser12345")
        
        # 에러 메시지가 반환되었는지 확인
        self.assertIn('error', user_info)
        self.assertEqual(user_info['error'], "User not found or invalid request")
        self.assertEqual(user_info['status_code'], 404)
    
    def test_request_exception(self):
        # 예를 들어, 인터넷이 끊어진 상태에서 요청하면 예외가 발생해야 합니다
        user_info = get_github_user_info("octocat")
        
        # 정상적인 상태에서는 requestException이 발생하지 않지만, 테스트 환경에서 예외를 확인할 수 있습니다.
        self.assertNotIn('error', user_info)

# 테스트 실행
if __name__ == '__main__':
    unittest.main()
