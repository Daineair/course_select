#import globals
import fileinput
#from add_login import User

with open("C:/course_select/course_list.txt", "r", encoding="utf-8") as course_file:
        c = course_file.read().split("\n")
with open("C:/course_select/student_course_list.txt", "r", encoding="utf-8") as s_course_file:
        sc = s_course_file.read().split("\n")

class Course():
    def __init__(self, cls_id, cls_name, cls_professor, cls_type, cls_num, cls_time):
        self.cls_id = cls_id
        self.cls_name = cls_name
        self.cls_professor = cls_professor
        self.cls_type = cls_type
        self.cls_num = cls_num
        self.cls_time = cls_time
   
class StudentCourse():
    def __init__(self, uid, cid):
        self.uid = uid
        self.cid = cid
        
def delete(state ,uid):
    if state == 2:
        print("\n老師無法幫學生退選，請學生自行退選")
    else:
        #print("in delete_section")
        studentID = uid
        while 1==1:
            choose=0
            choose=input()
            choose_flag=0
            for k in range(len(sc)): #對身分
                num = sc[k].split()
                studentCourse = StudentCourse(num[0], num[1])
                if choose==studentCourse.cid:
                    choose_flag=1
                    print("選擇退選"+choose)
                    break
            if choose_flag==1:   
                break
            if choose_flag==0:   
                print("您的課程沒有代碼為"+choose+"請再輸入一次")
                for i in range(len(sc)): #對身分
                    num = sc[i].split()
                    studentCourse = StudentCourse(num[0], num[1]) 
                    if studentCourse.uid == studentID:
                        for j in range(len(c)): #對課表課程
                            unit = c[j].split()
                            course = Course(unit[0], unit[1], unit[2], unit[3], unit[4], unit[5])
                            if course.cls_id == studentCourse.cid: 
                               print(f'課程代碼: {course.cls_id} 課程名稱: {course.cls_name} 課程學分: {course.cls_num} 課程時間: {time(course.cls_time)}')
        minus=0
        total=0
        final=0
        for j in range(len(c)): #找該課程學分
            unit = c[j].split()
            course = Course(unit[0], unit[1], unit[2], unit[3], unit[4], unit[5])
            if choose == unit[0]: 
                minus=int(unit[4])
                #print("扣該課程學分" + str(minus))
                break
        for i in range(len(sc)): #對身分
            num = sc[i].split()
            studentCourse = StudentCourse(num[0], num[1]) 
            if studentCourse.uid == studentID:    
                for k in range(len(c)): #對課表課程
                    unit = c[k].split()
                    course = Course(unit[0], unit[1], unit[2], unit[3], unit[4], unit[5])
                    if course.cls_id == studentCourse.cid: 
                        total+=int(unit[4])
                        #print("目前課程學分" + str(total))
        final=total-minus
        #print("總學分" + str(final))
        if final>=7:
            deleteself=3
            for i in range(len(c)): #找該課程學分
                    #print("in loop")
                    unit = c[i].split()
                    course = Course(unit[0], unit[1], unit[2], unit[3], unit[4], unit[5])
                    if choose == unit[0]: 
                        deleteself=unit[3]
                        #print("是否為必修:"+deleteself+" unit[0]:"+unit[0]+" unit[3]:"+unit[3])
                        break
            #print("deleteself:"+str(deleteself))
            if deleteself=="1":
                delete_id=0
                delete_cid=0
                for i in range(len(sc)): #對身分
                    num = sc[i].split()
                    studentCourse = StudentCourse(num[0], num[1])
                    if choose==num[1]:
                        delete_id=num[0]
                        delete_cid=num[1]
                        break
                #print("delete_id:"+delete_id+" delete_cid:"+delete_cid)
                with fileinput.FileInput("C:/course_select/student_course_list.txt", inplace=True, backup=".bak") as file:
                   for line in file:
                       if f"{delete_id}\t{delete_cid}" not in line:
                           print(line, end='')
                print("退選成功，以下是您的課表")
                with open("C:/course_select/student_course_list.txt", "r", encoding="utf-8") as s_course_file:
                    sc2 = s_course_file.read().split("\n")
                for i in range(len(sc2)): #對身分
                    num2 = sc2[i].split()
                    studentCourse2 = StudentCourse(num2[0], num2[1]) 
                    if studentCourse2.uid == studentID:
                        for j in range(len(c)): #對課表課程
                            unit = c[j].split()
                            course = Course(unit[0], unit[1], unit[2], unit[3], unit[4], unit[5])
                            if course.cls_id == studentCourse2.cid: 
                               print(f'課程代碼: {course.cls_id} 課程名稱: {course.cls_name} 課程學分: {course.cls_num} 課程時間: {time(course.cls_time)}')
            else:
                print("退選失敗，必修不能退選")
        else:
            print("退選失敗，學分下限不能低於七學分")
