#學生類別
class Student:
    #名子,學號,科系
    def __init__(self, name, id, major):
        self.name = name  
        self.id = id
        self.department = major
        self.course_changes = self.CourseAddDrop(self.id)

    #加退選類
    class CourseAddDrop:
        
        #學生ID,加選,退選
        def __init__(self, student_id):
            self.student_id = student_id
            #一開始沒有加選
            self.added_courses = [] 
             #一開始沒有退選
            self.dropped_courses = []
            
        #加入課
        def add_course(self, course):
            self.added_courses.append(course)
            print(f"{self.student_id} 已加入 {course}.")


        #退選課
        def drop_course(self, course):
            self.added_courses.remove(course)  
            self.dropped_courses.append(course)
            print(f"{self.student_id} 已退出 {course}.")

#創建學生         
stu1 = Student("劉宗", "4A9G0105", "資訊工程")  

#加選課程
stu1.course_changes.add_course("C++程式設計")
stu1.course_changes.add_course("資料庫系統")

#退選課程  
stu1.course_changes.drop_course("資料庫系統")  

print(stu1.name, stu1.course_changes.added_courses)
print(stu1.name, stu1.course_changes.dropped_courses)
            




