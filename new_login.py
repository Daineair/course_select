# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 15:06:37 2023

@author: d1090654
"""
import new_course_system
import my_course
import delete_selection
user_f = open("C:/course_select/User_list.txt","r+",encoding="utf-8")
# a = "AAA"
# user_f.write(a)
# user_f.close()
class User():
    def __init__(self,uid,pw,name):
        self.uid = uid
        self.pw = pw
        self.name = name
def login(login_state):
    global state,uid
    if(login_state == 0):
        state = 0
        print("Enter your id and password:")
        s = user_f.read().split("\n")
        info = input().split()
        if(len(info) > 2 or len(info) < 2):
            print("Must input a set of id and a set of password.")
            return 0
        uid = info[0]
        upw = info[1]
        i = 0
        for i in range(len(s)):
            unit = s[i].split()
            user = User(unit[0],unit[1],unit[2])
            if(uid == user.uid and upw == user.pw):
                login_state = 1#確保現在是登入成功狀態
                if uid[0] == 'D':
                    state = 1
                elif uid[0] == 'T':
                    state = 2
                print("login successfully!")
        if state == 0:
            print("ERROR! Wrong user id or password.")
            login_state = 0
        login(login_state)
    else:
        if state == 1:#學生
            mode = input("Enter '1' search courses, '2' check your courses,'0' log out': ")
        elif state == 2:#老師
            mode = input("Enter '1' search courses,'0' log out':")
        print(mode)
        if mode == '0':
            print("log out successfully!")
            return 1
        elif mode == '1':
            print("search courses.")
            login_state = new_course_system.course_main(login_state, state, uid)
            print("login = ",login_state)
        elif mode == '2':
            withdraw_course = 0
            print("check your courses.")
            my_course.myCourses(state, uid)
            withdraw_course = input("Do you want to withdraw any course?(y/n)")
            if withdraw_course=="y":
                print("yes")
                delete_selection.delete(state, uid)
        login(login_state)
global login_state
login_state = 0
login(login_state)
