class InvalidChoice(Exception):
    pass

tasks=[]
status=[]

def choice_check(num):
    if num<1 or num>5:
        raise InvalidChoice("choice must be between 1 to 5! try again!")
    else:
        return 1

def get_data():# this function will only work once to link the lists in the program to the data file
    global tasks,status
    counter=0
    with open('Todo_List.txt','r') as List:
        data=List.readlines() #this will get each line as an element of the list data
    
    while counter<len(data):
        curr_data=data[counter] #this will store the current line in curr_data
        status_index=curr_data.find('Complete')
        if(status_index!=-1):#this means that the status is found
            tasks.append(curr_data[:status_index].rstrip(" "))#to remove whitespace from right side
            status.append(curr_data[status_index:].strip()) #.strip to remove \n
            counter+=1
        else:
           status_index=curr_data.find('Pending')
           tasks.append(curr_data[:status_index].rstrip(" "))#to remove whitespace from right side
           status.append(curr_data[status_index:].strip()) #.strip to remove \n
           counter+=1

def file_handle():
    global tasks,status
    max_len = 0

    for task in tasks:
        if len(task)>max_len:
            max_len=len(task)
    with open('Todo_List.txt','w') as Tasks:
        counter=0
        task_adjust = 0
        for task in tasks:
            task_adjust = task.ljust(max_len)  # because string is imutable
            Tasks.write(task_adjust+" "*10+status[counter]+'\n')
            counter+=1

def add_task(task_name,task_status):
    global tasks,status
    tasks.append(task_name)
    status.append(task_status)
    file_handle()

def delete_task(task_name):
    global tasks,status
    counter=0
    found = 0
    for task in tasks:
        if(task_name==task):
            del tasks[counter] #deletes the element with the given index
            del status[counter]
            file_handle()
            found=1
            print("Task Deleted")
            break
        counter+=1
    if (found==0):
        print("Task not found")

def update_task(task_name,new_status):
    global tasks, status
    counter = 0
    found = 0
    for task in tasks:
        if (task_name == task):
            status[counter]=new_status
            file_handle()
            print("Task Updated")
            found=1
            break
        counter += 1
    if (found == 0):
        print("Task not found")

def view_list():
    global tasks, status
    max_len = 0
    counter = 0
    for task in tasks:
        if len(task) > max_len:
            max_len = len(task)
    for task in tasks:
        print(task.ljust(max_len) + (" " * 10) + status[counter])
        counter += 1

def todo_list():
    print("Welcome to your To-Do List")
    get_data()
    while (True):
        choice=int(input("1. to add a Task press (1)"
        "\n2. to delete a Task press (2)"
        "\n3. to update a task status (Complete or Pending) press (3)\n4.to view the todo list press (4)"
                     "\n5. to exit press (5)\n:  "))
        choice_check(choice)


        if(choice==1):
            task_name=input("Enter task name: ")
            task_status=input("Enter task status: ")
            add_task(task_name,task_status)
        elif(choice==2):
            task_name = input("Enter task name: ")
            delete_task(task_name)
        elif(choice==3):
            task_name = input("Enter task name: ")
            task_status=input("Enter task status: ")
            update_task(task_name,task_status)
        elif choice==4:
            view_list()
        elif choice==5:
            print("thanks for using the program")
            break






try:
    todo_list()
except InvalidChoice as e:
    print(e)