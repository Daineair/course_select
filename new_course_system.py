# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 23:07:25 2023

@author: D0927628
"""
# import globals
# from login import user
import modify_content
import new_add_selection
def read_course_data(file_path):
    courses = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            course_data = line.strip().split()
            courses.append(course_data)
    return courses

def read_teacher_data(file_path):
    teachers = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            teacher_data = line.strip().split()
            teachers[teacher_data[0]] = teacher_data[2]
    return teachers

def convert_schedule(schedule):
    day_map = {"1013": "星期一 早上8點 3節",
               "1063": "星期一 下午1點 2節",
               "3032": "星期三 早上10點 2節",
               "5072": "星期五 下午2點 2節",
               "4061": "星期四 下午1點 1節",
               "1022": "星期一 早上9點 2節"}

    schedule_info = day_map.get(schedule, "未知日期和時間")
    return schedule_info

def search_course(course_code, courses):
    for course in courses:
        if course[0] == course_code:
            return course
    return None

def display_course_info(course,login_state, state, uid):
    if course:
        print(f"課程名稱：{course[1]}")
        print(f"授課教師：{teachers.get(course[2], '未知名字')}")
        print(f"類型：{'必修' if course[3] == '0' else '選修'}")
        print(f"學分數：{course[4]}")
        print(f"時間：{convert_schedule(course[5])}")
        print(f"課程描述：{course[6]}")
        print(f"課程目標：{course[7]}")
    else:
        print("找不到該課程")
        course_main(login_state, state, uid)
def course_main(login_state,state,uid):
    #if __name__ == "__login__":
       global teachers
       file_path = "course_list.txt"
       file_path_teachers = "User_list.txt"
       courses = read_course_data(file_path)
       teachers = read_teacher_data(file_path_teachers)
         
       while True:
           print("state =",state)
           if state == 1 or 2:
               course_code = input("輸入課程代碼 (或輸入 '0' 退出): ")
                    
               if course_code.lower() == '0':
                    print("離開查詢系統。")
                    print(login_state)
                    return 1
           course = search_course(course_code, courses)
           display_course_info(course,login_state, state, uid)
           print("使用者ID=",uid)
           if(state == 1):
               x = input("如要加選該課程請按'1'，繼續查詢按其他任意建:")
               if(x == '1'):
                   new_add_selection.add(state,uid,course_code)
           if(state == 2 and course[2] == uid) :
               mode = input("可輸入'1'進入修改模式，輸入'2'為學生加選(或輸入其他任意建退回搜尋課程):")
               if mode == '1':
                   modify_content.modify(course[2],course[6], course[7])
                   print("修改完成，繼續搜尋課程模式")
               elif mode == '2':
                   new_add_selection.add(state,uid,course_code)
