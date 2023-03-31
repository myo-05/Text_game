from monster import *
from player import *
import random, time, os, msvcrt
from threading import Timer
from rich import *

os.system("cls")
# 용사이름 받기
print("\n캐릭터를 생성합니다.\n")
print("용사님의 이름은 무엇인가요?")
name = str(input())

time.sleep(1)

os.system("cls")

# 인트로 및 설명글
time.sleep(1)
print("========================게임 설명==========================")
print(f"반갑습니다, [{name}]님.\n")
time.sleep(1)
print("05RPG에 오신 것을 환영합니다.\n")
time.sleep(1)
print("05RPG는 5와 인연이 깊은 게임입니다.\n")
time.sleep(1)
print(f"이제부터 [{name}]님은")
time.sleep(1)
print("\t5가지의 능력치와")
time.sleep(1)
print("\t5가지의 동작")
time.sleep(1)
print("\t5가지의 몬스터를 만날것입니다.\n")
time.sleep(1)
print("그리고 매 전투, 5초 내의 선택을 강요받으실 겁니다.\n")
time.sleep(1)
print("■~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~■\n")
print("5초 룰을 극복하고 '최단시간 플레이'로 몬스터를 무찔러 주세요!\n")
print("■~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~■\n")

while True:
    print(f"계속 하려면 Y키를 입력하세요.")

    ans = msvcrt.getch()
    if ans == b"y" or ans == b"Y":
        os.system("cls")
        break
time.sleep(1)

# 용사의 능력치 랜덤 분배하기 ... (기회5번 제한걸기)
while True:
    os.system("cls")
    print("========================능력치 부여=========================")
    print(f"\n[{name}]님의 능력치를 부여합니다.\n")

    power = random.randrange(1, 11)
    def_ = random.randrange(1, 11)
    int = random.randrange(1, 11)
    luck = random.randrange(1, 11)
    love = random.randrange(1, 11)

    # chance = 5
    print(f"힘: {power} / 방어: {def_} / 지능: {int} / 운 = {luck} / 동료애 = {love}")
    print(f"능력치에 만족하십니까? [Y = 만족] [AnyKey = 능력치재부여]")
    # print(f"능력치를 다시 부여하시겠습니까?(잔여기회:{chance}회) y = 네, n = 아니오")
    ans = msvcrt.getch()
    if ans == b"n" or ans == b"N":
        continue
    elif ans == b"y" or ans == b"Y":
        print(
            f"\n[{name}]님의 능력치는\n 힘: {power} 방어:{def_} 지능:{int} 운:{luck} 동료애:{love} 입니다.\n"
        )
        break

player = Character(name, power, def_, int, luck, love)

# 전투시작 선택
while True:

    print(f"[{name}]님 전투를 시작하시겠습니까? y = 네")
    ans = msvcrt.getch()

    if ans == b"y" or ans == b"Y":
        print(f"\n[{name}]님 건투를 빕니다.\n")
        time.sleep(1)
        os.system("cls")
        break

time.sleep(1)

# 몬스터 리스트
monster = [
    Monster("HTML", 100, 10),
    Monster("CSS", 200, 20),
    Monster("JS", 300, 30),
    Monster("Python", 400, 40),
    Monster("Algorithm", 500, 50),
]


# 게임종료 함수에 사용되는 변수
play = True
time_ = 5

# 게임오버 함수가 사용될 경우, 게임오버 판별용 변수 play가 False가 된다.
def gameover():
    print("\nTime over!\n결단력을 길러오세요..!\n")
    global play
    play = False


# 랜덤으로 몬스터를 생성한다
random_monster = random.choice(monster)
# 배틀함수
def status(func):
    def wrapper():
        os.system("cls")
        print("\n■~~~~~~~~~~~~~~~~~~~~~~~전투모드~~~~~~~~~~~~~~~~~~~~~~~~~~~~■\n")
        # 플레이어의 정보를 보여준다
        player.show_status()

        # 몬스터의 정보를 보여준다
        print(f"\n몬스터 {random_monster.name} 출현!\n")
        random_monster.status_check()
        print("==============================================================\n")

        # 5가지 동작 선택
        print("\n 1.기본공격 2.공격스킬 3. 회복스킬 4.방어스킬 5.카운터")
        print("\n==============================================================")
        print(f"\n          {time_}초 안에 동작을 결정하세요..!\n")
        print("\n==============================================================")
        func()

    return wrapper


@status
def status():
    return


def battle():
    status()
    # 플레이어와 몬스터가 모두 살아있다면 계속 전투, 타임오버가 아니라면 계속 전투
    while player.hp > 0 and random_monster.hp > 0 and play:
        # 전투 시 입력이 5초 내로 없으면 게임종료
        timelimit = Timer(time_, gameover)  # while 문 내에서 정의하면 timer사용가능!
        timelimit.start()
        # 동작을 입력받는다
        action = msvcrt.getch()
        # 타임오버라면 반복문 빠져나가기
        if not play:
            break
        time.sleep(0.1)  # 연속입력 방지
        if action == b"1":
            os.system("cls")
            status()
            timelimit.cancel()
            player.attack(random_monster)
            random_monster.attack(player)
            continue
        elif action == b"2":
            os.system("cls")
            status()
            timelimit.cancel()
            player.special_attack(random_monster)
            random_monster.attack(player)
            continue
        elif action == b"3":
            os.system("cls")
            status()
            timelimit.cancel()
            player.heal(random_monster)
            random_monster.attack(player)
            continue
        elif action == b"4":
            os.system("cls")
            status()
            timelimit.cancel()
            player.defend(random_monster)
            random_monster.attack(player)
            continue
        elif action == b"5":
            os.system("cls")
            status()
            timelimit.cancel()
            player.counter(random_monster)
            random_monster.attack(player)
            continue
        else:
            print("\n정신차리세요! 용사님!")
            continue

    if player.hp <= 0:
        print(f"\n{player.name}님은 한줌의 먼지가 되었습니다.")
    # 몬스터가 죽었다면 경험치를1 올린다.
    elif random_monster.hp <= 0:
        player.ex += 1
        print(f"\n{random_monster.name}이(가) 쓰러졌습니다.")


start_time = time.time()  # 전투 시작시간 저장

# 전투시작
while player.ex < 5:
    random_monster = random.choice(monster)
    battle()
    if not play or player.hp <= 0:
        break
# 전투종료

end_time = time.time()  # 전투 종료시간 저장


# 게임결과
if player.ex == 5:
    print(f"\n{player.name}님 축하합니다! 모든 몬스터를 잡았습니다!")
else:
    print(f"\n{player.name}님 실력을 길러오세요!")

# 플레이가 종료된 시간 - 코드가 시작된 시간으로 실행 시간 구하기 (단위 : 초)
playtime = f"{end_time-start_time:.3f} 초"

print(f"\n[{name}]님은 [{playtime}]동안 전투를 하셨습니다.\n")

# 다시시작(미구현)
