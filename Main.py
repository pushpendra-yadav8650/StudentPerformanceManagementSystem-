import csv 
import json

print("Automated Training Performance Management System")
#This function for upload Student quiz CSV the file 
Student_data =[]
def load_data(filename):
    with open(filename, "r") as f:
        data = csv.reader(f)
        for user in data :
            Student_info = {
                "Timestamp": user[0] ,          
                "Total score": user[1],          
                "Name" : user[2],           
                "Name [Score]" : user[3],           
                "Name [Feedback]" : user[4] ,          
                "Email" :user[5] ,          
                "Email [Score]" : user[6]  ,         
                "Email [Feedback]" : user[7]  
             }    
            Student_data.append(Student_info)
    return Student_data
    # print(Student_data)
    # res = Student_data
    with open("Student_data78.json","w",encoding='utf-8') as file:
         json.dump(res, file, indent=4)       
data = load_data("Quiz 2_16_6_26.csv")
# print(data)
#read the json file from the folder for calculate percentage 
def Student_per(filename):
    with open(filename, "r", encoding='utf-8')as f:
       res = json.load(f)
    return res
resdata = Student_per("Student_data78.json")
#This function calcualte the Student marks total marks and Percentage 
def Calculater_per(resdata):
    studet_sum =0
    total_out_of = 0
    for user in resdata:
        res =  user["Total score"].split('/')[0].strip()
        newres = int(float(res))
        total = int(user["Total score"][7:10])
        total_out_of+=total
        studet_sum+= newres
    student_per = studet_sum/int(total_out_of) * 100
    print(f"student total marks {studet_sum}")
    print(f"student average marks {student_per:.2f} % ")
Calculater_per(resdata) #call the function 
# print(count)
student_module_data = []
def Student_Module(resdata):
    for student in resdata:
        marks = int(float( student["Total score"].split('/')[0].strip()))
        total = int(student["Total score"][7:10])
        percentage = round(marks/total *100,2)
        if  percentage >= 90 :
            performance = "Excelent"
        elif percentage >= 75:
            performance = "Good"
        elif percentage >= 60:
            performance = "Average"
        else:
            performance = "Weak"
        studentdata={
           
           "Name":student["Name"],
           "Total score":int(float( student["Total score"].split('/')[0].strip())),
           "percentage":percentage,
           "Performance" : performance
       } 
        student_module_data.append(studentdata)
    
    for std in student_module_data:
        print(f" Student name is {std["Name"]}\n Student Score = {std["Total score"]}\n Student Percentage = {std["percentage"]}%,\n Student Performance = {std["Performance"]}\n")
Student_Module(resdata)
        

