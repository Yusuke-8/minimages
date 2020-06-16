import random

def computer_list():
# 各要素の数字がそれぞれ重ならないようにする関数
    number = []
    element_1 = random.randint(0,9)
    element_2 = random.randint(0,9)
    element_3 = random.randint(0,9)

    number.append(str(element_1))

    if element_1 == element_2:
        while element_1 == element_2:
            element_2 = random.randint(0,9)
        number.append(str(element_2))
    else:
        number.append(str(element_2))

    if element_1 == element_3 or element_2 == element_3:
        while element_1 == element_3 or element_2 == element_3:
            element_3 = random.randint(0,9)
        number.append(str(element_3))
    else:
        number.append(str(element_3))

    return number


def player_list(input_number):
# プレイヤーの入力した数字をリスト化する関数
    number = []
    for i_index in range(0,len(input_number)):
        number.append(input_number[i_index])
    return number

def Match_Eat(computer_list,player_list):
# 場所と数字があっている場合のカウントを返す関数
    count = 0
    for i_index in range(0,len(player_list)):
        if player_list[i_index] == computer_list[i_index]:
            count += 1
    return count

def Match_Bite(computer_list,player_list):
# 数字があることを数える関数
    count = 0
    for i_index in range(0,len(player_list)):
        for j_index in range(0,len(player_list)):
            if player_list[i_index] == computer_list[j_index]:
                count += 1
    for i_index in range(0,len(player_list)):
        if player_list[i_index] == computer_list[i_index]:
            count -= 1
    return count
