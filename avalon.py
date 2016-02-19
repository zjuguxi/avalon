# -*- coding:utf-8 -*-

# 第一部分，定义特殊角色及其属性，创建Characters类
class Characters(object):
    def __init__(self, name,number):
        self.name = name
        self.number = number
    def print_number(self):
        print '%s : %s' % (self.name, self.number)

Merlin = Characters('Merlin', 1)
Percival = Characters('Percival', 2)
Morgana = Characters('Morgana', 3)
Mordred = Characters('Mordred', 4)
Oberon = Characters('Oberon', 5)
Assassin = Characters('Assassin', 6)


# 创建玩家人数统计函数

players_amount = 0

def players_amount_add():
    global players_amount
    players_amount += 1
    return players_amount


# 第二部分，房主创建房间

host_name = raw_input('A room is created, input your name >>>')
maxroom = 001
roomid = 001

if bool(host_name) == True:
    players_amount_add()


# 第三部分，其他人加入房间

enter_room = raw_input('enter the room number >>> ')


player1_name = raw_input('Player1, Now enter your name >>> ')
player2_name = raw_input('Player2, Now enter your name >>> ')
player3_name = raw_input('Player3, Now enter your name >>> ')
player4_name = raw_input('Player4, Now enter your name >>> ')
player5_name = raw_input('Player5, Now enter your name >>> ')
player6_name = raw_input('Player6, Now enter your name >>> ')
player7_name = raw_input('Player7, Now enter your name >>> ')
player8_name = raw_input('Player8, Now enter your name >>> ')
player9_name = raw_input('Player9, Now enter your name >>> ')


if bool(player1_name) == True:
    players_amount_add()

if bool(player2_name) == True:
    players_amount_add()

if bool(player3_name) == True:
    players_amount_add()

if bool(player4_name) == True:
    players_amount_add()

if bool(player5_name) == True:
    players_amount_add()

if bool(player6_name) == True:
    players_amount_add()

if bool(player7_name) == True:
    players_amount_add()

if bool(player8_name) == True:
    players_amount_add()

if bool(player9_name) == True:
    players_amount_add()


# 第四部分，统计人数

print ' There are %s people in this round of Avalon. \r ' % players_amount
  