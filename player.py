import random, time, os
from threading import Timer
import msvcrt

# 캐릭터 기본정보
class Character:
    # 캐릭터의 기본 능력치
    def __init__(self, name, power, def_, int, luck, love, hp=700, mp=100):
        self.name = name
        self.max_hp = max(hp, 700)
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.power = power
        self.def_ = def_
        self.int = int
        self.luck = luck
        self.love = love
        self.ex = 0

    ################## 기본공격 power ##########################
    def attack(self, other):
        damage = random.randint(self.power * 9, self.power * 11)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")

    ################### 공격스킬 스파르타! int #############################
    def special_attack(self, other):

        if self.mp <= 0:
            print(f"MP가 부족합니다.\n당황한 틈에 기습을 당합니다!\n")
            return

        damage = random.randint(self.int * 2, self.int * 3)
        other.hp = max(other.hp - damage, 0)
        self.mp -= 10
        print(
            f"[{self.name}]의 공격스킬! 스.파.르.타!\n\n\t{other.name}에게 [{damage}]의 데미지를 입혔습니다."
        )

    ##################### 회복스킬 중꺾그마! love ##########################
    def heal(self, other):

        if self.mp <= 0:
            print(f"MP가 부족합니다.\n당황한 틈에 기습을 당합니다!\n")
            return

        heal = self.max_hp * 0.1 * self.love
        self.hp += heal
        self.mp -= 10

        print(
            f"[{self.name}]님의 회복스킬! 중.꺾.그.마!\n\n\t[{self.name}]님의 체력이 {heal}회복 되었습니다."
        )

    ####################### 방어스킬 중꺾마! def_##########################
    def defend(self, other):

        self.hp += self.def_

        print(f"{self.name}의 방어! 중.꺾.마 !\n\n\t{other.name}의 다음 공격의 데미지가 감소합니다.")

    ####################### 카운터 키미노 나마에와! luck ############################
    def counter(self, other):
        # 입력시간 3초 제한
        countertime = False

        def timeover():
            print("\n입력시간이 초과되었습니다.")
            global countertime
            countertime = True
            self.hp = max(self.hp - damage, 0)
            print(f"\n{self.name}님이 카운터 실패로 {damage}만큼의 역관광를 입었습니다.")
            return True

        timeout = 3
        t = Timer(timeout, timeover)
        t.start()

        print(
            f"{self.name}의 카운터공격! 키.미.노.나.마.에.와!\n\n\t {timeout} 초 안에 {other.name}의 이름을 입력하세요!"
        )
        damage = random.randint(self.luck * 2, self.luck * 99)
        # 입력받기
        ans = str(input())
        if ans == other.name:
            t.cancel()
            other.hp = max(other.hp - damage, 0)
            print(f"\n{other.name}이(가) {damage}만큼의 카운터데미지를 입었습니다. HP: {other.hp}")
        elif ans != other.name and countertime:
            t.cancel()
            self.hp = max(self.hp - damage, 0)
            print(f"\n{self.name}님이 카운터 실패로 {damage}만큼의 역관광를 입었습니다.")

    ################ 상태보여주기####################
    def show_status(self):
        print(
            f"{self.name}의 상태: HP {self.hp}/{self.max_hp} | MP {self.mp}/{self.max_mp} | EX {self.ex}/5"
        )
