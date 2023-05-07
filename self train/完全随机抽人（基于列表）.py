import random

# 设置抽中的序号
select_people = []

# 运行主体
print('完全随机的抽取指定的人数')
all_people = int(input('总共多少人：'))
choose_people = int(input('要抽取的人数：'))

# 抽取环节
for people in range(choose_people):
    choose_one = random.randint(1, all_people)
    while True:
        # 判断是否与已有结果相同
        if choose_one not in select_people:
            select_people.append(choose_one)
            break
        else:
            choose_one = random.randint(1, all_people)

# 输出结果
for i in select_people:
    print('抽到了', i)
