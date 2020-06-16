import janken2

print("じゃんけんを始めます")
player_name = input("名前を入れてください:")
player_hand = input("数字を入力してください　0:グー　1：チョキ　2：パー:")
hand = ["グー","チョキ","パー"]

if int(player_hand) < 0 or 2 < int(player_hand):
    while int(player_hand) < 0 or 2 < int(player_hand):
        print("範囲外です")
        player_hand = input("数字を入力してください　0:グー　1：チョキ　2：パー:")

print(player_name+"さんの手は"+hand[int(player_hand)]+"です")

janken2.janken(player_name,player_hand)
