import time, random
while True:
    player_victory=0
    enemy_victory=0
    for i in range(1,4):
        time.sleep(2)
        print("现在是第"+str(i)+"局")
        player_life=random.randint(100,150)
        player_attack=random.randint(30,50)
        enemy_life=random.randint(100,150)
        enemy_attack=random.randint(30,50)
        print("[玩家] \n "+"血量："+str(player_life)+"\n 攻击："+str(player_attack))
        time.sleep(1)
        print("[敌人] \n "+"血量："+str(enemy_life)+"\n 攻击："+str(enemy_attack))
        time.sleep(1)
        while player_life>0 and enemy_life>0:
              player_life=player_life-enemy_attack
              enemy_life=enemy_life-player_attack
              print("你发起了攻击。敌人剩余血量"+str(enemy_life))
              print("敌人发起了攻击。玩家剩余血量"+str(player_life))
              time.sleep(1.5)
        if player_life>0 and enemy_life<=0:
            player_victory=player_victory+1
            print("敌人死翘翘了，你赢啦")
        elif player_life<=0 and enemy_life>0:
            enemy_victory=enemy_victory+1
            print("敌人把你干掉了，你死啦")
        else:
            print("你们同归于尽啦")
    if player_victory>enemy_victory:
          print("最终结果：你赢啦")
    elif enemy_victory>player_victory:
          print("最终结果：你数啦") 
    else:
          print("最终结果：平局") 
    a1=input("要继续游戏吗？请输入n退出，输入其他就继续")
    if a1=="n":
       break
