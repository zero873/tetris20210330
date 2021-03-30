print("게임을 시작합니다")
print("테트리스 시작")
##### 여기서 부터 반복 ######
for i in range(10):
    print("1. 오른쪽 2. 왼쪽 3. 블록 바꾸기")
    number = input("숫자를 입력하세요: ")
    print("당신이 입력한 숫자는?",number)
    if int(number) == 1:
        print("오른쪽으로 이동")
    if int(number) == 2:
        print("왼쪽으로 이동")
    if int(number) == 3:
        print("블록 바꾸기")
##### 반복 종료 ######