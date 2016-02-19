# -*- coding:utf-8 -*-

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
    else:
        print "Please enter y or n."

    player1_vote1 = raw_input('Please vote ,y/n >>> ')
    if player1_vote1 == 'y':
        captain_vote_up += 1
    elif player1_vote1 == 'n':
        captain_vote_down -= 1
    else:
        print "Please enter y or n."

    player2_vote1= raw_input('Please vote ,y/n >>> ')
    if player2_vote1 == 'y':
        captain_vote_up += 1
    elif player2_vote1 == 'n':
        captain_vote_down -= 1
    else:
        print "Please enter y or n."

    player3_vote1 = raw_input('Please vote ,y/n >>> ')
    if player3_vote1 == 'y':
        captain_vote_up += 1
    elif host_vote1 == 'n':
        captain_vote_down -= 1
    else:
        print "Please enter y or n."

    player4_vote1 = raw_input('Please vote ,y/n >>> ')
    if player4_vote1 == 'y':
        captain_vote_up += 1
    elif player4_vote1 == 'n':
        captain_vote_down -= 1
    else:
        print "Please enter y or n."

    player5_vote1 = raw_input('Please vote ,y/n >>> ')
    if player5_vote1 == 'y':
        captain_vote_up += 1
    elif player5_vote1 == 'n':
        captain_vote_down -= 1
    else:
        print "Please enter y or n."

    player6_vote1 = raw_input('Please vote ,y/n >>> ')
    if player6_vote1 == 'y':
        captain_vote_up += 1
    elif player6_vote1 == 'n':
        captain_vote_down -= 1
    else:
        print "Please enter y or n."

    player7_vote1 = raw_input('Please vote ,y/n >>> ')
    if player7_vote1 == 'y':
        captain_vote_up += 1
    elif player7_vote1 == 'n':
        captain_vote_down -= 1
    else:
        print "Please enter y or n."

    player8_vote1= raw_input('Please vote ,y/n >>> ')
    if player8_vote1 == 'y':
        captain_vote_up += 1
    elif player8_vote1 == 'n':
        captain_vote_down -= 1
    else:
        print "Please enter y or n."

    player9_vote1 = raw_input('Please vote ,y/n >>> ')
    if player9_vote1 == 'y':
        captain_vote_up += 1
    elif player9_vote1 == 'n':
        captain_vote_down -= 1
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
    else:
        print "Please enter y or n."

    player1_vote2 = raw_input('Please vote ,y/n >>> ')
    if player1_vote2 == 'y':
        task_vote_up += 1
    elif player1_vote2 == 'n':
        task_vote_down -= 1
    else:
        print "Please enter y or n."

    player2_vote2= raw_input('Please vote ,y/n >>> ')
    if player2_vote2 == 'y':
        task_vote_up += 1
    elif player2_vote2 == 'n':
        task_vote_down -= 1
    else:
        print "Please enter y or n."

    player3_vote2 = raw_input('Please vote ,y/n >>> ')
    if player3_vote2 == 'y':
        task_vote_up += 1
    elif host_vote2 == 'n':
        task_vote_down -= 1
    else:
        print "Please enter y or n."

    player4_vote2 = raw_input('Please vote ,y/n >>> ')
    if player4_vote2 == 'y':
        task_vote_up += 1
    elif player4_vote2 == 'n':
        task_vote_down -= 1
    else:
        print "Please enter y or n."

    player5_vote2 = raw_input('Please vote ,y/n >>> ')
    if player5_vote2 == 'y':
        task_vote_up += 1
    elif player5_vote2 == 'n':
        task_vote_down -= 1
    else:
        print "Please enter y or n."

    player6_vote2 = raw_input('Please vote ,y/n >>> ')
    if player6_vote2 == 'y':
        task_vote_up += 1
    elif player6_vote2 == 'n':
        task_vote_down -= 1
    else:
        print "Please enter y or n."

    player7_vote2 = raw_input('Please vote ,y/n >>> ')
    if player7_vote2 == 'y':
        task_vote_up += 1
    elif player7_vote2 == 'n':
        task_vote_down -= 1
    else:
        print "Please enter y or n."

    player8_vote2= raw_input('Please vote ,y/n >>> ')
    if player8_vote2 == 'y':
        task_vote_up += 1
    elif player8_vote2 == 'n':
        task_vote_down -= 1
    else:
        print "Please enter y or n."

    player9_vote2 = raw_input('Please vote ,y/n >>> ')
    if player9_vote2 == 'y':
        task_vote_up += 1
    elif player9_vote2 == 'n':
        task_vote_down -= 1
    else:
        print "Please enter y or n."

Captain_Vote()

    # 队长投票结果验证
if captain_vote_up + captain_vote_down > 0:
    print "Succeeded！"
    print "Up vote is %s " % captain_vote_up
    print "Down vote is %s " % captain_vote_down

else:
    print "Lose! "
    print "Up vote is %s " % captain_vote_up
    print "Down vote is %s " % captain_vote_down
    Captain_Vote()