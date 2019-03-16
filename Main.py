from Tkinter import *
from Scheduler import Scheduler
from ScheduleItem import *

scheduler = Scheduler()

window = Tk()
window.title("Welcome")
window.geometry('700x700')

lbl1 = Label(window, text="Tasks")
lbl1.grid(column=0, row=1)

txt = Entry(window, width=10)
txt.grid(column=0, row=2)

opvar = StringVar(window)
op1 = OptionMenu(window, opvar, *scheduler.getCategories())
op1.grid(column=1, row=2)

min1 = Entry(window, width=5)
min1.grid(column=2, row=2)

scheduleitems = []

newTaskRowNum = 2
#these track the columns
taskList = []
category = []
durations = []
editButtons = []

flag = False
flag2 = False

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
    print(newTaskRowNum)
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

    s = ScheduleItem(txt.get(), opvar.get(), min1.get())
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

    editMin = Entry(window, width=5)
    editMin.insert(0, durations[num].cget("text"))
    durations[num].grid_forget()
    durations[num] = editMin
    editMin.grid(column=2, row=(num+2))

    editButtons[num].grid_forget()
    editButtons[num] = Button(window, text="Save Task", command=lambda:saveTask(num))
    editButtons[num].grid(column=4, row=(num+2))

def saveTask(num):
    saveTask = Label(window, text=taskList[num].get(), width=10)
    taskList[num].grid_forget()
    saveTask.grid(column=0, row=(num+2))
    taskList[num] = saveTask

    saveOp = Label(window, text=opvar.get())
    category[num].grid_forget()
    saveOp.grid(column=1, row=(num+2))
    category[num] = saveOp

    saveMin = Label(window, text=durations[num].get(), width=5)
    durations[num].grid_forget()
    saveMin.grid(column=2, row=(num+2))
    durations[num] = saveMin

    editButtons[num].grid_forget()
    editButtons[num] = Button(window, text="Edit Task", command=lambda:editTask(num))
    editButtons[num].grid(column=4, row=(num+2))

def start():
    global scheduleitems
    s = Scheduler()
    s.cycle(scheduleitems[0])


btn = Button(window, text="Add Task", command=addTask)
btn.grid(column=3, row=2)
btn2 = Button(window, text="Start", command=start)
btn2.grid(column=3, row=4)
btn4 = Button(window, text="End")
btn4.grid(column=3, row=5)
window.mainloop()
