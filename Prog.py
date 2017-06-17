from tkinter import *


root = Tk()
but_type_test = Button(root,
                       text="Test question",
                       width=30, height=5,
                       bg='white', fg='blue')
but_type_exact = Button(root,
                        text="Exact question",
                        width=30, height=5,
                        bg='white', fg='blue')
but_finish = Button(root,
                    text="End",
                    width=30, height=5,
                    bg='white', fg='blue')

lab = Label(root,
                text="Please, choose type of question",
                font="Arial 10")

lab.pack()

but_type_test.pack(side='left')
but_finish.pack(side='right')
but_type_exact.pack(side='bottom')

dict = {}

def fun(event):
    # test question
    question = input("Enter the question -> ")
    lst_answer = []
    print("Now you're writing 3 answers and only one of them is true.\n"
              "When you write a true answer, please put # before the answer.\n"
              "Example -> #People have two arms")
    print("-----------------------")
    for i in range(3):
        answer = input("Enter the answer -> ")
        lst_answer.append(answer)
    dict[question] = lst_answer

def bun(event):
    # exact question
    question = input("Enter the question -> ")
    answer = input("Enter the answer -> ")
    dict[question] = answer

def ret(event):
    print(dict)

but_type_test.bind("<Button-1>", fun)
but_type_exact.bind("<Button-1>", bun)
but_finish.bind("<Button-1>", ret)

root.mainloop()

