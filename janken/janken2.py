import random

def janken(name,number):
    hand = ["グー","チョキ","パー"]
    computer_hand = random.randint(0,2)
    if int(number) == computer_hand:
        print("コンピューターの手は"+hand[int(computer_hand)]+"です")
        print("引き分け")
        number = int(input("もう一度、数字を入力してください　0:グー　1：チョキ　2：パー:"))
        if number < 0 or 2 < number:
            while number < 0 or 2 < number:
                print("範囲外です")
                number = int(input("数字を入力してください　0:グー　1：チョキ　2：パー:"))
        print(name+"さんの手は"+hand[number]+"です")
        janken(name,number)

    elif int(number) == 0 and computer_hand == 1:
        print("コンピューターの手は"+hand[int(computer_hand)]+"です")
        print(name+"さんの勝ちです")
    elif int(number) == 1 and computer_hand == 2:
        print("コンピューターの手は"+hand[int(computer_hand)]+"です")
        print(name+"さんの勝ちです")
    elif int(number) == 2 and computer_hand == 0:
        print("コンピューターの手は"+hand[int(computer_hand)]+"です")
        print(name+"さんの勝ちです")
    else:
        print("コンピューターの手は"+hand[int(computer_hand)]+"です")
        print(name+"さんの負けです")
