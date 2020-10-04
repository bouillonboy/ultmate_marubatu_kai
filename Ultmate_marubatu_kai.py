"""アルティメットマルバツゲーム作成の流れ
1.マスを表すリストを用意する(今回は2重のリスト)
2.先行のプレイヤー(User0)の入力値(座標)を標準形で受け取る
3.user1の入力が可能か判断する(前回の入力に対応しているか?,まだ入力がされてない座標か?)
不可能ならエラーメッセージを表示する.
4.user1の入力をリストに追加する.また盤面の見た目も変える必要がある
5.記号が3つ並んでいるかの判断をする(エリアと盤面ともに判断する)
6.後行のプレイヤー(User1)の入力値(座標)を標準形で受け取る
7.user2の入力が可能か判断する(前回の入力に対応しているか?,まだ入力がされてない座標か?)
不可能ならエラーメッセージを表示する.
8.user2の入力をリストに追加する.また盤面の見た目も変える必要がある
9.記号が3つ並んでいるかの判断をする(エリアと盤面ともに判断する)
"""
"""
アルティメットエリアで揃ったら，その盤面は全てそのプレイヤーのきごうにする
"""

#勝利条件の判定をする関数(盤面で揃っているかどうかの判定)
def check_decision(coordinate_map):
    l123 = list(set([1, 2, 3]) & set(coordinate_map))
    l123.sort()
    if[1, 2, 3] == l123:
        return True
    l456 = list(set([4, 5, 6]) & set(coordinate_map))
    l456.sort()
    if[4, 5, 6] == l456:
        return True
    l789 = list(set([7, 8, 9]) & set(coordinate_map))
    l789.sort()
    if[7, 8, 9] == l789:
        return True
    l147 = list(set([1, 4, 7]) & set(coordinate_map))
    l147.sort()
    if[1, 4, 7] == l147:
        return True
    l258 = list(set([2, 5, 8]) & set(coordinate_map))
    l258.sort()
    if[2, 5, 8] == l258:
        return True
    l369 = list(set([3, 6, 9]) & set(coordinate_map))
    l369.sort()
    if[3, 6, 9] == l369:
        return True
    l159 = list(set([1, 5, 9]) & set(coordinate_map))
    l159.sort()
    if[1, 5, 9] == l159:
        return True
    l357 = list(set([3, 5, 7]) & set(coordinate_map))
    l357.sort()
    if[3, 5, 7] == l357:
        return True
    return False

def zyuunokurai(num):
    for i in range(10):
        if num >= 10:
            num -= 10
        else:
            return i

def kakikae0(zyuu):#エリアをとった時の盤面書き換え関数
    global banmen 
    if zyuu % 2 == 0: #ノーマルエリアの時
        area_name = rule_area[int(zyuu)]
        banmen = banmen.replace(area_name + "0"," o")
        return banmen
    else: #アルティメットエリアのとき
        area_name = rule_area[int(zyuu)]
        for i in range(1,10):
            banmen = banmen.replace(area_name + str(i)," o")
        return banmen

def kakikae1(zyuu):#エリアをとった時用の書き換え関数
    global banmen 
    if zyuu % 2 == 0: #ノーマルエリアの時
        area_name = rule_area[int(zyuu)]
        banmen = banmen.replace(area_name + "0"," x")
        return banmen
    else: #アルティメットエリアのとき
        area_name = rule_area[int(zyuu)]
        for i in range(1,10):
            banmen = banmen.replace(area_name + str(i)," x")
        return banmen

def kakikae0_list(zyuu,idx): #エリアをとった時のリスト書き換え用
    global banmen_map
    if zyuu % 2 == 0: #ノーマルエリアの時
        banmen_map[idx] = "o"
    else: #アルティメットエリアのとき zyuu = 1,3,5,7,9
        for i in range(9):
            if zyuu == 1:
                banmen_map[(zyuu-1) * 10 + i] =  "o"
            elif zyuu == 3:
                banmen_map[(zyuu-2) * 10 + i] = "o"
            elif zyuu == 5:
                banmen_map[(zyuu-3) * 10 + i] = "o"
            elif zyuu == 7:
                banmen_map[(zyuu-4) * 10 + i] = "o"
            elif zyuu == 9:
                banmen_map[(zyuu-5) * 10 + i] = "o"


def kakikae1_list(zyuu,idx): #エリアをとった時のリスト書き換え用
    global banmen_map
    if zyuu % 2 == 0: #ノーマルエリアの時
        banmen_map[idx] = "x"
    else: #アルティメットエリアのとき 
        for i in range(9):
            if zyuu == 1:
                banmen_map[(zyuu-1) * 10 + i] = "x"
            elif zyuu == 3:
                banmen_map[(zyuu-2) * 10 + i] = "x"
            elif zyuu == 5:
                banmen_map[(zyuu-3) * 10 + i] = "x"
            elif zyuu == 7:
                banmen_map[(zyuu-4) * 10 + i] = "x"
            elif zyuu == 9:
                banmen_map[(zyuu-5) * 10 + i] = "x"

