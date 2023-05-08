import random


# 定义抽奖函数
def random_pick(count: int, pick: int) -> list:
    result = list()
    for i in range(pick):
        choose_one = random.randint(1, count)
        while True:
            # 判断是否与已有结果相同
            if choose_one not in result:
                result.append(choose_one)
                break
            else:
                choose_one = random.randint(1, count)
    return result


# 运行主体
print('完全随机的抽取指定的人数')
all_people = int(input('总共多少人：'))
choose_people = int(input('要抽取的人数：'))

# 抽取环节
select_people = random_pick(all_people, choose_people)

# 输出结果
for i in select_people:
    print('抽到了', i)
