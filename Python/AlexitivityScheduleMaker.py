from tkinter import *
window = Tk()
window.title("Welcome to Alexitivity")
window.geometry('700x700')
# rowxcolumn

lbl1 = Label(window, text="Tasks")
lbl1.grid(column=1, row=0)

txt = Entry(window, width=10)
txt.grid(column=0, row=1)

newTaskRowNum = 2
taskList = []
editButtons = []

def addTask():
    global newTaskRowNum
    global txt
    global btn
    index = len(editButtons)
    lbl2 = Label(window, text=txt.get())
    btn2 = Button(window, text="Edit Task", command=lambda:editTask(index))
    btn2.grid(column=2, row=newTaskRowNum)
    txt.delete(0, len(txt.get()))
    taskList.append(lbl2)
    print(taskList)
    lbl2.grid(column=0, row=newTaskRowNum)
    
    newTaskRowNum += 1
    print(newTaskRowNum)
    txt.grid(column=0, row=newTaskRowNum)
    btn.grid(column=2, row=newTaskRowNum)

def editTask(num):
    taskList[num].grid_forget()
    editTxt = Entry(window, width=10)
    editTxt.grid(column=0, row=num + 1)
    

btn = Button(window, text="Add Task", command = addTask)
btn.grid(column=3, row=1)
window.mainloop()