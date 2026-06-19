import csv 
import json

def load_data(filename):
    Student_data =[]
    Student_info ={}
    with open(filename, "r") as f:
        data = csv.reader(f)
        # print(data)
        for user in data :
            Student_info["Timestamp"] = user[0]           
            Student_info["Total score"] = user[1]           
            Student_info["Name"] = user[2]           
            Student_info["Name [Score]"] = user[3]           
            Student_info["Name [Feedback]"] = user[4]           
            Student_info["Email"] = user[5]           
            Student_info["Email [Score]"] = user[6]           
            Student_info["Email [Feedback]"] = user[7]   
            Student_data.append(Student_info)
    return Student_data
    with open("Student_data2.json","w",encoding='utf-8') as file:
         json.dump(res, file, indent=4)       
data = load_data("Quiz 2_16_6_26.csv")
print(data)