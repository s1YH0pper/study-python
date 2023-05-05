import random

# 设置抽中的序号
select_people = set()

# 运行主体
print('完全随机的抽取指定的人数')
all_people = int(input('总共多少人：'))
choose_people = int(input('要抽取的人数：'))

# 抽取环节
while True:
    select_people.add(random.randint(1, all_people))
    if len(select_people) == choose_people:
        break

# 输出结果
for i in select_people:
    print('抽到了', i)
