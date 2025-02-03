import re

def validate_password(password):
    # 정규 표현식 패턴
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$'
    
    # 정규 표현식으로 비밀번호 검사
    if re.match(pattern, password):
        return True
    else:
        return False

# 테스트
password = input("비밀번호를 입력해주세요: ")

if validate_password(password):
    print("비밀번호가 유효합니다.")
else:
    print("비밀번호가 유효하지 않습니다. 조건을 확인하세요.")
