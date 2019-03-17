from Tkinter import *
#from Tkinter import messagebox
from Scheduler import Scheduler
from ScheduleItem import *
import threading
import boto3
import json

def updateFromDatabase():
    dynamodb=boto3.resource('dynamodb',aws_access_key_id='AKIAJMEYIZVMTHDEJORQ',aws_secret_access_key='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',region_name='us-east-1')
    table = dynamodb.Table('blairfinalfinaltable')
    data = table.scan()["Items"]
    for task in data:
        addItemFromDatabase(task["activityName"], task["duration"])
        newTaskRowNum += 1
        lbl2 = Label(window, text=task["activityName"])
        taskList.append(lbl2)
        lbl2.grid(column=0, row=newTaskRowNum)

        op2 = Label(window, text=opvar.set(1))
        category.append(op2)
        op2.grid(column=1, row=newTaskRowNum)

        min2 = Label(window, text=task["duration"])
        durations.append(min2)
        min2.grid(column=2, row=newTaskRowNum)


scheduler = Scheduler()

window = Tk()
window.title("Welcome")
window.geometry('700x700')

lbl1 = Label(window, text="Tasks")
lbl1.grid(column=0, row=1)

lbl3 = Label(window, text="Category")
lbl3.grid(column=1, row=1)

lbl4 = Label(window, text="Minutes")
lbl4.grid(column=2, row=1)

txt = Entry(window, width=10)
txt.grid(column=0, row=2)

opvar = StringVar(window)
op1 = OptionMenu(window, opvar, *scheduler.getCategories())
op1.grid(column=1, row=2)

min1 = Entry(window, width=10)
min1.grid(column=2, row=2)

scheduleitems = []

newTaskRowNum = 2
#these track the columns
taskList = []
category = []
durations = []
editButtons = []

flag = False

def addItemFromDatabase(name, duration):
	scheduleitems.append(ScheduleItem(name, "Homework", duration))

def addTask():
    global newTaskRowNum
    global txt
    global op1
    global min1
    global btn
    global opvar
    index = len(editButtons)
    lbl2 = Label(window, text=txt.get())
    taskList.append(lbl2)
    lbl2.grid(column=0, row=newTaskRowNum)
    #print(newTaskRowNum)
    #op2 = OptionMenu(window, opvar, *scheduler.getCategories())
    op2 = Label(window, text=opvar.get())
    category.append(op2)
    op2.grid(column=1, row=newTaskRowNum)
    #min2 = Entry(window, width=10)
    min2 = Label(window, text=min1.get())
    durations.append(min2)
    min2.grid(column=2, row=newTaskRowNum)

    btn2 = Button(window, text="Edit Task", command=lambda:editTask(index))
    editButtons.append(btn2)
    btn2.grid(column=4, row=newTaskRowNum)

    s = ScheduleItem(txt.get(), opvar.get(), int(min1.get()))
    scheduleitems.append(s)

    txt.delete(0, len(txt.get()))
    opvar.set("")
    min1.delete(0, len(min1.get()))
    #print(taskList)

    newTaskRowNum += 1
    #print(newTaskRowNum)
    txt.grid(column=0, row=newTaskRowNum)
    op1.grid(column=1, row=newTaskRowNum)
    min1.grid(column=2, row=newTaskRowNum)
    btn.grid(column=4, row=newTaskRowNum)

def editTask(num):
    #print(taskList[num].cget("text"))
    editTxt = Entry(window, width=10)
    editTxt.insert(0, taskList[num].cget("text"))
    taskList[num].grid_forget()
    taskList[num] = editTxt
    editTxt.grid(column=0, row=(num+2))

    ao = opvar.get()
    editOp = OptionMenu(window, opvar, *scheduler.getCategories())
    opvar.set(ao)
    category[num].grid_forget()
    category[num] = editOp
    editOp.grid(column=1, row=(num+2))

    editMin = Entry(window, )
    editMin.insert(0, durations[num].cget("text"))
    durations[num].grid_forget()
    durations[num] = editMin
    editMin.grid(column=2, row=(num+2))

    editButtons[num].grid_forget()
    editButtons[num] = Button(window, text="Save Task", command=lambda:saveTask(num))
    editButtons[num].grid(column=4, row=(num+2))

def saveTask(num):
    if(durations[num].get().isdigit()):
        saveTask = Label(window, text=taskList[num].get(), width=10)
        taskList[num].grid_forget()
        saveTask.grid(column=0, row=(num+2))
        taskList[num] = saveTask

        saveOp = Label(window, text=opvar.get())
        category[num].grid_forget()
        saveOp.grid(column=1, row=(num+2))
        category[num] = saveOp

        saveMin = Label(window, text=durations[num].get(), width=10)
        durations[num].grid_forget()
        saveMin.grid(column=2, row=(num+2))
        durations[num] = saveMin

        editButtons[num].grid_forget()
        editButtons[num] = Button(window, text="Edit Task", command=lambda:editTask(num))
        editButtons[num].grid(column=4, row=(num+2))
    else:
        print(durations[num].get())
        messagebox.showerror("Error!", "Please enter a number for the duration.")


flag = False

def start():
    flag = False
    global scheduleitems
    s = Scheduler()
    for a in scheduleitems:
        print(a.getDuration())
        if not flag:
            s.cycle(a)
            print("done")

def end():
    flag = True

btn = Button(window, text="Add Task", command=addTask)
btn.grid(column=4, row=2)
btn2 = Button(window, text="Start", command=start)
btn2.grid(column=6, row=2)
btn4 = Button(window, text="End", command=end)
btn4.grid(column=6, row=3)
btn4 = Button(window, text="Quit", command=window.destroy)
btn4.grid(column=6, row=4)
updateFromDatabase()

print(scheduleitems)
window.mainloop()
