import csv

def write_csv(info_list):
    with open('C:/Users/DELL/Desktop/My_Cap_Python_Program/student_info.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name","Age","Contect Number","Email ID"])

        writer.writerow(info_list)


if __name__ == '__main__':
    condition=True
    num = 1
    
    while(condition):
        name=input("Enter Name of Student:")
        age=int(input("Enter Your Age:"))
        contect_number=int(input("Enter your contect number:"))
        email_id=input("Enter your Email ID:")

        student_info=[name,age,contect_number,email_id]

        print("\nName:",name,"\nAge:",age,"\nContect Number:",contect_number,"\nEmail ID:",email_id)

        check=input("Is the information is correct (yes/no):")

        if check == 'yes':
            write_csv(student_info)
            
            a=input("\nDo you want to enter the information of more students (yes/no):")
            if a=='yes':
                condition=True
                num=num+1
            elif a=='no':
                condition=False

        elif check == 'no':
            print("Please re write the information.")
