# -*- coding:utf-8 -*-
from sys import exit
# 定义回合输赢

win = 0
lose = 0

# 定义队长投票

def Captain_Vote():
    global captain_vote_up
    global captain_vote_down

    captain_vote_up = 0
    captain_vote_down = 0
    # 队长投票
    host_vote1 = raw_input('Please vote ,y/n >>> ')
    if host_vote1 == 'y':
        captain_vote_up += 1
    elif host_vote1 == 'n':
        captain_vote_down -= 1
    elif host_vote1 == '':
        pass
    else:
        print "Please enter y or n."

    player1_vote1 = raw_input('Please vote ,y/n >>> ')
    if player1_vote1 == 'y':
        captain_vote_up += 1
    elif player1_vote1 == 'n':
        captain_vote_down -= 1
    elif player1_vote1 == '':
        pass
    else:
        print "Please enter y or n."

    player2_vote1= raw_input('Please vote ,y/n >>> ')
    if player2_vote1 == 'y':
        captain_vote_up += 1
    elif player2_vote1 == 'n':
        captain_vote_down -= 1
    elif player2_vote1 == '':
        pass
    else:
        print "Please enter y or n."

    player3_vote1 = raw_input('Please vote ,y/n >>> ')
    if player3_vote1 == 'y':
        captain_vote_up += 1
    elif player3_vote1 == 'n':
        captain_vote_down -= 1
    elif player3_vote1 == '':
        pass
    else:
        print "Please enter y or n."

    player4_vote1 = raw_input('Please vote ,y/n >>> ')
    if player4_vote1 == 'y':
        captain_vote_up += 1
    elif player4_vote1 == 'n':
        captain_vote_down -= 1
    elif player4_vote1 == '':
        pass
    else:
        print "Please enter y or n."

    player5_vote1 = raw_input('Please vote ,y/n >>> ')
    if player5_vote1 == 'y':
        captain_vote_up += 1
    elif player5_vote1 == 'n':
        captain_vote_down -= 1
    elif player5_vote1 == '':
        pass
    else:
        print "Please enter y or n."

    player6_vote1 = raw_input('Please vote ,y/n >>> ')
    if player6_vote1 == 'y':
        captain_vote_up += 1
    elif player6_vote1 == 'n':
        captain_vote_down -= 1
    elif player6_vote1 == '':
        pass
    else:
        print "Please enter y or n."

    player7_vote1 = raw_input('Please vote ,y/n >>> ')
    if player7_vote1 == 'y':
        captain_vote_up += 1
    elif player7_vote1 == 'n':
        captain_vote_down -= 1
    elif player7_vote1 == '':
        pass
    else:
        print "Please enter y or n."

    player8_vote1= raw_input('Please vote ,y/n >>> ')
    if player8_vote1 == 'y':
        captain_vote_up += 1
    elif player8_vote1 == 'n':
        captain_vote_down -= 1
    elif player8_vote1 == '':
        pass
    else:
        print "Please enter y or n."

    player9_vote1 = raw_input('Please vote ,y/n >>> ')
    if player9_vote1 == 'y':
        captain_vote_up += 1
    elif player9_vote1 == 'n':
        captain_vote_down -= 1
    elif player9_vote1 == '':
        pass
    else:
        print "Please enter y or n."

# 定义任务投票

def Task_Vote():
    global task_vote_up
    global task_vote_down

    task_vote_up = 0
    task_vote_down = 0
    # 队长投票
    host_vote2 = raw_input('Please vote ,y/n >>> ')
    if host_vote2 == 'y':
        task_vote_up += 1
    elif host_vote2 == 'n':
        task_vote_down -= 1
    elif host_vote2 == '':
        pass
    else:
        print "Please enter y or n."

    player1_vote2 = raw_input('Please vote ,y/n >>> ')
    if player1_vote2 == 'y':
        task_vote_up += 1
    elif player1_vote2 == 'n':
        task_vote_down -= 1
    elif player1_vote2 == '':
        pass
    else:
        print "Please enter y or n."

    player2_vote2= raw_input('Please vote ,y/n >>> ')
    if player2_vote2 == 'y':
        task_vote_up += 1
    elif player2_vote2 == 'n':
        task_vote_down -= 1
    elif player2_vote2 == '':
        pass
    else:
        print "Please enter y or n."

    player3_vote2 = raw_input('Please vote ,y/n >>> ')
    if player3_vote2 == 'y':
        task_vote_up += 1
    elif player3_vote2 == 'n':
        task_vote_down -= 1
    elif player3_vote2 == '':
        pass
    else:
        print "Please enter y or n."

    player4_vote2 = raw_input('Please vote ,y/n >>> ')
    if player4_vote2 == 'y':
        task_vote_up += 1
    elif player4_vote2 == 'n':
        task_vote_down -= 1
    elif player4_vote2 == '':
        pass    
    else:
        print "Please enter y or n."

    player5_vote2 = raw_input('Please vote ,y/n >>> ')
    if player5_vote2 == 'y':
        task_vote_up += 1
    elif player5_vote2 == 'n':
        task_vote_down -= 1
    elif player5_vote2 == '':
        pass
    else:
        print "Please enter y or n."

    player6_vote2 = raw_input('Please vote ,y/n >>> ')
    if player6_vote2 == 'y':
        task_vote_up += 1
    elif player6_vote2 == 'n':
        task_vote_down -= 1
    elif player6_vote2 == '':
        pass
    else:
        print "Please enter y or n."

    player7_vote2 = raw_input('Please vote ,y/n >>> ')
    if player7_vote2 == 'y':
        task_vote_up += 1
    elif player7_vote2 == 'n':
        task_vote_down -= 1
    elif player7_vote2 == '':
        pass
    else:
        print "Please enter y or n."

    player8_vote2= raw_input('Please vote ,y/n >>> ')
    if player8_vote2 == 'y':
        task_vote_up += 1
    elif player8_vote2 == 'n':
        task_vote_down -= 1
    elif player8_vote2 == '':
        pass
    else:
        print "Please enter y or n."

    player9_vote2 = raw_input('Please vote ,y/n >>> ')
    if player9_vote2 == 'y':
        task_vote_up += 1
    elif player9_vote2 == 'n':
        task_vote_down -= 1
    elif player9_vote2 == '':
        pass
    else:
        print "Please enter y or n."

# 正式开始，队长投票（最多5次），然后进行任务投票

Captain_Vote_Times = 0

Captain_Vote()

    # 队长投票结果验证
if captain_vote_up + captain_vote_down > 0:
    print "Succeed！"
    print "Up vote is %s " % captain_vote_up
    print "Down vote is %s " % captain_vote_down
    Task_Vote()

elif captain_vote_up + captain_vote_down <= 0:
    Captain_Vote_Times += 1
    print "Lose! "
    print "Up vote is %s " % captain_vote_up
    print "Down vote is %s " % captain_vote_down
    Captain_Vote()
    Captain_Vote_Times += 1

    if Captain_Vote_Times = 6
        print "Arthur's team loses！"
        exit()

while (win < 3 and lose < 3):
    Task_Vote()