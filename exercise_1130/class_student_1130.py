class Student:

    #類別屬性
    schoolName="南台科大"
    schoolAddress="南台街1號"


    def __init__(self) -> None:
        pass

    def __init__(self,major,departmentChairName,studentName,studentID,grade,getCredit,gradesGPA,studentAddress):
        self._major=major #科系名稱
        self._departmentChairName=departmentChairName #系主任姓名
        self._studentName=studentName#學生姓名
        self._studentID=studentID #學生學號(ID)
        self._grade=grade #年級
        self._getCredit=getCredit #取得學分
        self._gradesGPA=gradesGPA #成績GPA
        self._studentAddress=studentAddress #學生地址

    def get_schoolName(self): #取得學校名子
        return self.schoolName

    def get_schoolAddress(self): #取得學校地址
        return self.schoolAddress

    def get_major(self): #取得科系名稱
        return self._major

    def set_major(self,value):#設定科系名稱
        self._major=value

    def get_departmentChairName(self): #取得系主任姓名
        return self._departmentChairName

    def set_departmentChairName(self,value):#設定系主任姓名
        self._departmentChairName=value

    def get_studentName(self): #取得學生姓名
        return self._studentName

    def set_studentName(self,value):#設定學生姓名
        self._studentName=value

    def get_studentID(self): #取得學生學號(ID)
        return self._studentID

    def set_studentID(self,value):#設定學生學號(ID)
        self._studentID=value

    def get_grade(self): #取得年級
        return self._grade

    def set_grade(self,value):#設定年級
        self._grade=value

    def get_getCredit(self): #取得取得學分
        return self._getCredit

    def set_getCredit(self,value):#設定取得學分
        self._getCredit=value

    def get_gradesGPA(self): #取得成績GPA
        return self._gradesGPA

    def set_gradesGPA(self,value):#設定成績GPA
        self._gradesGPA=value

    def get_studentAddress(self): #取得學生地址
        return self._studentAddress

    def set_studentAddress(self,value):#設定學生地址
        self._studentAddress=value

    
    



st1=Student("CSIE","Horng","LU D D","4A9G0105",4,123,3,"台中17號")

print(st1.get_schoolName())
print(st1.get_schoolAddress())
print(st1.get_major())
print(st1.get_departmentChairName())
print(st1.get_studentName())
print(st1.get_studentID())
print(st1.get_grade())
print(st1.get_getCredit())
print(st1.get_gradesGPA())
print(st1.get_studentAddress())
