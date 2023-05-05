# 显示欢迎界面
print('=' * 10, '欢迎使用员工管理系统', '=' * 10)
# 创建一个列表，用来保存员工的信息
emps = ['孙悟空\t18\t男\t花果山']

while True:
    print('请选择要做的操作：')
    print('\t1.显示员工列表')
    print('\t2.添加员工')
    print('\t3.删除员工')
    print('\t4.退出系统')
    user_choose = int(input('请选择[1-4]:'))
    print('=' * 42)
    # 根据选择进行相关操作
    if user_choose == 1:
        # 查询员工
        print('\t序号\t姓名\t年龄\t性别\t住址')
        # 创建一个变量，来表示员工的序号
        n = 1
        # 显示员工信息
        for emp in emps:
            print(f'\t{n}\t{emp}')
            n += 1
    elif user_choose == 2:
        # 添加员工
        # 获取要添加员工的信息
        emp_name = input('请输入员工姓名：')
        emp_age = input('请输入员工年龄：')
        emp_gender = input('请输入员工性别：')
        emp_address = input('请输入员工住址：')
        emp = f'{emp_name}\t{emp_age}\t{emp_gender}\t{emp_address}'
        # 显示一个提示信息
        print('以下员工将被添加到系统中')
        print('=' * 42)
        print('姓名\t年龄\t性别\t住址')
        print(emp)
        print('=' * 42)
        user_confirm = input('是否确认该操作[Y/N]:')
        # 判断
        if user_confirm == 'y':
            # 确认
            emps.append(emp)
            print('添加成功')
        else:
            # 取消操作
            print('添加已取消')
    elif user_choose == 3:
        # 删除员工
        # 获取要删除员工的序号
        del_number = int(input('请输入要删除的员工序号'))
        # 判断序号是否有效
        if 0 < del_number <= len(emps):
            del_index = del_number - 1
            # 显示提示
            print('以下员工将被删除')
            print('=' * 42)
            print('\t序号\t姓名\t年龄\t性别\t住址')
            print(f'\t{del_number}\t{emps[del_index]}')
            print('=' * 42)
            user_confirm = input('是否确认该操作[Y/N]:')
            # 判断
            if user_confirm == 'y':
                # 删除元素
                emps.pop(del_index)
                print('员工已被删除')
            else:
                print('操作已取消')
        else:
            print('您的输入有误，请重新操作')
    elif user_choose == 4:
        print('欢迎使用，再见！')
        break
    else:
        print('输入有误，重新选择')
    print('=' * 42)
