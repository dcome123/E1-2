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


if __name__ == "__main__":
    main()