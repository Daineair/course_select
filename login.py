# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 15:06:37 2023

@author: d1090654
"""
import course_system
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
        print("Enter your id and passward:")
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
                login_state = 1
                if uid[0] == 'D':
                    state = 1
                elif uid[0] == 'T':
                    state = 2
                print("login successfully!")
                # if state == 1:
                #     mode = input("Enter '1' search courses, '2' check your courses: ")
                # elif state == 2:
                #     mode = input("Enter '1' search courses:")
                # print(mode)
                # if mode == '1':
                #     print("search courses.")
                #     course_system.course_system()
                # return 1
        if state == 0:
            print("ERROR! Wrong user id or password.")
            login_state = 0
        login(login_state)
    else:
        if state == 1:
            mode = input("Enter '1' search courses, '2' check your courses,'0' log out': ")
        elif state == 2:
            mode = input("Enter '1' search courses,'0' log out':")
        print(mode)
        if mode == '0':
            print("log out successfully!")
            return 1
        elif mode == '1':
            print("search courses.")
            login_state = course_system.course_system(login_state,state,uid)
            print("login = ",login_state)
        elif mode == '2':
            print("check your courses.")
        login(login_state)
global login_state
login_state = 0
login(login_state)