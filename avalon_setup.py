# -*- coding:utf-8 -*-
from random import choice

import avalon
from avalon import players_amount
from avalon import host_name
from avalon import player1_name
from avalon import player2_name
from avalon import player3_name
from avalon import player4_name
from avalon import player5_name
from avalon import player6_name
from avalon import player7_name
from avalon import player8_name
from avalon import player9_name

'''
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
Loyalist1 = Characters('Loyalist1', 7)
Loyalist2 = Characters('Loyalist1', 8)
Loyalist3 = Characters('Loyalist1', 9)
Loyalist4 = Characters('Loyalist1', 10)
Minion = Characters('Minion', 11)
'''


if players_amount == 5:

    character_list = ['Merlin', 'Percival', 'Loyalist1', 'Morgana', 'Assassin']

    host_character = choice(character_list)
    character_list.remove(host_character)
    
    player1_character = choice(character_list)
    character_list.remove(player1_character)

    player2_character = choice(character_list)
    character_list.remove(player2_character)

    player3_character = choice(character_list)
    character_list.remove(player3_character)

    player4_character = choice(character_list)

    print host_character
    print player1_character
    print player2_character
    print player3_character
    print player4_character

    print '%s\'s character is %s.' % (host_name, host_character)
    print '%s\'s character is %s.' % (player1_name, player1_character)
    print '%s\'s character is %s.' % (player2_name, player2_character)
    print '%s\'s character is %s.' % (player3_name, player3_character)
    print '%s\'s character is %s.' % (player4_name, player4_character)


elif players_amount == 6:

    character_list = ['Merlin', 'Percival', 'Loyalist1', 'Loyalist2', 'Morgana', 'Assassin']

    host_character = choice(character_list)
    character_list.remove(host_character)
    
    player1_character = choice(character_list)
    character_list.remove(player1_character)

    player2_character = choice(character_list)
    character_list.remove(player2_character)

    player3_character = choice(character_list)
    character_list.remove(player3_character)

    player4_character = choice(character_list)
    character_list.remove(player4_character)

    player5_character = choice(character_list)

    print '%s\'s character is %s.' % (host_name, host_character)
    print '%s\'s character is %s.' % (player1_name, player1_character)
    print '%s\'s character is %s.' % (player2_name, player2_character)
    print '%s\'s character is %s.' % (player3_name, player3_character)
    print '%s\'s character is %s.' % (player4_name, player4_character)
    print '%s\'s character is %s.' % (player5_name, player5_character)

elif players_amount == 7:

    character_list = ['Merlin', 'Percival', 'Loyalist1', 'Loyalist2', 'Morgana', 'Oberon', 'Assassin']

    host_character = choice(character_list)
    character_list.remove(host_character)
    
    player1_character = choice(character_list)
    character_list.remove(player1_character)

    player2_character = choice(character_list)
    character_list.remove(player2_character)

    player3_character = choice(character_list)
    character_list.remove(player3_character)

    player4_character = choice(character_list)
    character_list.remove(player4_character)

    player5_character = choice(character_list)
    character_list.remove(player5_character)

    player6_character = choice(character_list)

    print '%s\'s character is %s.' % (host_name, host_character)
    print '%s\'s character is %s.' % (player1_name, player1_character)
    print '%s\'s character is %s.' % (player2_name, player2_character)
    print '%s\'s character is %s.' % (player3_name, player3_character)
    print '%s\'s character is %s.' % (player4_name, player4_character)
    print '%s\'s character is %s.' % (player5_name, player5_character)
    print '%s\'s character is %s.' % (player6_name, player6_character)
    

