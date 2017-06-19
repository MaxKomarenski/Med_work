from tkinter import *
import json


class Med_prog():
    def __init__(self):
        self.main_dict = {}
        self.but_type_test = Button(root,
                               text="Test question",
                               width=30, height=5,
                               bg='white', fg='blue')
        self.but_type_exact = Button(root,
                                text="Exact question",
                                width=30, height=5,
                                bg='white', fg='blue')
        self.but_finish = Button(root,
                            text="End",
                            width=30, height=5,
                            bg='white', fg='blue')

        self.lab = Label(root,
                    text="Please, choose type of question",
                    font="Arial 12")

        self.lab.pack()

        self.but_type_test.pack(side='left')
        self.but_finish.pack(side='right')
        self.but_type_exact.pack(side='bottom')

        self.but_type_test.bind("<Button-1>", self.test_question)
        self.but_type_exact.bind("<Button-1>", self.exact_question)
        self.but_finish.bind("<Button-1>", self.end)

    def test_question(self, event):
        # test question
        window = Toplevel(root)
        question = input("Enter the question -> ")
        lst_answer = []
        print("Now you're writing 3 answers and only one of them is true.\n"
              "When you write a true answer, please put # before the answer.\n"
              "Example -> #People have two arms")
        print("-----------------------")
        for i in range(3):
            answer = input("Enter the answer -> ")
            lst_answer.append(answer)
        self.main_dict[question] = lst_answer

    def exact_question(self, event):
        # exact question
        question = input("Enter the question -> ")
        answer = input("Enter the answer -> ")
        self.main_dict[question] = answer

    def end(self, event):
        print(self.main_dict)
        json.dump(self.main_dict, open("test.json", "w"))


root = Tk()
root.title('Root')
obj = Med_prog()

root.mainloop()
