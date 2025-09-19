# guess_the_number.py
# random 라이브러리는 무작위 숫자를 만드는 함수입니다. 
import random

def guess_the_number():
    """숫자 맞추기 게임의 메인 함수입니다."""
    
    # 1. 컴퓨터가 1부터 100 사이의 비밀 숫자를 하나 고릅니다.
    secret_number = random.randint(1, 100)
    attempts = 0 # 사용자가 시도한 횟수를 저장할 변수
    
    print("🎉 숫자 맞추기 게임에 오신 것을 환영합니다! 🎉")
    print("제가 1부터 100 사이의 숫자를 하나 생각했습니다. 맞춰보세요!")

    # 2. 사용자가 숫자를 맞출 때까지 무한 반복합니다.
    while True:
        try:
            # 3. 사용자로부터 숫자를 입력받습니다.
            guess_str = input("당신의 추측은? ")
            guess = int(guess_str) # 입력받은 글자를 숫자로 변환
            
            attempts += 1 # 시도 횟수 1 증가
            
            # 4. 사용자의 추측과 비밀 숫자를 비교하여 힌트를 줍니다.
            if guess < secret_number:
                print("⬆️ 너무 작아요! 더 큰 숫자입니다.")
            elif guess > secret_number:
                print("⬇️ 너무 커요! 더 작은 숫자입니다.")
            else:
                # 5. 숫자를 맞췄을 경우, 축하 메시지를 출력하고 게임을 종료합니다.
                print(f"✨ 정답입니다! 축하합니다! ✨")
                print(f"총 {attempts}번 만에 맞추셨네요!")
                break # while 반복문을 탈출하여 게임 종료
                
        except ValueError:
            # 사용자가 숫자가 아닌 다른 것을 입력했을 때의 예외 처리
            print("😥 잘못된 입력입니다. 숫자만 입력해주세요.")

# 이 스크립트 파일이 직접 실행될 때만 게임을 시작합니다.
if __name__ == "__main__":
    guess_the_number()