elif players_amount == 8:

    character_list = ['Merlin', 'Percival', 'Loyalist1', 'Loyalist2', 'Loyalist3', 'Morgana', 'Assassin', 'Minion']

    host_character = choice(character_list)
    character_list.remove(host_character)
    
    player1_character = choice(character_list)
    character_list.remove(player1_character)

    player2_character = choice(character_list)
    character_list.remove(player2_character)

    player3_character = choice(character_list)
    character_list.remove(player3_character)

    player4_character = choice(character_list)
    character_list.remove(player4_character)

    player5_character = choice(character_list)
    character_list.remove(player5_character)

    player6_character = choice(character_list)
    character_list.remove(player6_character)

    player7_character = choice(character_list)

    print '%s\'s character is %s.' % (host_name, host_character)
    print '%s\'s character is %s.' % (player1_name, player1_character)
    print '%s\'s character is %s.' % (player2_name, player2_character)
    print '%s\'s character is %s.' % (player3_name, player3_character)
    print '%s\'s character is %s.' % (player4_name, player4_character)
    print '%s\'s character is %s.' % (player5_name, player5_character)
    print '%s\'s character is %s.' % (player6_name, player6_character)
    print '%s\'s character is %s.' % (player7_name, player7_character)
    

elif players_amount == 9:

    character_list= ['Merlin', 'Percival', 'Loyalist1', 'Loyalist2', 'Loyalist3', 'Loyalist4', 'Mordred', 'Morgana', 'Assassin']

    host_character = choice(character_list)
    character_list.remove(host_character)
    
    player1_character = choice(character_list)
    character_list.remove(player1_character)

    player2_character = choice(character_list)
    character_list.remove(player2_character)

    player3_character = choice(character_list)
    character_list.remove(player3_character)

    player4_character = choice(character_list)
    character_list.remove(player4_character)

    player5_character = choice(character_list)
    character_list.remove(player5_character)

    player6_character = choice(character_list)
    character_list.remove(player6_character)

    player7_character = choice(character_list)
    character_list.remove(player7_character)

    player8_character = choice(character_list)

    print '%s\'s character is %s.' % (host_name, host_character)
    print '%s\'s character is %s.' % (player1_name, player1_character)
    print '%s\'s character is %s.' % (player2_name, player2_character)
    print '%s\'s character is %s.' % (player3_name, player3_character)
    print '%s\'s character is %s.' % (player4_name, player4_character)
    print '%s\'s character is %s.' % (player5_name, player5_character)
    print '%s\'s character is %s.' % (player6_name, player6_character)
    print '%s\'s character is %s.' % (player7_name, player7_character)
    print '%s\'s character is %s.' % (player8_name, player8_character)
    

elif players_amount == 10:

    character_list = ['Merlin', 'Percival', 'Loyalist1', 'Loyalist2', 'Loyalist3', 'Loyalist4', 'Morgana', 'Mordred', 'Minion', 'Assassin']

    host_character = choice(character_list)
    character_list.remove(host_character)
    
    player1_character = choice(character_list)
    character_list.remove(player1_character)

    player2_character = choice(character_list)
    character_list.remove(player2_character)

    player3_character = choice(character_list)
    character_list.remove(player3_character)

    player4_character = choice(character_list)
    character_list.remove(player4_character)

    player5_character = choice(character_list)
    character_list.remove(player5_character)

    player6_character = choice(character_list)
    character_list.remove(player6_character)

    player7_character = choice(character_list)
    character_list.remove(player7_character)

    player8_character = choice(character_list)
    character_list.remove(player8_character)

    player9_character = choice(character_list)

    print '%s\'s character is %s.' % (host_name, host_character)
    print '%s\'s character is %s.' % (player1_name, player1_character)
    print '%s\'s character is %s.' % (player2_name, player2_character)
    print '%s\'s character is %s.' % (player3_name, player3_character)
    print '%s\'s character is %s.' % (player4_name, player4_character)
    print '%s\'s character is %s.' % (player5_name, player5_character)
    print '%s\'s character is %s.' % (player6_name, player6_character)
    print '%s\'s character is %s.' % (player7_name, player7_character)
    print '%s\'s character is %s.' % (player8_name, player8_character)
    print '%s\'s character is %s.' % (player9_name, player9_character)