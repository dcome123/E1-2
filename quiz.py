import random

questions = [
    ("가장 빠른 닭은?", "후다닥"),
    ("인어공주의 성씨는?", "언더 더씨"),
    ("세상에서 가장 지루한 중학교는?", "로딩중"),
    ("바나나가 웃으면?", "바나나킥"),
    ("쇼핑을 가장 좋아하는 동물은?", "사자"),
]

score = 0
random.shuffle(questions)

print("=== 퀴즈 게임 ===")
for question, answer in questions:
    ans = input(question + " > ")
    if ans == answer:
        print("정답! ✅")
        score += 1
    else:
        print(f"오답! 정답은 '{answer}' 입니다. ❌")

print(f"최종 점수: {score}/{len(questions)}")
