while True:
    # 사용자로부터 입력 받기
    user_input = input("문장을 입력해주세요: ")

    # '!quit'을 입력하면 종료
    if user_input == "!quit":
        print("프로그램을 종료합니다.")
        break
    
    # 입력 받은 문장 그대로 출력
    print("입력하신 문장은:", user_input)

