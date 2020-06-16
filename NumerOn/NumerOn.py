import NumerOn2

print("NumerOnを始める場合は関数 NumerOn()を呼び出してください。")
def NumerOn():
    print("NumerOnを始めます。\nコンピューターが生成した異なる三桁の数字を10回以内に当ててください。")
    print("3Eatにするとあなたの勝利です。")
    print("\n用語説明\nBite:三桁の中に数字はあるが,場所があっていない\nEat:数字と場所があっている\n")
    
    Eat_count = 0
    Bite_count = 0
    wrong = 0
    computer_list = NumerOn2.computer_list()

    while wrong < 10:
        player_list = input("三桁の数字を入力しください：")
        player_list = NumerOn2.player_list(player_list)
        Eat_count = NumerOn2.Match_Eat(computer_list,player_list)
        Bite_count = NumerOn2.Match_Bite(computer_list,player_list)
        print(str(Bite_count)+"Bite "+str(Eat_count)+"Eat!")

        if Eat_count == 3:
            break
        else:
            wrong += 1

    if wrong == 10:
        print("あなたの負けです。")
        print("正解は "+"".join(computer_list)+" です")
    else:
        print("あなたの勝ちです。")
        print("正解は "+"".join(computer_list)+" です")
