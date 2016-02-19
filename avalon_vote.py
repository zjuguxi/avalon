# -*- coding:utf-8 -*-
from sys import exit
# 定义回合输赢

win = 0
lose = 0
Captain_Vote_Times = 0





# 最终胜负判断

def result():

    if (win < 3 and lose < 3):
        Captain_Vote()

    elif win == 3:
        print "***** Arthur's Team Finally wins!*****"
        exit()
    elif lose == 3:
        print "****** Mordred's Team Finally wins! *****"
    else:
        print "***** You found a bug! Report it to GuXi! *****"
        exit()





# 定义队长投票

def Captain_Vote():
    global captain_vote_up
    global captain_vote_down
    global Captain_Vote_Times
    global lose
    global win

    Captain_Vote_Times += 1

    captain_vote_up = 0
    captain_vote_down = 0
    # 队长投票
    host_vote1 = raw_input('Please vote ,y/n >>> ')
    if host_vote1 == 'y':
        captain_vote_up += 1
    elif host_vote1 == 'n':
        captain_vote_down += 1
    elif host_vote1 == '':
        pass
    else:
        print "Please enter y or n."

    player1_vote1 = raw_input('Please vote ,y/n >>> ')
    if player1_vote1 == 'y':
        captain_vote_up += 1
    elif player1_vote1 == 'n':
        captain_vote_down += 1
    elif player1_vote1 == '':
        pass
    else:
        print "Please enter y or n."

    player2_vote1= raw_input('Please vote ,y/n >>> ')
    if player2_vote1 == 'y':
        captain_vote_up += 1
    elif player2_vote1 == 'n':
        captain_vote_down += 1
    elif player2_vote1 == '':
        pass
    else:
        print "Please enter y or n."

    player3_vote1 = raw_input('Please vote ,y/n >>> ')
    if player3_vote1 == 'y':
        captain_vote_up += 1
    elif player3_vote1 == 'n':
        captain_vote_down += 1
    elif player3_vote1 == '':
        pass
    else:
        print "Please enter y or n."

    player4_vote1 = raw_input('Please vote ,y/n >>> ')
    if player4_vote1 == 'y':
        captain_vote_up += 1
    elif player4_vote1 == 'n':
        captain_vote_down += 1
    elif player4_vote1 == '':
        pass
    else:
        print "Please enter y or n."

    player5_vote1 = raw_input('Please vote ,y/n >>> ')
    if player5_vote1 == 'y':
        captain_vote_up += 1
    elif player5_vote1 == 'n':
        captain_vote_down += 1
    elif player5_vote1 == '':
        pass
    else:
        print "Please enter y or n."

    player6_vote1 = raw_input('Please vote ,y/n >>> ')
    if player6_vote1 == 'y':
        captain_vote_up += 1
    elif player6_vote1 == 'n':
        captain_vote_down += 1
    elif player6_vote1 == '':
        pass
    else:
        print "Please enter y or n."

    player7_vote1 = raw_input('Please vote ,y/n >>> ')
    if player7_vote1 == 'y':
        captain_vote_up += 1
    elif player7_vote1 == 'n':
        captain_vote_down += 1
    elif player7_vote1 == '':
        pass
    else:
        print "Please enter y or n."

    player8_vote1= raw_input('Please vote ,y/n >>> ')
    if player8_vote1 == 'y':
        captain_vote_up += 1
    elif player8_vote1 == 'n':
        captain_vote_down += 1
    elif player8_vote1 == '':
        pass
    else:
        print "Please enter y or n."

    player9_vote1 = raw_input('Please vote ,y/n >>> ')
    if player9_vote1 == 'y':
        captain_vote_up += 1
    elif player9_vote1 == 'n':
        captain_vote_down += 1
    elif player9_vote1 == '':
        pass
    else:
        print "Please enter y or n."

    if captain_vote_up - captain_vote_down > 0:
        print "Captain Vote Passed! "
        print "Up vote is %s " % captain_vote_up
        print "Down vote is %s " % captain_vote_down
        print "Now vote for the task."
        Task_Vote()
    else:
        if Captain_Vote_Times > 4:
            Captain_Vote_Times = 0
            print "Mordred's Team win!"
            print "Up vote is %s " % captain_vote_up
            print "Down vote is %s " % captain_vote_down
            lose += 1
            print "win = %s " % win
            print "lose = %s " % lose
            result()
        else:    
            print "Captain Vote didn't passed!"
            print "Up vote is %s " % captain_vote_up
            print "Down vote is %s " % captain_vote_down
            print "win = %s " % win
            print "lose = %s " % lose
            print "Now vote again."
            Captain_Vote()






