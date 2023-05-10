print("Welcome, this is khalid's and russel's project for IT II, our project is a quiz which tests user's on their knowlege of our school, GEMS, would you like to begin?")
print("")
start = input("type yes if you would like to begin the quiz: ")

def question_1():
    print("When was our school founded?")
def question_2():
    print("Who is the current head of our school?")
def question_3():
    print("Who originally founded the Gems corporation")
def question_4():
    print("In which city was the first Gems school built?")
def question_5():
    print("What does GEMS stand for?")
def question_6():
    print("How many different nationalities of students are there in GEMS")
def question_7():
    print("What curriculum does our school follow?")
def question_8():
    print("What is our schools mascot name?")
def question_9():
    print("Which street is our school on?")
def question_10():
    print("What does AAQ stand for?")

if start == "yes":
    question_1()
    answer_here_1 = input("Enter Answer: ")
    if answer_here_1 == "2014":
        print("Correct!")
    else:
        print("Incorrect, GEMS AAQ was established in 2014")

    next = input("type yes if you would like to continue the quiz: ")
    if next == "yes":
        question_2()
        answer_here_2 = input("Enter Answer: ")
        if answer_here_2 == "Mark Lentz":
            print("Correct")
        else:
            print("Incorrect, the current head of GEMS AAQ is Mark Lentz")
    
    next = input("type yes if you would like to continue the quiz: ")
    if next == "yes":
        question_3()
        answer_here_3 = input("Enter Answer: ")
        if answer_here_3 == "Sunny Varkey":
            print("Correct")
        else:
            print("Incorrect, the original founder of the GEMS corporation is Sunny Varkey")

    next = input("type yes if you would like to continue the quiz: ")
    if next == "yes":
        question_4()
        answer_here_4 = input("Enter Answer: ")
        if answer_here_4 == "Dubai":
            print("Correct")
        else:
            print("Incorrect, the fist GEMS school was founded in Dubai")
            
     next = input("type yes if you would like to continue the quiz: ")
     if next == "yes":
         question_5()
         answer_here_5 = input("Enter Answer: ")
         if answer_here_5 == "Global Education Management System":
             print("Correct")
         else:
             print("Incorrect, GEMS stands for Global Education Management System")
             
    next = input("type yes if you would like to continue the quiz: ")
     if next == "yes":
         question_6()
         answer_here_6 = input("Enter Answer: ")
         if answer_here_6 == "80+":
             print("Correct")
         else:
             print("Incorrect, ")
             
    next = input("type yes if you would like to continue the quiz: ")
     if next == "yes":
         question_7()
         answer_here_7 = input("Enter Answer: ")
         if answer_here_7 == "american":
             print("Correct")
         else:
             print("Incorrect, ")
             
    next = input("type yes if you would like to continue the quiz: ")
     if next == "yes":
         question_8()
         answer_here_8 = input("Enter Answer: ")
         if answer_here_8 == "raptors":
             print("Correct")
         else:
             print("Incorrect, ")
             
    next = input("type yes if you would like to continue the quiz: ")
     if next == "yes":
         question_9()
         answer_here_9 = input("Enter Answer: ")
         if answer_here_9 == "Mian street":
             print("Correct")
         else:
             print("Incorrect, ")
             
    next = input("type yes if you would like to continue the quiz: ")
     if next == "yes":
         question_10()
         answer_here_10 = input("Enter Answer: ")
         if answer_here_10 == "American Academy Qatar":
             print("Correct")
         else:
             print("Incorrect, ")