def kakikae0_all():
    global banmen
    count = 0
    while count <= 49:
        for i in range(1,10):
            for j in range(1,10):
                banmen =  banmen.replace("x","o")
                area_name = rule_area[i]
                if i  in [2,4,6,8]:
                    banmen =  banmen.replace(area_name + "0", " o")
                    count += 1
                else:
                    banmen =  banmen.replace(area_name + str(j), " o")
                    count += 9
    return banmen

def kakikae1_all():
    global banmen
    count = 0
    while count <= 49:
        for i in range(1,10):
            for j in range(1,10):
                banmen =  banmen.replace("o","x")
                area_name = rule_area[i]
                if i  in [2,4,6,8]:
                    banmen =  banmen.replace(area_name + "0", " x")
                    count += 1
                else:
                    banmen =  banmen.replace(area_name + str(j), " x")
                    count += 9
    return banmen

def hikiwake(num):
    global user0_operations
    global user1_operations
    global hikiwake_list
    count = 0
    for i in range(1,10) :
        if rule_area[num] + str(i) not in banmen_map:
            count += 1
        if count == 9 and (num not in user0_operations) and (num not in user1_operations):
            hikiwake_list.append(num)
            break

banmen ="""
|A1|A2|A3|        |C1|C2|C3|
|--------|        |--------|
|A4|A5|A6|   B0   |C4|C5|C6|
|--------|        |--------|
|A7|A8|A9|        |C7|C8|C9|
----------------------------
|        |E1|E2|E3|        |
|        |--------|        |
|   D0   |E4|E5|E6|   F0   | 
|        |--------|        |
|        |E7|E8|E9|        | 
----------------------------
|G1|G2|G3|        |I1|I2|I3|
|--------|        |--------|
|G4|G5|G6|   H0   |I4|I5|I6|
|--------|        |--------|
|G7|G8|G9|        |I7|I8|I9|
"""

rule = {"A1":11,"A2":12,"A3":13,"A4":14,"A5":15,"A6":16,"A7":17,"A8":18,"A9":19,
        "B0":20,"C1":31,"C2":32,"C3":33,"C4":34,"C5":35,"C6":36,"C7":37,"C8":38,"C9":39,
        "D0":40,"E1":51,"E2":52,"E3":53,"E4":54,"E5":55,"E6":56,"E7":57,"E8":58,"E9":59,
        "F0":60,"G1":71,"G2":72,"G3":73,"G4":74,"G5":75,"G6":76,"G7":77,"G8":78,"G9":79,
        "H0":80,"I1":91,"I2":92,"I3":93,"I4":94,"I5":95,"I6":96,"I7":97,"I8":98,"I9":99}

rule_area = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",0:"A,C,E,G,Iの好きな場所"}

banmen_map = ["A1","A2","A3","A4","A5","A6","A7","A8","A9","B0",
            "C1","C2","C3","C4","C5","C6","C7","C8","C9","D0",
            "E1","E2","E3","E4","E5","E6","E7","E8","E9","F0",
            "G1","G2","G3","G4","G5","G6","G7","G8","G9","H0",
            "I1","I2","I3","I4","I5","I6","I7","I8","I9"]

user0_operations = [] #ユーザー0が盤面で見た時に獲得したマス
user1_operations = []
hikiwake_list = [] #引き分けしたエリア用のリスト

