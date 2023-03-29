import random, time, os
from threading import Timer


# 몬스터의 기본정보
class Monster:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.ex = 1

    def attack(self, other):
        time.sleep(0.5)
        damage = random.randint(int(self.damage * 0.8), int(self.damage * 1.2))
        other.hp = max(other.hp - damage, 0)
        self.attack_name = random.choice(
            ["세미콜론 지우기!", "Error 공격!", "오타 공격!", "이게 왜 돼? 왜 안 돼? | 부조리공격!"]
        )
        print(
            f"\n{self.name}의 {self.attack_name}\n\n\t{damage}만큼의 공격을 받아 HP가 {other.hp} 되었습니다."
        )

    def status_check(self):
        print(f"{self.name}의 HP : {self.hp} 공격력 : {self.damage}")


# # 몬스터 HTML
# class HTML_Monster(Monster):
#     def __init__(self, other):
#         super().__init__()
#         other
#     # 부모 클래스에 존재하는 status_check 메소드를 overriding 합니다.
#     def status_check(self):
#         print(f"HTML의 HP : {self.hp}")


# # 몬스터 CSS
# class CSS_Monster(Monster):
#     def __init__(self, other):
#         super().__init__()

#     def status_check(self):
#         print(f"CSS의 HP : {self.hp}")


# # 몬스터 JS
# class JS_Monster(Monster):
#     def __init__(self, other):
#         super().__init__()

#     def status_check(self):
#         print(f"JS의 HP : {self.hp}")


# # 몬스터 Python
# class Python_Monster(Monster):
#     def __init__(self, other):
#         super().__init__()

#     def status_check(self):
#         print(f"Python의 HP : {self.hp}")


# # 몬스터 알고리즘
# class Algorithm_Monster(Monster):
#     def __init__(self, other):
#         super().__init__()

#     def status_check(self):
#         print(f"Algorithm의 HP : {self.hp}")
