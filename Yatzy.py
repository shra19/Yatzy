import random
from collections import namedtuple
final =[]

    #The scoring pad is to be implemented with a dictionary containing each category and a score associated to the category.
scoring_pad = {"Ones":0 , "Twoes":0 , "Threes":0 , "Fours":0, "Fives":0,"Sixes":0, "Pair":0, "Two Pairs":0, "Three of a kind":0,
                "Four of a kind":0,"Small straight":0,"Large straight":0, "Full house":0, "Chance":0, "Yatzy":0 }
    #The player is to be implemented using a named tuple containing the player’s name, scoring pad, and the five dice they are to use.

Player = namedtuple('Player', ['player_name', 'player_scoring_pad', 'player_dice'])
player_spec = Player([], [], [])

def roll(dice_num):
    count = 1
    while count <= dice_num:
        num = random.randint(1, 6)
        yield num
        count += 1

def Ones(final_list):
    return(final_list.count(1))

def Twoes(final_list):
    return(final_list.count(2)*2)

def Threes(final_list):
    return(final_list.count(3)*3)

def Fours(final_list):
    return(final_list.count(4)*4)

def Fives(final_list):
    return(final_list.count(5)*5)

def Sixes(final_list):
    return(final_list.count(6)*6)

def Pair(final_list):
    slection_num = []
    score = 0
    for each_dice in range(1,7):
        num = final_list.count(each_dice)
        if num >= 2:
            slection_num.append(each_dice)
            print(f"slection_num{slection_num}")
            pair_dice = max(slection_num)
            print(f"maximum selecting{pair_dice}")
            score = pair_dice * 2
            print(f"final_score in Pair{score}")
    return(score)
        
def Two_pair(final_list):
    slection_num = []
    score = 0
    for each_dice in range(1,7):
        num = final_list.count(each_dice)
        if num >= 2:
            slection_num.append(each_dice)
            print(f"slection_num{slection_num}")
            if len(slection_num) == 2:
                score = sum(slection_num) * 2 
                print(f"final_score in Pair{score}")
    return(score)
        
def Three_of_kind(final_list):
    slection_num = []
    score = 0
    for each_dice in range(1,7):
        num = final_list.count(each_dice)
        if num >= 3:
            slection_num.append(each_dice)
            print(f"slection_num{slection_num}")
            score = sum(slection_num) * 3  # lambda
            print(f"final_score in Pair{score}")
    return(score)           

def Four_of_kind(final_list):
    slection_num = []
    score = 0
    for each_dice in range(1,7):
        num = final_list.count(each_dice)
        if num >= 4:
            slection_num.append(each_dice)
            print(f"slection_num{slection_num}")
            score = sum(slection_num) * 4  
            print(f"final_score in Pair{score}")
    return(score) 

def Small_straight(final_list):
    score = 0
    final_list.sort()
    if final_list == [1,2,3,4,5]:
        score = 15
    return(score)   

def Large_straight(final_list):
    score = 0
    final_list.sort()
    if final_list == [2,3,4,5,6]:
        score = 20
    return(score)

def Full_house(final_list):
    slection_num1 = []
    score = 0
    score1 = 0
    for each_dice1 in range(1,7):
        num1 = final_list.count(each_dice1)
        if num1 == 3:
            slection_num1.append(each_dice1)
            final_list.remove(each_dice1)
            final_list.remove(each_dice1)
            final_list.remove(each_dice1)
            score1 = each_dice1 * 3  
    for each_dice2 in range(1,7):
            num2 = final_list.count(each_dice2)
            if num2 == 2:
                score2 = each_dice2 * 2
                if score1 != 0:
                    score = score1 + score2
    return(score)

def Chance(final_list):
    return(sum(final_list))

def Yatzy(final_list):
    score = 0
    for each_dice in range(1,7):
        num = final_list.count(each_dice)
        if num == 5:
            score = 50 
    return(score)

