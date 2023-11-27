# D0971751

import globals
from add_login import User

course_list_path = "C:/course_select/course_list.txt"
CourseList = open(course_list_path, "r+", encoding="utf-8")
student_course_list_path = "C:/course_select/student_course_list.txt"
StudentCourseList = open(student_course_list_path, "r+", encoding="utf-8")
User_list_path = "C:/course_select/User_list.txt"
UserList = open(User_list_path, "r+", encoding="utf-8")

myCoursesList = []
timetable = [[0] * 5 for i in range(15)]

class Course():
    def __init__(self, cls_id, cls_name, cls_professor, cls_type, cls_num, cls_time):
        self.cls_id = cls_id
        self.cls_name = cls_name
        self.cls_professor = cls_professor
        self.cls_type = cls_type
        self.cls_num = cls_num
        self.cls_time = cls_time
   
class userInfo():
    def __init__(self, uid, cid):
        self.uid = uid
        self.cid = cid

def myCourses():
    C_list = CourseList.read().split("\n")
    S_list = StudentCourseList.read().split("\n")
    U_list = UserList.read().split("\n")
    cnt=0
    if(globals.state == 1):
        studentID = globals.uid
        for i  in range(len(U_list)):
            UserID = U_list[i].split()
            if(UserID[0] == studentID):
                student_info = userInfo(UserID[0],UserID[2])
        for i in range(len(S_list)):
            SID = S_list[i].split()
            if(SID[0] == studentID):
                CourseID = SID[1]
                for j in range(len(C_list)):
                    CID = C_list[j].split()
                    course = Course(CID[0], CID[1], CID[2], CID[3], CID[4], CID[5])
                    if(CourseID == course.cls_id):
                        myCoursesList.append(course)
                        class_day = int (course.cls_time[0])
                        class_time = int (course.cls_time[2])
                        class_num = int (course.cls_time[3])
                        for i in range(class_num):
                            timetable[class_time+i-1][class_day-1] = course.cls_name
                        break

        print("\n姓名： "+student_info.cid+"\t學號： "+student_info.uid+"\n")
        print("-----------------------------------------------------------------------------------------")
        print("|   \t|星期一\t\t|星期二\t\t|星期三\t\t|星期四\t\t|星期五\t\t|")

        print("-----------------------------------------------------------------------------------------")
        for i in range(15):
            print("|",i+1,"\t"+"|",end="")
            for j in range(5):
                if(timetable[i][j]!=0):
                    print(timetable[i][j],"\t"+"|",end="")
                else:
                    print("\t\t"+"|",end="")
            print("")
            print("-----------------------------------------------------------------------------------------")
    else:
        teacherID = globals.uid
        for i  in range(len(U_list)):
            UserID = U_list[i].split()
            if(UserID[0] == teacherID):
                teacher_info = userInfo(UserID[0],UserID[2])
        for i in range(len(C_list)):
            CID = C_list[i].split()
            if(CID[2] == teacherID):
                CourseID = CID[0]
                course = Course(CID[0], CID[1], CID[2], CID[3], CID[4], CID[5])
                if(CourseID == course.cls_id):
                    cnt += cnt + 1
                    myCoursesList.append(course)
                    class_day = int (course.cls_time[0])
                    class_time = int (course.cls_time[2])
                    class_num = int (course.cls_time[3])
                    for j in range(class_num):
                        timetable[class_time+j-1][class_day-1] = course.cls_name
        
        print("\n姓名： "+teacher_info.cid+"\t學號： "+teacher_info.uid+"\n")
        print("-----------------------------------------------------------------------------------------")
        print("|   \t|星期一\t\t|星期二\t\t|星期三\t\t|星期四\t\t|星期五\t\t|")

        print("-----------------------------------------------------------------------------------------")
        for i in range(15):
            print("|",i+1,"\t"+"|",end="")
            for j in range(5):
                if(timetable[i][j]!=0):
                    print(timetable[i][j],"\t"+"|",end="")
                else:
                    print("\t\t"+"|",end="")
            print("")
            print("-----------------------------------------------------------------------------------------")
   
myCourses()
CourseList.close()
StudentCourseList.close()


def credit():
    sum = 0
    for i in myCoursesList:
        sum = sum + int (i.cls_num)
    print("\n總學分：" ,sum,"\n")
credit()
