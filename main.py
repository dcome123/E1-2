def show_menu():
    """메뉴 화면을 보여준다."""
    print("=" * 40)
    print("       🎯 나만의 퀴즈 게임 🎯")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 40)


def read_int(prompt, low, high):
    """low~high 사이의 정수를 올바르게 입력할 때까지 계속 묻는다."""
    while True:
        text = input(prompt).strip()  # 앞뒤 공백 제거
        if text == "":
            print("⚠️ 빈 입력입니다. 숫자를 입력하세요.")
            continue
        try:
            number = int(text)
        except ValueError:
            print(f"⚠️ 잘못된 입력입니다. {low}-{high} 사이의 숫자를 입력하세요.")
            continue
        if number < low or number > high:
            print(f"⚠️ 잘못된 입력입니다. {low}-{high} 사이의 숫자를 입력하세요.")
            continue
        return number


def main():
    """프로그램의 시작점. 메뉴를 반복해서 보여준다."""
    try:
        while True:
            show_menu()
            choice = read_int("선택: ", 1, 5)
            if choice == 1:
                print("퀴즈 풀기는 준비 중입니다.")
            elif choice == 2:
                print("퀴즈 추가는 준비 중입니다.")
            elif choice == 3:
                print("퀴즈 목록은 준비 중입니다.")
            elif choice == 4:
                print("점수 확인은 준비 중입니다.")
            else:
                print("프로그램을 종료합니다.")
                break
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 안전하게 종료합니다.")


if __name__ == "__main__":
    main()