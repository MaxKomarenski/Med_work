dict = {}
def Input():
    while True:
        print("Enter - 1 if you want to input test question\n"
              "Enter - 2 if you want to input exact question\n"
              "Enter - 0 if you want to end")
        type_question = int(input("Enter number of type of question: "))
        if type_question == 1: #test question
            question = input("Enter the question -> ")
            lst_answer = []
            for i in range(3):
                answer = input("Enter the answer. If answer is true, write before this '#'\n"
                               "Example -> #How many arms people have ?")
                lst_answer.append(answer)
            dict[question] = lst_answer
            print(dict)
        elif type_question == 2: #exact question
            question = input("Enter the question -> ")
            answer = input("Enter the answer -> ")
            dict[question] = answer
            print(dict)
        else: #finishing of input
            break

    print('work')
    return dict


print(Input())