# 定义任务投票

def Task_Vote():
    global task_vote_up, task_vote_down, win, lose, Captain_Vote_Times


    Captain_Vote_Times = 0
    task_vote_up = 0
    task_vote_down = 0
    # 队长投票
    host_vote2 = raw_input('Please vote for task, y/n >>> ')
    if host_vote2 == 'y':
        task_vote_up += 1
    elif host_vote2 == 'n':
        task_vote_down += 1
    elif host_vote2 == '':
        pass
    else:
        print "Please enter y or n."

    player1_vote2 = raw_input('Please vote for task, y/n >>> ')
    if player1_vote2 == 'y':
        task_vote_up += 1
    elif player1_vote2 == 'n':
        task_vote_down += 1
    elif player1_vote2 == '':
        pass
    else:
        print "Please enter y or n."

    player2_vote2= raw_input('Please vote for task, y/n >>> ')
    if player2_vote2 == 'y':
        task_vote_up += 1
    elif player2_vote2 == 'n':
        task_vote_down += 1
    elif player2_vote2 == '':
        pass
    else:
        print "Please enter y or n."

    player3_vote2 = raw_input('Please vote for task, y/n >>> ')
    if player3_vote2 == 'y':
        task_vote_up += 1
    elif player3_vote2 == 'n':
        task_vote_down += 1
    elif player3_vote2 == '':
        pass
    else:
        print "Please enter y or n."

    player4_vote2 = raw_input('Please vote for task, y/n >>> ')
    if player4_vote2 == 'y':
        task_vote_up += 1
    elif player4_vote2 == 'n':
        task_vote_down += 1
    elif player4_vote2 == '':
        pass    
    else:
        print "Please enter y or n."

    player5_vote2 = raw_input('Please vote for task, y/n >>> ')
    if player5_vote2 == 'y':
        task_vote_up += 1
    elif player5_vote2 == 'n':
        task_vote_down += 1
    elif player5_vote2 == '':
        pass
    else:
        print "Please enter y or n."

    player6_vote2 = raw_input('Please vote for task, y/n >>> ')
    if player6_vote2 == 'y':
        task_vote_up += 1
    elif player6_vote2 == 'n':
        task_vote_down += 1
    elif player6_vote2 == '':
        pass
    else:
        print "Please enter y or n."

    player7_vote2 = raw_input('Please vote for task, y/n >>> ')
    if player7_vote2 == 'y':
        task_vote_up += 1
    elif player7_vote2 == 'n':
        task_vote_down += 1
    elif player7_vote2 == '':
        pass
    else:
        print "Please enter y or n."

    player8_vote2= raw_input('Please vote for task, y/n >>> ')
    if player8_vote2 == 'y':
        task_vote_up += 1
    elif player8_vote2 == 'n':
        task_vote_down += 1
    elif player8_vote2 == '':
        pass
    else:
        print "Please enter y or n."

    player9_vote2 = raw_input('Please vote for task, y/n >>> ')
    if player9_vote2 == 'y':
        task_vote_up += 1
    elif player9_vote2 == 'n':
        task_vote_down += 1
    elif player9_vote2 == '':
        pass
    else:
        print "Please enter y or n."

    if  task_vote_up - task_vote_down > 0:
        print "Arthur's Team wins!"
        print "Up vote is %s." % task_vote_up
        print "Down vote is %s." % task_vote_down
        win += 1
    
    else:
        print "Mordred's Team wins!"
        print "Up vote is %s." % task_vote_up
        print "Down vote is %s." % task_vote_down
        lose += 1
        Captain_Vote_Times = 0

    print "win = %s " % win
    print "lose = %s " % lose
    result()



    

# 正式开始，队长投票（最多5次），然后进行任务投票

Captain_Vote()