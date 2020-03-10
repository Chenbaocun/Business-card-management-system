# -*- coding: utf-8 -*-
# @Time : 2020/3/10 16:37
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : card_main.py
# @Software: PyCharm
import card_tools
while True:
    print("*" * 50)
    print("欢迎使用【名片管理系统】 V1.0")
    print('1. 新建名片')
    print('2. 显示全部')
    print('3. 查询名片')
    print()
    print("0. 退出系统")

    print("*" * 50)
    choice = input("请选择操作功能：")
    if choice == '1':
        print("您选择的操作是：1")
        print('-' * 50)
        card_tools.add_card()
    elif choice == '2':
        print("您选择的操作是：2")
        print('-' * 50)
        card_tools.show_all_card()
    elif choice == '3':
        print("您选择的操作是：3")
        print('-' * 50)
        card_tools.find_card()
    elif choice == '0':
        break
    else:
        print("输入有误请您重新输入！")