def main():
    while True: #get input until start
        
        user_name = input("player name is:") #Players are added through input by the user until a user input ‘start’
        player_spec.player_name.append(user_name)
        player_spec.player_scoring_pad.append(scoring_pad)
        player_spec.player_dice.append(list())
        print(player_spec.player_dice)

        answer = input("for starting a game please type>> start /or/ to add a new player press >> Enter:")
        if answer == "start":
            break
        
    random.shuffle(player_spec.player_name) #The order of the players is shuffled
    print(player_spec.player_name)
    
    game_step = 1
    while True:#game step
        player_number = 0

        while True: #player turn
            name = player_spec.player_name[player_number]

            print(" *******************************************************************")
            print(f"                      Turn:{name}                                  ")
            print(" *******************************************************************")
           

            roll_round = 1
            dice_number = 5
            final_list = []

            dices = roll(dice_number)
            
            # player_spec.player_dice.clear()
            player_spec.player_dice[player_number].clear()
            for i in range(dice_number):
                #print(player_number)
                player_spec.player_dice[player_number].append(next(dices))
                   
            print(f"Round{roll_round}:", player_spec.player_dice)
            while True:
                answer = input("Please roll dices with ENTER or keep.Type>(ENTER/keep):")
                if answer == "":
                    dices = roll(dice_number)
                    player_spec.player_dice[player_number].clear()
                    for i in range(dice_number):
                        player_spec.player_dice[player_number].append(next(dices))

                    roll_round += 1
                    print(f"Round{roll_round}:", player_spec.player_dice)
                elif answer ==  "keep":
                    number = input("please enter the number:")
                    player_spec.player_dice[player_number].remove(int(number))
                    final_list.append(int(number))
                    print("Player choices list:", final_list)
                    dice_number -= 1
                    print(player_spec.player_dice[player_number])

                if dice_number == 0:
                    final_list += player_spec.player_dice[player_number]
                    print("dice,Final player choices list:", final_list)
                    player_spec.player_dice[player_number].clear()
                    player_number +=1
                    break    
                if roll_round == 3:
                    final_list += player_spec.player_dice[player_number]
                    print("dice,Final player choices list:", final_list)
                    player_spec.player_dice[player_number].clear()
                    player_number +=1
                    break


            score_each_sequence(final_list, player_number-1, game_step)

            if player_number-1 == len(player_spec.player_name)-1: #? == 1
                game_step += 1
                break

        if game_step == 16:
            break

