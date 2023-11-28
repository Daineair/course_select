# D0971751

import globals

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

class classTime():
    def __init__(self, day, stime, hours, day2, stime2, hours2):
        self.day = day
        self.stime = stime
        self.hours = hours
        self.day2 = day2
        self.stime2 = stime2
        self.hours2 = hours2

def time(t):
    time_mapping = {
        "1013": "星期一 早上8點 3節",
        "1063": "星期一 下午1點 3節",
        "3032": "星期三 早上10點 2節",
        "5072": "星期五 下午2點 2節",
        "4061": "星期四 下午1點 1節",
        "1022": "星期一 早上9點 2節",
        "3042": "星期三 早上11點 2節",
        "2063": "星期二 下午1點 3節"
    }
    if t in time_mapping:
        return time_mapping[t]

def day(t):
    day_mapping = {
        "星期一": 1,
        "星期二": 2,
        "星期三": 3,
        "星期四": 4,
        "星期五": 5,
    }
    if t in day_mapping:
        return day_mapping[t]

global UserId
global States

def myCourses(state,uid):


    course_list_path = "C:/course_select/course_list.txt"
    CourseList = open(course_list_path, "r+", encoding="utf-8")
    student_course_list_path = "C:/course_select/student_course_list.txt"
    StudentCourseList = open(student_course_list_path, "r+", encoding="utf-8")
    User_list_path = "C:/course_select/User_list.txt"
    UserList = open(User_list_path, "r+", encoding="utf-8")
    
    myCoursesList = []
    timetable = [[0] * 5 for i in range(15)]
    TEACHERnAME = [[0] * 5 for i in range(15)]
    CLASSiD = [[0] * 5 for i in range(15)]

    C_list = CourseList.read().split("\n")
    S_list = StudentCourseList.read().split("\n")
    U_list = UserList.read().split("\n")


    cnt=0
    if (state == 1):
        studentID = uid
        for i  in range(len(U_list)):
            UserID = U_list[i].split()
            if(UserID[0] == studentID):
                student_info = userInfo(UserID[0],UserID[2])
        for i in range(len(S_list)):
            SID = S_list[i].split()
            if(len(SID)>1):
                if(SID[0] == studentID):
                    CourseID = SID[1]
                    for j in range(len(C_list)):
                        CID = C_list[j].split()
                        course = Course(CID[0], CID[1], CID[2], CID[3], CID[4], CID[5])
                        if(CourseID == course.cls_id):
                            myCoursesList.append(course)
                            Class_time = time(course.cls_time).split()
                            if(len(Class_time)<4):
                                class_day = int (course.cls_time[0])
                                class_time = int (course.cls_time[2])
                                class_num = int (course.cls_time[3])
                                for n in range(class_num):
                                    timetable[class_time+n-1][class_day-1] = course.cls_name
                                    for s in range(len(U_list)):
                                        Tname = U_list[s].split()
                                        if(len(Tname)>1):
                                            if(Tname[0]==course.cls_professor):
                                                TEACHERnAME[class_time+n-1][class_day-1] = Tname[2]
                                    CLASSiD[class_time+n-1][class_day-1] = course.cls_id
                                break
                            else:
                                t = classTime(Class_time[0],Class_time[1],Class_time[2],Class_time[4],Class_time[5],Class_time[6])
                                class_day = day(t.day)
                                if(len(t.stime)==4):
                                    if(t.stime in "早上"):
                                        class_time = int (t.stime[2]) - 7
                                    else:
                                        class_time = int (t.stime[2]) + 5
                                else:
                                    if(t.stime in "早上"):
                                        class_time = int (t.stime[2]+t.stime[3]) - 7
                                    else:
                                        class_time = int (t.stime[2]+t.stime[3]) + 5
                                
                                class_num = int (t.hours[0])
                                for n in range(class_num):
                                    timetable[class_time+n-1][class_day-1] = course.cls_name
                                    for s in range(len(U_list)):
                                        Tname = U_list[s].split()
                                        if(len(Tname)>1):
                                            if(Tname[0]==course.cls_professor):
                                                TEACHERnAME[class_time+n-1][class_day-1] = Tname[2]
                                    CLASSiD[class_time+n-1][class_day-1] = course.cls_id
                                class_day = day(t.day2)
                                if(len(t.stime2)==4):
                                    if(t.stime2 in "早上"):
                                        class_time = int (t.stime2[2]) - 7
                                    else:
                                        class_time = int (t.stime2[2]) + 5
                                else:
                                    if(t.stime in "早上"):
                                        class_time = int (t.stime2[2]+t.stime2[3]) - 7
                                    else:
                                        class_time = int (t.stime2[2]+t.stime2[3]) + 5
                                class_num = int (t.hours2[0])
                                for n in range(class_num):
                                    timetable[class_time+n-1][class_day-1] = course.cls_name
                                    for s in range(len(U_list)):
                                        Tname = U_list[s].split()
                                        if(len(Tname)>1):
                                            if(Tname[0]==course.cls_professor):
                                                TEACHERnAME[class_time+n-1][class_day-1] = Tname[2]
                                    CLASSiD[class_time+n-1][class_day-1] = course.cls_id
                                break

        print("\n姓名: "+student_info.cid+"\t學號: "+student_info.uid+"\n")
    else:
        teacherID = uid
        for i  in range(len(U_list)):
            UserID = U_list[i].split()
            if(UserID[0] == teacherID):
                teacher_info = userInfo(UserID[0],UserID[2])
        for i in range(len(C_list)):
            CID = C_list[i].split()
            if(len(CID)>4):
                if(CID[2] == teacherID):
                    CourseID = CID[0]
                    course = Course(CID[0], CID[1], CID[2], CID[3], CID[4], CID[5])
                    if(CourseID == course.cls_id):
                        cnt += cnt + 1
                        myCoursesList.append(course)
                        class_day = int (course.cls_time[0])
                        class_time = int (course.cls_time[2])
                        class_num = int (course.cls_time[3])
                        for n in range(class_num):
                            timetable[class_time+n-1][class_day-1] = course.cls_name
                            for s in range(len(U_list)):
                                Tname = U_list[s].split()
                                if(len(Tname)>1):
                                    if(Tname[0]==course.cls_professor):
                                        TEACHERnAME[class_time+n-1][class_day-1] = Tname[2]
                            CLASSiD[class_time+n-1][class_day-1] = course.cls_id
            
        print("\n姓名: "+teacher_info.cid+"\t學號: "+teacher_info.uid+"\n")
    
    print("-----------------------------------------------------------------------------------------")
    print("|   \t|星期一\t\t|星期二\t\t|星期三\t\t|星期四\t\t|星期五\t\t|")

    print("-----------------------------------------------------------------------------------------")
    for i in range(15):
        for l in range(3):
            if(l==1):
                print("|",i+1,"\t"+"|",end="")
            else:
                print("|","\t"+"|",end="")
            for j in range(5):
                if(timetable[i][j]!=0):
                    if(l == 0):
                        print(CLASSiD[i][j],"\t\t"+"|",end="")
                    if(l == 1):
                        print(timetable[i][j],"\t"+"|",end="")
                    if(l == 2):
                        if(len(TEACHERnAME[i][j])>4):
                            print(f'({TEACHERnAME[i][j]})\t|',end="")
                        else:
                            print(f'({TEACHERnAME[i][j]})\t\t|',end="")
                else:
                    print("\t\t"+"|",end="")
            
            print("")
        print("-----------------------------------------------------------------------------------------")
    print("")
    credit(state,myCoursesList)
    if(state == 1):
        for i in range(len(S_list)): #對身分
            SID = S_list[i].split()
            if(len(SID)>1):
                if SID[0] == studentID:
                    for j in range(len(C_list)): #對課表課程
                        unit = C_list[j].split()
                        # print(unit)
                        if(len(unit)>4):
                            course = Course(unit[0], unit[1], unit[2], unit[3], unit[4], unit[5])
                            if course.cls_id == SID[1]: 
                                print(f'課程代碼: {course.cls_id} 課程名稱: {course.cls_name} 課程學分: {course.cls_num} 課程時間: {time(course.cls_time)}\n')
            
    else:
        for j in range(len(C_list)): #對課表課程
            unit = C_list[j].split()
            # print(unit)
            if(len(unit)>4):
                course = Course(unit[0], unit[1], unit[2], unit[3], unit[4], unit[5])
                if course.cls_professor == teacher_info.uid: 
                    print(f'課程代碼: {course.cls_id} 課程名稱: {course.cls_name} 課程學分: {course.cls_num} 課程時間: {time(course.cls_time)}\n')
    
    CourseList.close()
    StudentCourseList.close()
    UserList.close()



def credit(state,myCoursesList):
    sum = 0
    if(state == 1):
        for i in myCoursesList:
            sum = sum + int (i.cls_num)
        print("總學分:" ,sum,"\n")
    myCoursesList[:] = []
    sum = 0
