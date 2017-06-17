def Input():
    while True:
        print("Enter - 1 if you want to input test question\n"
              "Enter - 2 if you want to input exact question\n"
              "Enter - 0 if you want to end")
        type_question = int(input("Enter number of type of question: "))
        if type_question == 1: #test question
            question = input("Enter the question -> ")
        elif type_question == 2: #exact question
            print('2')
        else: #finish th
            print('0')


print(Input())