def ultmate_marubatu():
    rule_message ="""
    アルティメットマルバツゲームのルール
    ・基本は通常のマルバツゲームと同じ
    ・初手はEのエリアのどこかにおかなければならない
    ・アルファベットと数字が対応しており，プレイヤーは前回のプレイヤーがおいたマスの数字に
    対応するアルファベットのエリア内におかなければならない.
    対応表:1-A,2-B,3-C,4-D,5-E,6-F,7-G,8-H,9-I,0のときはアルティメットエリア(A,C,E,G,I)の好きなエリアを選択できる
    (例)前回のプレイヤーがA5においたら，このターンはEのどこかにおかなくてはならない
    ・また対応するエリアがすでに埋まっておりおけない場合はアルティメットエリア(A,C,E,G,I)の好きなエリアを選択しておける
    ・アルティメットエリアの中で通常のマルバツゲームの決着がついたら，そのエリアはその勝者のエリアになり，
    あるプレイヤーのエリアが盤面で３つ揃った時にそのプレイヤーの勝利となる．
    ・なおノーマルエリア(B,D,F,H)は一度おくだけでそのプレイヤーのエリアとなる
    """

    user0_input = str() #ユーザー0の入力値
    user1_input = str() #ユーザー１の入力値
    user0_operations_area = [[],[],[],[],[],[],[],[],[]] #ユーザー0の獲得したマス
    user1_operations_area = [[],[],[],[],[],[],[],[],[]] #ユーザー1の獲得したマス
    next_area_int = 5 #次のプレイヤーがおける座標
    next_area_str = rule_area[next_area_int]
    global user0_operations
    global user1_operations
    global hikiwake_list

    err_message = "正しい座標を入力してください"

    turn_user = 0
    turn_count = 0

    global banmen
    global banmen_map

    print(rule_message)
    print("先行のプレイヤーをUser0,後行のプレイヤーをUser1とします")
    print('ではゲームを開始します．以下の盤面の文字で座標を指定してください')
    print(banmen)

    while True:
        if turn_user == 0: #user0のターン
            try:
                mes0 = 'user0のターンです.このターンはエリア',next_area_str ,'に置くことができます.座標を入力してください:'
                user0_input = input(mes0)
            except: #ちゃんと入力されなかったとき
                print(err_message)
                continue
            if user0_input in banmen_map: #おける時 (指定した座標がまだ空いている時)
                num = rule[user0_input] #指定した座標の数値を取得 user_inoutは"A1"みたいなやつ,numは11みたいなやつ
                zyuu = zyuunokurai(num) #numの10の位を求める
                if  (zyuu == next_area_int) or (next_area_int == 0 and (zyuu == 1 or zyuu == 3 or zyuu == 5 or zyuu == 7 or zyuu == 9)): #ネクストエリアにちゃんとあってるか
                    idx = banmen_map.index(user0_input) #indexを取得
                    user0_operations_area[zyuu-1].append(num - (zyuu * 10)) #user0がとったエリアのますのリストに追加
                    if check_decision(user0_operations_area[zyuu-1]) or zyuu == 2 or zyuu == 4 or zyuu == 6 or zyuu == 8: #エリア内で揃ったかの判定
                        user0_operations.append(zyuu) #盤面でのとったマスのリストに追加
                        if check_decision(user0_operations): #盤面で揃っているかの判定
                            kakikae0_all() #盤面全部をおんなじ記号にする
                            print(banmen)
                            print('VICTORY!!user0の勝ちです!')
                            break
                        kakikae0(zyuu)  #盤面の書き換え，エリア内を全部おんじ記号にする
                        print(banmen)
                        kakikae0_list(zyuu,idx) #マップのリストもそのエリアにおけないように全部書き換え
                    else: #揃わなかった時
                        banmen_map[idx] = "o" #盤面のリストを書き換える
                        banmen = banmen.replace(str(user0_input)," o") #盤面を書き換える
                        print(banmen)
                else: #ネクストエリアにあってない時
                    print(err_message)
                    continue
            else: #おけない時
                print(err_message)
                continue
            hikiwake(zyuu) #引き分けエリアのリスト作成
            turn_user = 1
            turn_count += 1
            iti = num - (zyuu * 10)
            if (iti in user0_operations) or (iti in user1_operations) or (iti in hikiwake_list): #next_areaがすでに埋まってる時
                iti = 0 #アルティメットフリーにする
            next_area_str = rule_area[iti]
            next_area_int = iti
        else: #user1のターン
            try:
                mes1 = 'user1のターンです.このターンはエリア',next_area_str,'に置くことができます.座標を入力してください:'
                user1_input = input(mes1)
            except: #ちゃんと入力されなかったとき
                print(err_message)
                continue
            if user1_input in banmen_map: #おける時
                num = rule[user1_input] #指定した座標の数値を取得 user_inoutは"A1"みたいなやつ,numは11みたいなやつ
                zyuu = zyuunokurai(num) #numの10の位を求める
                if (zyuu == next_area_int) or (next_area_int == 0 and (zyuu == 1 or zyuu == 3 or zyuu == 5 or zyuu == 7 or zyuu == 9)): #ネクストエリアにあってるか
                    idx = banmen_map.index(user1_input)
                    user1_operations_area[zyuu-1].append(num - (zyuu * 10)) #user0がとったエリアのますのリストに追加
                    if check_decision(user1_operations_area[zyuu-1]) or zyuu == 2 or zyuu == 4 or zyuu == 6 or zyuu == 8: #エリア内で揃ったかの判定
                        user1_operations.append(zyuu) #盤面でのとったマスのリストに追加
                        if check_decision(user1_operations): #盤面で揃っているかの判定
                            kakikae1_all()
                            print(banmen)
                            print('VICTORY!!user1の勝ちです!')
                            break
                        kakikae1(zyuu)  #とったエリアを全部おんなじ記号にしたい
                        print(banmen)
                        kakikae1_list(zyuu,idx) #マップのリストもそのエリアにおけないように全部書き換え
                    else: #揃わなかった時
                        banmen_map[idx] = "x" #盤面のリストを書き換える
                        banmen = banmen.replace(str(user1_input)," x") #盤面を書き換える
                        print(banmen)
                else: #ネクストエリアにあってない時
                    print(err_message)
                    continue
            else: #おけない時
                print(err_message)
                continue
            hikiwake(zyuu) #引き分けエリアのリスト作成
            turn_user = 0
            turn_count += 1
            iti = num - (zyuu * 10)
            if (iti in user0_operations) or (iti in user1_operations) or (iti in hikiwake_list):
                iti = 0
            next_area_str = rule_area[iti]
            next_area_int = iti
        if sum(user0_operations)  +  sum(user1_operations)  +  sum(hikiwake_list) ==  45:
            print('引き分けです')
            break

ultmate_marubatu()