import pymysql

    
def menu():
    print("Employee Attendence Management")
    print("------------------------------")
    print("1.Admin")
    print("2.Employee")
    print("3.Exit")
    return(int(input("Enter your choice")))

   
        
    
def insert_emp():
    conn = pymysql.connect('localhost','root','mysql123','employee_leave')
    cursor = conn.cursor()
    Emp_name = input("Enter Employee Name :")
    Desg = input("Enter Employee Designation :")
    no_of_leaves= int(input("Enter the total number of working days left :"))
    args = [Emp_name,Desg,no_of_leaves]
    sql = """insert into employee(Employee_Name,Designation,No_of_leaves)values(%s,%s,%s)"""
    cursor.execute(sql,args)
    pp = """select * from employee"""
    cursor.execute(pp)
    print("Data Entered Successfully")
    conn.commit()
    conn.close()
    return menu2()
        
def leave_dea():
    conn = pymysql.connect('localhost','root','mysql123','leavedetails')
    cursor = conn.cursor()
    Emp_id = input("Enter Employee ID :")
    print("Your Eligible For applying for a leave")
    reason = input("What is the reason for Taking a leave")
    tol = input("What type of leave do you wish for")
    num = int(input("How many days of leave do you wish for"))
    args = [Emp_id,reason,tol,num]
    sql = """insert into leavdetails(Employee_Id,Reason,Type_of_leave,No_of_Days)values(%s,%s,%s,%s)"""
    cursor.execute(sql,args)
    pp = """select * from leavdetails"""
    cursor.execute(pp)
    print("Data Entered Successfully")
    conn.commit()
    conn.close()
    return menu()  

def view_empdetails():
    conn = pymysql.connect('localhost','root','mysql123','employee_leave')
    cursor = conn.cursor()
    viw = """select * from employee"""
    cursor.execute(viw)
    for Employee_id,Employee_Name,Designation,No_of_leaves in cursor.fetchall():
        print('-'*50)
        print(Employee_id)
        print(Employee_Name)
        print(Designation)
        print(No_of_leaves)
        print('-'*50)
    conn.commit()
    conn.close()
    return menu2()

def view_leavedetails():
        conn = pymysql.connect('localhost','root','mysql123','leavedetails')
        cursor = conn.cursor()
        viw = """select Employee_id,reason,Type_of_leave,No_of_Days from leavdetails"""
        cursor.execute(viw)
        for Employee_id,reason,Type_of_leave,No_of_Days in cursor.fetchall():
            print('-'*50)
            print(Employee_id)
            print(reason)
            print(Type_of_leave)
            print(No_of_Days)
            print('-'*50)
        conn.commit()
        conn.close()
        return menu()

def up_name():
    conn = pymysql.connect('localhost','root','mysql123','employee_leave')
    cursor = conn.cursor()
    eid = input("Enter the Employee Id")
    enam = input("Enter the name of the employee you want to update:")
    sid = """select * from employee where Employee_Id={}""".format(eid)
    up = """update employee SET Employee_name = %s WHERE Employee_id = %s"""
    data = (enam,eid)
    cursor.execute(up,data)
    print("Update Successful")
    conn.commit()
    conn.close()
    return menu2()
   

def menu2():
    print("ADMIN")
    print("1.Insert a new employee")
    print("2.View employee")
    print("3.View Leave Details")
    print("4.Update")
    print("5.Exit")
    choice = int(input("Enter your choice"))

    while 1:
        if choice == 1:insert_emp()
        elif choice == 2:view_empdetails()
        elif choice == 3:view_leavedetails()
        elif choice == 4:up_name() 
        elif choice == 5: exit(0)
        else: print("Invalid Choice")

while 1:
    choice = menu()
    if choice == 1: menu2()
    elif choice == 2:
        print("Employee")
        print("--------")
        print("1.View employee")
        print("2.Apply for Leave")
        print("3.Exit")
        ch = (int(input("Enter your choice")))
        if ch == 1:
            view()
        elif ch==2:
            leave_dea()
        else:exit(0)    
    elif choice == 3: exit(0)
    else : print("Invalid Choice")


    
    
