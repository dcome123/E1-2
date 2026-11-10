import json
from pathlib import Path

# 데이터 파일 경로: main.py와 같은 폴더(프로젝트 루트)의 state.json
STATE_FILE = Path(__file__).resolve().parent / "state.json"


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

    def to_dict(self):
        """저장하기 위해 퀴즈를 딕셔너리(dict)로 바꾼다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }


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


def quiz_from_dict(data):
    """딕셔너리를 Quiz 객체로 바꾼다. 형식이 올바르지 않으면 ValueError를 일으킨다."""
    question = data["question"]
    choices = data["choices"]
    answer = data["answer"]
    if not isinstance(question, str) or question.strip() == "":
        raise ValueError("문제 형식 오류")
    if not isinstance(choices, list) or len(choices) != 4:
        raise ValueError("선택지 형식 오류")
    if not all(isinstance(choice, str) for choice in choices):
        raise ValueError("선택지 형식 오류")
    if not isinstance(answer, int) or isinstance(answer, bool) or not 1 <= answer <= 4:
        raise ValueError("정답 형식 오류")
    return Quiz(question, choices, answer)


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


def calc_score(correct, total):
    """맞힌 개수를 100점 만점 점수로 바꿔 돌려준다."""
    return int(correct / total * 100)


class QuizGame:
    """퀴즈 게임 전체를 관리하는 클래스."""

    def __init__(self, state_path=STATE_FILE):
        self.state_path = state_path  # 데이터를 저장할 파일 경로
        self.quizzes = []             # 퀴즈 목록
        self.best_score = None        # 최고 점수 (아직 없으면 None)
        self.load_state()

    def load_state(self):
        """state.json에서 퀴즈와 최고 점수를 불러온다."""
        if not self.state_path.exists():
            print("📂 저장된 데이터가 없어 기본 퀴즈로 시작합니다.")
            self.quizzes = create_default_quizzes()
            return

        try:
            with open(self.state_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            quizzes = [quiz_from_dict(item) for item in data["quizzes"]]
            best_score = data["best_score"]
            if best_score is not None and (
                not isinstance(best_score, int) or isinstance(best_score, bool)
            ):
                raise ValueError("최고 점수 형식 오류")
        except (OSError, ValueError, KeyError, TypeError):
            print("⚠️ 저장 파일을 읽을 수 없거나 손상되었습니다. 기본 퀴즈로 초기화합니다.")
            self.quizzes = create_default_quizzes()
            self.best_score = None
            self.save_state()
            return

        self.quizzes = quizzes
        self.best_score = best_score
        score_text = "없음" if best_score is None else f"{best_score}점"
        print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(quizzes)}개, 최고점수 {score_text})")

    def save_state(self):
        """퀴즈와 최고 점수를 state.json에 저장한다."""
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score,
        }
        try:
            with open(self.state_path, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except OSError:
            print("⚠️ 저장 중 오류가 발생했습니다. 데이터가 저장되지 않았을 수 있습니다.")

    def show_menu(self):
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

    def play_quiz(self):
        """퀴즈를 모두 출제하고, 점수를 최고 점수와 비교한다."""
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가하세요.")
            return

        total = len(self.quizzes)
        correct = 0
        print(f"\n📝 퀴즈를 시작합니다! (총 {total}문제)\n")

        for number, quiz in enumerate(self.quizzes, start=1):
            print("-" * 40)
            quiz.display(number)
            print()
            user_answer = read_int("정답 입력: ", 1, 4)
            if quiz.is_correct(user_answer):
                print("✅ 정답입니다!")
                correct += 1
            else:
                print(f"❌ 틀렸습니다. 정답은 {quiz.answer}번입니다.")

        score = calc_score(correct, total)
        print("=" * 40)
        print(f"🏆 결과: {total}문제 중 {correct}문제 정답! ({score}점)")
        print("=" * 40)
        self.update_best_score(score)

    def update_best_score(self, score):
        """이번 점수가 최고 점수보다 높으면 갱신하고 저장한다."""
        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다!")
            self.save_state()

    def add_quiz(self):
        """새 퀴즈를 입력받아 목록에 추가하고 저장한다."""
        print("\n📌 새로운 퀴즈를 추가합니다.\n")
        question = read_text("문제를 입력하세요: ")
        choices = []
        for number in range(1, 5):
            choices.append(read_text(f"선택지 {number}: "))
        answer = read_int("정답 번호 (1-4): ", 1, 4)
        self.quizzes.append(Quiz(question, choices, answer))
        self.save_state()
        print("\n✅ 퀴즈가 추가되었습니다!\n")

    def list_quizzes(self):
        """등록된 퀴즈의 목록을 보여준다."""
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return

        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)\n")
        print("-" * 40)
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"[{number}] {quiz.question}")
        print("-" * 40)

    def show_best_score(self):
        """최고 점수를 보여준다."""
        if self.best_score is None:
            print("⚠️ 아직 퀴즈를 풀지 않았습니다. 먼저 퀴즈를 풀어 보세요.")
        else:
            print(f"\n🏆 최고 점수: {self.best_score}점\n")

    def run(self):
        """메뉴를 반복해서 보여주며 게임을 진행한다. 끝날 때 항상 저장한다."""
        try:
            while True:
                self.show_menu()
                choice = read_int("선택: ", 1, 5)
                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.list_quizzes()
                elif choice == 4:
                    self.show_best_score()
                else:
                    print("프로그램을 종료합니다.")
                    break
        except (KeyboardInterrupt, EOFError):
            print("\n입력이 중단되어 안전하게 종료합니다.")
        finally:
            self.save_state()


def main():
    """프로그램의 시작점."""
    game = QuizGame()
    game.run()


if __name__ == "__main__":
    main()