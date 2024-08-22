import time # Imports time to be used later in the code
import os # Imports os to be used later in the code

# The questions, options to awnser and awnsers for the quiz all put in lists
questions = [1,"Who possesses the ring of power at the start of the trilogy?",2,"Who do the hobbits encounter at the Prancing Pony?",3,"How many members make up the fellowship of the ring?",4,"What is the name of the elf in the fellowship?",5,"What is the name of the dwarf in the fellowship?",6,"Who is the first member of the fellowship to be separated from the group?"]
options = [1,"A. Bilbo B. John C. Dumbledoor D. Humblemoore E. stewie griffin",2,"A. The manager of the store B. Their cousin C. A prancing pony D. Legoland E. Strider",3,"A. 1.5 B. 10 C. enough D. 9 E. 7",4,"A. Buddy B. Legolas C. Jolly D. Bernard E. Aegnor",5,"A. Peter Dinklage B.Tommy Morrison C. Gimli D. Balin E. Dwalin",6,"A. Gandalf B. Jerry the stone C. The ring D. Frodo E. Aragorn"]
awnsers = [1,"A",2,"E",3,"D",4,"B",5,"C",6,"A"]

def question1(): # This function controls the first 
    print(questions[1])
    print('')
    print(options[1])
    print('')
    Q1 = input('Your awnser: ')
    if Q1 == 'A' or 'Bilbo':
        print('Correct')
    else:
        print('Incorrect, the awnser was', awnsers[1])
    time.sleep(4)
    os.system('clear')
    question2()

def question2():
    print(questions[3])
    print('')
    print(options[3])
    print('')
    Q2 = input('your awnser: ')
    if Q2 == 'E' or 'Strider':
        print('Correct')
    else:
        print('Incorrect, the awnser was', awnsers[3])
    time.sleep(4)
    os.system('clear')
    question3()

def question3():
    print(questions[5])
    print('')
    print(options[5])
    print('')
    Q3 = input('your awnser: ')
    if Q3 == 'D' or '9':
        print('Correct')
    else:
        print('Incorrect, the awnser was', awnsers[5])
    time.sleep(4)
    os.system('clear')
    question4()

def question4():
    print(questions[7])
    print('')
    print(options[7])
    print('')
    Q4 = input('your awnser: ')
    if Q4 == 'B' or 'Legolas':
        print('Correct')
    else:
        print('Incorrect, the awnser was', awnsers[7])
    time.sleep(4)
    os.system('clear')
    question5()

def question5():
    print(questions[9])
    print('')
    print(options[9])
    print('')
    Q5 = input('your awnser: ')
    if Q5 == 'C' or 'Gimli':
        print('Correct')
    else:
        print('Incorrect, the awnser was', awnsers[9])
    time.sleep(4)
    os.system('clear')
    question6()

def question6():
    print(questions[11])
    print('')
    print(options[11])
    print('')
    Q6 = input('your awnser: ')
    if Q6 == 'A' or 'Gandalf':
        print('Correct')
    else:
        print('Incorrect, the awnser was', awnsers[11])
    time.sleep(4)
    os.system('clear')

def question7():
    print(questions[5])
    print('')
    print(options[5])
    print('')
    Q3 = input('your awnser: ')
    if Q3 == 'D' or '9':
        print('Correct')
    else:
        print('Incorrect, the awnser was', awnsers[5])
    time.sleep(4)
    os.system('clear')
    question4()

def question8():
    print(questions[7])
    print('')
    print(options[7])
    print('')
    Q4 = input('your awnser: ')
    if Q4 == 'B' or 'Legolas':
        print('Correct')
    else:
        print('Incorrect, the awnser was', awnsers[7])
    time.sleep(4)
    os.system('clear')
    question5()

def question9():
    print(questions[9])
    print('')
    print(options[9])
    print('')
    Q5 = input('your awnser: ')
    if Q5 == 'C' or 'Gimli':
        print('Correct')
    else:
        print('Incorrect, the awnser was', awnsers[9])
    time.sleep(4)
    os.system('clear')
    question6()

def question10():
    print(questions[11])
    print('')
    print(options[11])
    print('')
    Q6 = input('your awnser: ')
    if Q6 == 'A' or 'Gandalf':
        print('Correct')
    else:
        print('Incorrect, the awnser was', awnsers[11])
    time.sleep(4)
    os.system('clear')


print('Welcome to the lord of the rings quiz, this quiz will test you and your knowledge of the lord of the rings.')
time.sleep(3)
start = input('Type "the any key" to start: ')
print('')
if start == 'the any key':
    print('Good job, your are one of the people who read it right... thank you...')
    print('')
    time.sleep(3)
    print('Please awnser in caps... other than that lets begin')
    print('')
    time.sleep(3)
    os.system('clear')
    question1()
else:
    print('You should have typed "the any key".... your no fun...')
    print('')
    time.sleep(3)
    print('Oh well... please awnser in caps... other than that lets begin')
    print('')
    time.sleep(3)
    os.system('clear')
    question1()

