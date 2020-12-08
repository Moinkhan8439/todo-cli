from utility import getQuote,getLine,exit,getDate,validate
from todo import Todo
import os
from datetime import datetime
import time

def loadMenu():
    os.system('clear')
    choice=0
    while(1):
        print("What do you want to do")
        print("1. Add a new task")
        print("2. Login to a different date")
        print("3. Update an exisiting task")
        print("4. Remove an exisiting task")
        print("5. Go back to dashboard")
        print("0. Exit")
        choice=int(input())
        if(choice not in {0,1,2,3,4,5}):
            choice=int(input())
        else:
            break
    if(choice==0):
            exit()
    elif(choice==1):
        loadAdd(todo)
    elif(choice==2):
        loadView(todo)
    elif(choice==3):
        loadUpdate(todo)
    elif(choice==4):
        loadRemove(todo)
    loadDashboardTodo()

def loadDashboardCommon(state,arrow,press):
    os.system('clear')
    while(1):
        todo.state="dashboard"
        print("{0:>40}".format(getDate()))
        print("Welcome to Todo List Here is the quote of the day")
        print(todo.getQuote())
        print()
        print("Task schedule for today is\n")
        getLine()
        print("\n{0:>18}\n".format(state))
        getLine()
        print("\n\n{0:>15}\n".format(arrow))
        print("")
        print("To see Upcoming Press {press}".format(press=press))
        print("To go to menu, Enter 1")
        print("To exit press 0")
        return input()


def loadDashboardTodo():
    c=loadDashboardCommon("ToDo","→","d or D")
    try:
        if(c=="d" or c=="D"):
            loadDashboardCompleted()
        elif(int(c)==1):
            loadMenu()
        else:
            exit()
    except ValueError:
        loadDashboardTodo()

def loadDashboardCompleted():
    c=loadDashboardCommon("Completed","←","a or A")
    try:
        if(c=="a" or c=="A"):
            loadDashboardTodo()
        elif(int(c)==1):
            loadMenu()
        else:
            exit()
    except ValueError:
        loadDashboardCompleted()

def loadWelcome():
    print("1.Create a New TODO List")
    print("2.Load an exisiting TODO List")
    return int(input())

def newDoc(todo):
    os.system('clear') 
    name=input("Enter the name of your new todolist:\n")
    while(os.path.exists(name)):
        print("A file with the same name exist choose another name")
        name=input("Enter the name of your new todolist:\n")
    todo.setFile(name)
    os.system('clear') 

#def loadTasks(todo,name):



def loadFile(todo):
    os.system('clear')
    name=input("Enter the name of an existing file\n")
    while((not (os.path.exists(name))) or (name.split('.')[-1] != "todo")):
        if((name.split('.')[-1] != "todo")):
            print("The file has an invalid extension it should have a .todo extension")
        else:
            print("The file doesn't exist please enter the name of an existing file")
        name=input("Enter the name of an existing Todo File\n")   
    todo.file=name
    #loadTasks(todo,name)
    os.system('clear') 

def loadAdd(todo):
    os.system('clear')
    name=""
    description=""
    date=""
    while(name==""):
        print("Enter the name of the task")
        name=input()
        if name=="":
            print("Task name can't be empty")
    description=input("Enter the Description of the task (Optional, Default:Empty): ")
    while(True):
        date=input("Enter the date of the task (Optional, Default:Today's Date): ")
        date=validate(date)
        if(date is not None):
            break
        else:
            print("Date entered in wrong format please enter in the format dd-mm-yyyy")
    priority=""
    while((not (priority.isnumeric()) ) or (not (1<=int(priority)<=10))):
        priority=input("Enter the prioirty of the task (Optional, Default:1): ")
        if(priority==""):
            break
    if(date==""):
        date=datetime.today().strftime("%d-%m-%y")
    if(todo.tasks.get(date) is None):
        todo.tasks[date]=[]
    todo.createTask(name,description,priority,date)
    print("Task Added successfully")
    time.sleep(1)


def login():
    while(True):
        print("Date to Login ( Format dd-mm-yyyy): ")
        date=input()
        date=validate(date)
        if(date is not None):
            return date
        else:
            print("Date format is not correct")


def viewtask(todo,date):
    print("The task for the date {} are".format(date))
    for index,task in enumerate(todo.tasks[date]):
        print(index+1,task.getTitle())
    time.sleep(2)



def loadView(todo):
    date=login()
    todo.setDate(date)
    loadDashboardTodo()

def loadUpdate(todo):
    todo.date

def loadRemove(todo):
    todo.date



if __name__=="__main__":
    todo=Todo()
    answer=loadWelcome()
    todo.setQuote(getQuote())
    todo.setState("welcome")
    if(answer==1): ##Create a new todolist
        newDoc(todo)        
    else: ##Load a new todolist
        loadFile(todo)
    loadDashboardTodo()
    
    