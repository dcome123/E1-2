class Quiz:
    """퀴즈 한 문제를 나타내는 클래스."""

    def __init__(self, question, choices, answer):
        self.question = question  # 문제 (str)
        self.choices = choices    # 선택지 4개 (list)
        self.answer = answer      # 정답 번호 1~4 (int)

    def display(self, number=None):
        """문제와 선택지를 화면에 보여준다."""
        if number is not None:
            print(f"[문제 {number}]")
        print(self.question)
        print()
        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")

    def is_correct(self, user_answer):
        """고른 번호가 정답이면 True, 아니면 False를 돌려준다."""
        return user_answer == self.answer


def create_default_quizzes():
    """처음 실행할 때 사용하는 기본 퀴즈 8문제를 만들어 돌려준다."""
    return [
        # 코딩
        Quiz(
            "컴퓨터에게 할 일을 순서대로 적어 놓은 것을 무엇이라고 할까요?",
            ["노래", "편지", "프로그램", "사진"],
            3,
        ),
        Quiz(
            "프로그램이 제대로 움직이지 않을 때, 잘못된 곳(버그)을 찾아 고치는 일을 무엇이라고 할까요?",
            ["디버깅", "다운로드", "업로드", "로그인"],
            1,
        ),
        # 인공지능 기초
        Quiz(
            "사람처럼 배우고 판단하는 능력을 컴퓨터에 갖추게 한 기술은 무엇일까요?",
            ["블루투스", "프린터", "전자레인지", "인공지능(AI)"],
            4,
        ),
        Quiz(
            "다음 중 인공지능이 쓰인 예로 가장 알맞은 것은 무엇일까요?",
            [
                "손으로 돌려 쓰는 연필깎이",
                "말을 알아듣고 대답하는 음성 비서",
                "전기 없이 켜는 촛불",
                "종이에 쓰는 일기장",
            ],
            2,
        ),
        # 인공지능 학습방법
        Quiz(
            "인공지능이 많은 예시(데이터)를 보고 규칙을 스스로 배우는 방법은 무엇일까요?",
            ["머신러닝(기계학습)", "청소하기", "타자 연습", "줄넘기"],
            1,
        ),
        Quiz(
            "선생님이 정답을 알려주면서 가르치듯, 정답이 붙은 데이터로 배우는 방법은 무엇일까요?",
            ["강화학습", "비지도학습", "지도학습", "전이학습"],
            3,
        ),
        # 데이터의 종류
        Quiz(
            "사진이나 그림처럼 눈으로 보는 데이터를 무엇이라고 할까요?",
            ["소리 데이터", "숫자 데이터", "글자 데이터", "이미지 데이터"],
            4,
        ),
        Quiz(
            "다음 중 글자(텍스트) 데이터의 예는 무엇일까요?",
            [
                "친구에게 보낸 문자 메시지",
                "찍어 둔 가족 사진",
                "녹음한 노랫소리",
                "그려 놓은 그림",
            ],
            1,
        ),
    ]


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


def read_text(prompt):
    """빈 입력이 아닌 글자를 입력받을 때까지 계속 묻는다."""
    while True:
        text = input(prompt).strip()
        if text == "":
            print("⚠️ 빈 입력입니다. 내용을 입력하세요.")
            continue
        return text


def play_quiz(quizzes):
    """퀴즈를 모두 출제하고 (맞힌 개수, 전체 개수)를 돌려준다."""
    if not quizzes:
        print("⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가하세요.")
        return None

    total = len(quizzes)
    correct = 0
    print(f"\n📝 퀴즈를 시작합니다! (총 {total}문제)\n")

    for number, quiz in enumerate(quizzes, start=1):
        print("-" * 40)
        quiz.display(number)
        print()
        user_answer = read_int("정답 입력: ", 1, 4)
        if quiz.is_correct(user_answer):
            print("✅ 정답입니다!")
            correct += 1
        else:
            print(f"❌ 틀렸습니다. 정답은 {quiz.answer}번입니다.")

    score = int(correct / total * 100)
    print("=" * 40)
    print(f"🏆 결과: {total}문제 중 {correct}문제 정답! ({score}점)")
    print("=" * 40)
    return correct, total


def add_quiz(quizzes):
    """새 퀴즈를 입력받아 목록에 추가한다."""
    print("\n📌 새로운 퀴즈를 추가합니다.\n")
    question = read_text("문제를 입력하세요: ")
    choices = []



def main():
    """프로그램의 시작점. 메뉴를 반복해서 보여준다."""
    quizzes = create_default_quizzes()
    try:
        while True:
            show_menu()
            choice = read_int("선택: ", 1, 5)
            if choice == 1:
                play_quiz(quizzes)
            elif choice == 2:
                add_quiz(quizzes)
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