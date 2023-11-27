# import globals
# from login import User

# AddNum = 0
# ClassId = "0000"
# ClassType = "0"
# ClassNum = 0
# ClassTime = 0
# StudentCredit = 0
# add_flag = 1
# path1 = "C:/course_select/course_list.txt"
# f = open(path1, "r+", encoding="utf-8")
# path2 = "C:/course_select/student_course_list.txt"
# nf = open(path2, "r+", encoding="utf-8")

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

def add(state,uid,course_code):
    #ClassId = "0000"
    ClassType = "0"
    ClassNum = 0
    ClassTime = 0
    StudentCredit = 0
    add_flag = 1
    path1 = "C:/course_select/course_list.txt"
    f = open(path1, "r+", encoding="utf-8")
    path2 = "C:/course_select/student_course_list.txt"
    nf = open(path2, "r+", encoding="utf-8")
    s = f.read().split("\n")
    ns = nf.read().split("\n")
    if(state == 2):
        print("\n輸入學生學號：")
        AddUID = input().split()
        studentID = AddUID[0]
    else:
        studentID = uid
        
    #print("\n輸入預加選課程代碼：")
    add_flag = 1
    StudentCredit = 0
    add_time = 0
    add_time_day = 0
    add_time_start = 0
    add_time_conti = 0
    add_classId = course_code
    for i in range(len(s)): 
        unit = s[i].split()
        course = Course(unit[0], unit[1], unit[2], unit[3], unit[4], unit[5])
        if(course.cls_id == add_classId): #Select
            ClassType = course.cls_type
            ClassNum = int(course.cls_num)
            ClassTime = int(course.cls_time)
            add_time = ClassTime #加選課程時間分析
            add_time_day = add_time // 1000 
            add_time_start = (add_time - (add_time_day*1000)) // 10
            add_time_conti = add_time % 10
    for i in range(len(s)): 
        unit = s[i].split()
        course = Course(unit[0], unit[1], unit[2], unit[3], unit[4], unit[5])
        #print("\n", course.cls_id, course.cls_type, course.cls_num)
        #print("\n", add_classId, ClassType, ClassNum, ClassTime)
        #print("\nadd", add_time, add_time_day, add_time_start, add_time_conti)
        for j in range(len(ns)): #Credit Total
            num = ns[j].split()
            studentCourse = StudentCourse(num[0], num[1]) 
            if(studentCourse.uid == studentID):              
                if(studentCourse.cid == course.cls_id): 
                    credit = int(course.cls_num) #學分計算
                    StudentCredit += credit  
                    #print(StudentCredit,studentCourse.cid, course.cls_id, studentCourse.uid, "\n")
                    time = int(course.cls_time) #學生課程時間分析
                    time_day = time // 1000
                    time_start = (time - (time_day*1000)) // 10
                    time_conti = time % 10
                    #print("\ncourse", time, time_day, time_start, time_conti)
                    #print("\nadd", add_time, add_time_day, add_time_start, add_time_conti)
                    #print("\nstudentCourse.cid", studentCourse.cid,"add", add_classId)
                    if(studentCourse.cid == course_code): #是否同一堂課
                        add_flag = 2
                    elif((add_time_day == time_day) and add_time != 0): #時間是否衝突
                        for i in range(add_time_start, (add_time_start+add_time_conti+1)):
                            #print("\ni:", i)
                            if(i>=time_start and i<=(time_start+time_conti)):
                                add_flag = 0
                                break
                                print("\naddfilg", add_flag)
                    #print("flag", add_flag)
    if(state == 1):
        if(ClassType == "0"): #為必修課
            print("必修課無法自行加選，找該課老師加選吧！")
        elif(add_flag == 2): #重複加選ㄌ
            print("加選失敗，課程已重複加選了ฅ●ω●ฅ")
        elif(add_flag == 0): #衝堂ㄌ
            print("課堂時間衝突了(つ´ω`)つ")
        elif(StudentCredit + ClassNum > 10): #超過學分上限
            print("超過學分上限囉.-.")
        else: #寫入學生資料
            with open(path2, "a") as file:
                file.write("\n" + studentID + "        " + add_classId)
            print("加選成功(′゜ω。‵)")
    elif(state == 2):
        if(add_flag == 2): #重複加選ㄌ
            print("加選失敗，課程已重複加選了ฅ●ω●ฅ")
        elif(add_flag == 0): #衝堂ㄌ
            print("加選失敗課堂時間衝突了(つ´ω`)つ")
        elif(StudentCredit + ClassNum > 10): #超過學分上限
            print("加選失敗超過學分上限囉.-.")
        else: #寫入學生資料
            with open(path2, "a") as file:
                file.write("\n" + studentID + "        " + add_classId)
            print("加選成功(′゜ω。‵)")
    f.close()
    nf.close()
# add(state,uid)
# f.close()
# nf.close()