def score_each_sequence(final_list, player_num, game_step):    
    if game_step == 1:
        score1 = Ones(final_list)
        flag = dict(player_spec.player_scoring_pad[player_num])
        flag['Ones'] = score1
        player_spec.player_scoring_pad[player_num] = flag
        print(player_spec.player_scoring_pad[player_num])
        
        print(" -------------------------------------------------------------------")
        print(f"                       step Ones>>{player_spec.player_name[player_num]} Score is:{score1}                   ")
        print(" -------------------------------------------------------------------")

    elif game_step == 2:
        score2 = Twoes(final_list)
        flag = dict(player_spec.player_scoring_pad[player_num])
        flag['Twoes'] = score2
        player_spec.player_scoring_pad[player_num] = flag
        print(player_spec.player_scoring_pad[player_num])
        print(" -------------------------------------------------------------------")
        print(f"                       step Twoes>>{player_spec.player_name[player_num]} Score is:{score2}                  ")
        print(" -------------------------------------------------------------------")

    elif game_step == 3:
        score3 = Threes(final_list)
        flag = dict(player_spec.player_scoring_pad[player_num])
        flag['Threes'] = score3
        player_spec.player_scoring_pad[player_num] = flag
        print(player_spec.player_scoring_pad[player_num])
        print(" ------------------------------------------------------")
        print(f"                  step Threes>>{player_spec.player_name[player_num]} Score is:{score3}                      ")
        print(" ------------------------------------------------------")

    elif game_step == 4:
        score4 = Fours(final_list)
        flag = dict(player_spec.player_scoring_pad[player_num])
        flag['Fours'] = score4
        player_spec.player_scoring_pad[player_num] = flag
        print(player_spec.player_scoring_pad[player_num])
        print(" ------------------------------------------------------")
        print(f"                   step Fours>>{player_spec.player_name[player_num]} Score is:{score4}                       ")
        print(" ------------------------------------------------------")

    elif game_step == 5:
        score5 = Fives(final_list)
        flag = dict(player_spec.player_scoring_pad[player_num])
        flag['Fives'] = score5
        player_spec.player_scoring_pad[player_num] = flag
        print(player_spec.player_scoring_pad[player_num])
        print(" ------------------------------------------------------")
        print(f"                 step Fives>>{player_spec.player_name[player_num]} Score is:{score5}                        ")
        print(" ------------------------------------------------------")

    elif game_step == 6:
        score6 = Sixes(final_list)
        flag = dict(player_spec.player_scoring_pad[player_num])
        flag['Sixes'] = score6
        player_spec.player_scoring_pad[player_num] = flag
        print(player_spec.player_scoring_pad[player_num])
        print(" ------------------------------------------------------")
        print(f"                  step Sixes>>{player_spec.player_name[player_num]} Score is:{score6}                        ")
        print(" ------------------------------------------------------")
    
    elif game_step == 7:
        score7 = Pair(final_list)
        flag = dict(player_spec.player_scoring_pad[player_num])
        flag['Pair'] = score7
        player_spec.player_scoring_pad[player_num] = flag
        print(player_spec.player_scoring_pad[player_num])
        print(" ------------------------------------------------------")
        print(f"              Step Pair>>{player_spec.player_name[player_num]} Score is:{score7}                              ")
        print(" ------------------------------------------------------")
    
    elif game_step == 8:
        score8 = Two_pair(final_list)
        flag = dict(player_spec.player_scoring_pad[player_num])
        flag['Two Pairs'] = score8
        player_spec.player_scoring_pad[player_num] = flag
        print(player_spec.player_scoring_pad[player_num])
        print(" ------------------------------------------------------")
        print(f"               Step Two Pairs>>{player_spec.player_name[player_num]} Score is:{score8}                        ")
        print(" ------------------------------------------------------")
    
    elif game_step == 9:
        score9 = Three_of_kind(final_list)
        flag = dict(player_spec.player_scoring_pad[player_num])
        flag['Three of a kind'] = score9
        player_spec.player_scoring_pad[player_num] = flag
        print(player_spec.player_scoring_pad[player_num])
        print(" ------------------------------------------------------")
        print(f"             Three of a kind>>{player_spec.player_name[player_num]} Score is:{score9}                        ")
        print(" ------------------------------------------------------")

    elif game_step == 10:
        score10 = Four_of_kind(final_list)
        flag = dict(player_spec.player_scoring_pad[player_num])
        flag['Four of a kind'] = score10
        player_spec.player_scoring_pad[player_num] = flag
        print(player_spec.player_scoring_pad[player_num])
        print(" ------------------------------------------------------")
        print(f"             Four of a kind>>{player_spec.player_name[player_num]} Score is:{score10}                       ")
        print(" ------------------------------------------------------")

    elif game_step == 11:
        score11 = Small_straight(final_list)
        flag = dict(player_spec.player_scoring_pad[player_num])
        flag['Small straight'] = score11
        player_spec.player_scoring_pad[player_num] = flag
        print(player_spec.player_scoring_pad[player_num])
        print(" ------------------------------------------------------")
        print(f"              small straight>>{player_spec.player_name[player_num]} Score is:{score11}                       ")
        print(" ------------------------------------------------------")

    elif game_step == 12:
        score12 = Large_straight(final_list)
        flag = dict(player_spec.player_scoring_pad[player_num])
        flag['Three of a kind'] = score12
        player_spec.player_scoring_pad[player_num] = flag
        print(player_spec.player_scoring_pad[player_num])
        print(" ------------------------------------------------------")
        print(f"               Large straight>>{player_spec.player_name[player_num]} Score is:{score12}                       ")
        print(" ------------------------------------------------------")

    elif game_step == 13:
        score13 = Full_house(final_list)
        flag = dict(player_spec.player_scoring_pad[player_num])
        flag['Full house'] = score13
        # print(flag)
        player_spec.player_scoring_pad[player_num] = flag
        print(player_spec.player_scoring_pad[player_num])
        print(" ------------------------------------------------------")
        print(f"             Full house>>{player_spec.player_name[player_num]} Score is:{score13}                               ")
        print(" ------------------------------------------------------")

    elif game_step == 14:
        score14 = Chance(final_list)
        flag = dict(player_spec.player_scoring_pad[player_num])
        flag['Chance'] = score14
        player_spec.player_scoring_pad[player_num] = flag
        print(player_spec.player_scoring_pad[player_num])
        print(" ------------------------------------------------------")
        print(f"               chance{player_spec.player_name[player_num]} Score is:{score14}                                ")
        print(" ------------------------------------------------------")

    elif game_step == 15:
        score15 = Yatzy(final_list)
        flag = dict(player_spec.player_scoring_pad[player_num])
        flag['Yatzy'] = score15
        player_spec.player_scoring_pad[player_num] = flag
        print(player_spec.player_scoring_pad[player_num])
        print(" ------------------------------------------------------")
        print(f"              Yatzy{player_spec.player_name[player_num]} Score is:{score15}                                ")
        print(" ------------------------------------------------------")    

main()

finall_list_score = []
for each_user in range(len(player_spec.player_name)):
    [user_name, user_score] = [player_spec.player_name[each_user], sum(player_spec.player_scoring_pad[each_user].values())]
    finall_list_score.append([user_name, user_score])

    def sortSecond(val): 
        return val[1]
    finall_list_score.sort(key = sortSecond, reverse = True)
    
for member in range(len(finall_list_score)): 
    print(f"{finall_list_score[member][0]} final score is {finall_list_score[member][1]}")
    if  member == 0:
        print(f"{finall_list_score[member][0]}<<< is Winner >>>")
    elif finall_list_score[0][1] == finall_list_score[1][1]:
        print(f"{finall_list_score[0][0]} and {finall_list_score[1][0]} <<< is Winner >>>")
        

print("\ntest finished")

