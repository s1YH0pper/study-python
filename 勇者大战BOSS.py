# 代码实例
# 开发者：霍珀
# 版权所有：Team GS

# 输入玩家姓名
user_name = input('请输入玩家名：')
boss_name = input('请输入BOSS名：')

# 游戏开始界面
print('=' * 5, user_name, '大战%s' % boss_name, '=' * 5, sep='')
print('1.攻击力是指攻击时最大造成的伤害')
print('2.每次练级时成长的数值是随机的')
print('3.BOSS每次造成的伤害是随机的')
print('4.其他设定由玩家自己探索')
print('=' * 20)
print('请选择你的身份')
print('     1、勇者')
print('     2、BOSS')
print('')

# 游戏角色选择
start_choice = int(input('请选择(1-2):'))
if start_choice == 1:
    print('你已经选择勇者，恭喜你将以勇者的身份进行游戏！')
elif start_choice == 2:
    print('臭小子想当BOSS，你给我去当勇者，我才是BOSS！')
else:
    print('你的输入不正确，系统自动为你选择勇者！')
print('=' * 5, '游戏开始', '=' * 5, sep='')

# 数值初始化
import random

train = 4
attack = 2
health = 10
BOSS_health = random.randint(20, 40)

# 游戏系统
print('你的身份是->勇者<-,你的攻击力是：', attack, '你的生命值是：', health, sep='')
while True:
    print('')
    print('请选择你要做的操作：')
    print('     1、练级,你还有', train, '次机会', sep='')
    print('     2、打BOSS(建议血量>30)')
    print('     3、逃跑')
    print('')

    game_choice = int(input('请选择(1-3)：'))

    print('')
    if game_choice == 1:
        if train > 0:
            train -= 1
            add_attack = random.randint(4, 12)
            add_health = random.randint(1, 9)
            attack += add_attack
            health += add_health

            print('你的攻击力增加了：', add_attack, '点，生命值增加了：', add_health, '点', sep='')
        else:
            print('你已经没有练级机会了')
    elif game_choice == 2:

        print('=' * 5, '战斗开始', '=' * 5, sep='')

        while health > 0 and BOSS_health > 0:
            damage = random.randint(attack // 2, attack)
            BOSS_health -= damage

            print('你对BOSS造成了', damage, '点伤害，BOSS还剩', BOSS_health, '生命值', sep='')
            print('')

            BOSS_attack = random.randint(10, 30)
            health -= BOSS_attack

            print('BOSS对你造成了', BOSS_attack, '点伤害，你还剩', health, '生命值', sep='')
            print('')

            # 先进行一次判断是否出现选项
            if BOSS_health <= 0 or health <= 0:
                continue

            # 下一次攻击判断
            print('请选择你要做的操作：')
            print('     1、继续攻击')
            print('     2、投降')
            battle_choice = input('选择：')
            if battle_choice == 2:
                print('你被BOSS打败了')
                break

        # 胜负条件判断
        else:
            if BOSS_health <= 0 and health > 0:
                print('恭喜你打败了BOSS')
                break
            elif health <= 0 and BOSS_health > 0:
                print('你被BOSS打败了')
                print('是否再次战斗(1.是/2.否),有额外加强')
                again_choice = int(input('请选择：'))
                if again_choice == 1:
                    train = 4
                    train += random.randint(1, 2)
                    attack = 2
                    attack += random.randint(2, 3)
                    health = 10
                    health += random.randint(2, 3)
                    BOSS_health = random.randint(20, 40)
                elif again_choice == 2:
                    break
                else:
                    print('输入错误，再次选择')
            else:
                print('同归于尽，Game Over！！！')
                print('是否再次战斗(1.是/2.否)')
                again_choice = int(input('请选择：'))
                if again_choice == 1:
                    train = 4
                    attack = 2
                    health = 10
                    BOSS_health = random.randint(20, 40)
                    print('')
                elif again_choice == 2:
                    break
                else:
                    print('输入错误，再次选择')
    elif game_choice == 3:
        print('胆小鬼！！！给爷爬！！！')
        break
    else:
        print('你的输入不正确，请重新选择')
    print('你的攻击力是：', attack, '你的生命值是：', health, sep='')
input('回车退出游戏')
