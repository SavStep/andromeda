from random import random


class Character():
    def __init__(self,name,xray):
        self.name = name
        self.heatlh = 100
        self.mana = 0
        self.xray = xray
    def attack(self,enemy_name,enemy_health):
        enemy_health -= 5
        self.mana +=2
        print(f'{self.name} атакует персонажа по имени {enemy_name}, оставляя у него {enemy_health} жизней')
        return enemy_health
    
    def super_attack(self,enemy_name,enemy_health):
        enemy_health -= 12
        self.mana -= 6
        ulta = random.choice(self.xray)
        print(f'{self.name} атакует персонажа по имени {enemy_name} исползуя {ulta} , оставляя у него {enemy_health} жизней')
        return enemy_health
    
scorpion = Character(name =  'скорпион',xray=['GET OVER HERE','АТАКА ЦЕПЬЮ'])
alien = Character(name =  'чужой',xray=['поглощение мозгов','кислотное море'])
joker = Character(name =  'джокер',xray=['убийственная шутка','смехо-бомба'])
enemies = [scorpion,alien,joker]
enemy1 = random.choice(enemies)
enemies.remove(enemy1)
enemy2 = random.choice(enemies)
print(f'{enemy1.name} vs {enemy2.name}')
import time
while True:
    enemy2.heatlh = enemy1.attack(enemy2.name,enemy2.heatlh)
    enemy1.heatlh = enemy2.attack(enemy1.name,enemy1.heatlh)
    time.sleep(2)
    coin = random.randint(1,2)
    if enemy1.mana <7:
        if coin ==1:
            enemy2.heatlh = enemy1.super_attack(enemy2.name,enemy2.heatlh)
            enemy1.mana-=7
    if enemy2.mana <7:
        if coin ==1:
            enemy1.heatlh = enemy2.super_attack(enemy1.name,enemy1.heatlh)
            enemy2.mana-=7
    if enemy2.heatlh <=0 and enemy1.heatlh<=0:
        print('Ничья')
        break
    elif enemy2.heatlh <=0:
        print(f'{enemy1.name}name')
    elif enemy1.heatlh <=0:
        print(f'{enemy2.name}name')
