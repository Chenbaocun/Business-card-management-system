# -*- coding: utf-8 -*-
# @Time : 2020/3/10 16:37
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : card_tools.py
# @Software: PyCharm
card_list = []


def add_card():
    '''
    新建莫名片
    :return: 不返回
    '''
    print("功能:新建名片：")
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    qq = input("请输入 QQ 号码：")
    email = input("请输入邮箱：")
    card_dict = {"name": name, "phone": phone, 'qq': qq, "email": email}
    card_list.append(card_dict)
    print("成功添加 %s 的名片" % name)


def show_all_card():
    '''
    显示所有的名片
    :return: 如果没有存储名片返回空
    '''
    print("功能：显示全部")
    if len(card_list) == 0:
        print("无数据")
        return
    print("姓名\t\t\t\t电话\t\t\t\tQQ\t\t\t\t邮箱\t\t\t\t")
    print("-" * 50)
    for card_dict in card_list:
        print("%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t" % (
            card_dict['name'], card_dict['phone'], card_dict['qq'], card_dict['email']))


def find_card():
    '''
    查找指定姓名的名片
    :return:
    '''
    print("功能：搜索名片")
    name = input("请输入要搜索的姓名：")
    for card_dict in card_list:
        if card_dict['name'] == name:
            print("姓名\t\t\t\t电话\t\t\t\tQQ\t\t\t\t邮箱\t\t\t\t")
            print("-" * 50)
            print("%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t" % (
                card_dict['name'], card_dict['phone'], card_dict['qq'], card_dict['email']))
            print("-" * 50)
            choice = input("请输入对名片的操作：1：修改/ 2.删除/ 0：返回上级菜单 ：")
            if choice == '1':
                index = card_list.index(card_dict)
                card_dict = card_list[index]
                card_dict['name'] = judge(card_dict['name'], input("请输入姓名【单纯回车不修改】："))
                card_dict['phone'] = judge(card_dict['phone'], input("请输入电话【单纯回车不修改】："))
                card_dict['qq'] = judge(card_dict['qq'], input("请输入 QQ 号码【单纯回车不修改】："))
                card_dict['email'] = judge(card_dict['email'], input("请输入邮箱【单纯回车不修改】："))
                print("用户%s名片信息修改成功" % card_dict['name'])
                break
            if choice == '2':
                card_list.remove(card_dict)
                print("用户%s删除成功" % card_dict['name'])
                break
            if choice == '0':
                break
    else:
        print("没有该人记录")


def judge(info, input):
    '''
    判断用户是否需要修改当前信息
    :param info:信息
    :param input: 输入的信息
    :return: 决策后的修改数据
    '''
    if input == "":
        return info
    else:
        return input
