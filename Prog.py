def Input():
    dict = {}
    while True:
        print("Enter - 1 if you want to input test question\n"
              "Enter - 2 if you want to input exact question\n"
              "Enter - 0 if you want to end")
        type_question = int(input("Enter number of type of question: "))
        if type_question == 1:  # test question
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
        elif type_question == 2:  # exact question
            question = input("Enter the question -> ")
            answer = input("Enter the answer -> ")
            dict[question] = answer
        else:  # finishing of input
            break

    print('work')
    return dict


print(Input())
