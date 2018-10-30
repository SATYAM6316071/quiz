import random
import termcolor
from termcolor import colored
print(colored("*******************************","green"))
print(colored("*******************************","green"))
print(colored("************HANGMAN************",'blue'))
print(colored("*******************************","green"))
print(colored("*******************************","green"))
name=input(colored("ENTER THE NAME TO PLAY HANGMAN: ",'blue'))      #user name
print(colored("Hi {} welcome to HANGMAN".format(name),'red'))
print(colored("Enter 1 for play easy leval HANGMAN","yellow"))
print(colored("Enter 2 for play hard leval HANGMAN",'yellow'))
choice=int(input(colored('Enter the choice:','blue')))
if choice!=1 and choice!=2:
    print("Wrong input")
    exit(0)
main_list=['MOVIE','FRUIT','PROGRAMMING_LANGUAGE']#Main list for shuffle
random.shuffle(main_list)
if main_list[0]=='FRUIT':
    fruit=['APPLE','MANGO','GUAVA','LITCHI','BANANA','ORANGE','COCONUT','BLACKPLUM',]#fruit list for shuffle
    random.shuffle(fruit)
    answer=fruit[1]                 #for printing the answer which is not guess by user
    compiler_answer=list(answer)    #answer for compiler
    print(colored("Guess the name of fruit:","green"))
elif main_list[0]=='MOVIE':
    movie=['RACE3', 'BAGHI2','RAID','PARI','PARMANU','PADMAN','PADMAVAT']
    random.shuffle(movie)
    answer = movie[1]               #for printing the answer which is not guess by user
    compiler_answer = list(answer)
    print(colored("Guess the name of movie(relise 2018):","magenta"))
elif main_list[0]=='PROGRAMMING_LANGUAGE':
    programming_language = ['ANDROID', 'C++', 'JAVA', 'PYTHON', 'SHIFT','JAVASCRIPT','PHP','HTML','KOTLIN','JSON','AJAX']
    random.shuffle(programming_language)
    answer = programming_language[1]            #for printing the answer which is not guess by user
    compiler_answer = list(answer)
    print(colored("Guess the name of programming_language:","blue"))

display=[]
display.extend(compiler_answer)
ex_it=1
count=0
if choice==1:
    for i in range(len(display)):
        display[i]=" - "
    q = []                      #for mixing the index position
    for i in range(len(compiler_answer)):
        q.append(i)
    random.shuffle(q)
    a = q[0]
    guess=compiler_answer[a]
    guess = guess.upper()
    for i in range(len(compiler_answer)):
        if compiler_answer[i] == guess:
            display[i] = guess
            count+=1
            ex_it+=1
    print(colored("".join(display),"blue"))
    print('\n')
elif choice==2:
    for i in range(len(display)):
        display[i]=" - "                            #for printing the -
    print(colored(''.join(display),'blue'))
    print("\n")

while count<len(compiler_answer):
    if ex_it<=10:
        ex_it+=1
        guess=input(colored("Guess a letter: ",'yellow'))
        guess=guess.upper()
        for i in range(len(compiler_answer)):
            if compiler_answer[i]==guess:           #insertion
                display[i]=Guess
                count+=1
        print(colored("".join(display),"blue"))
        print("\n")
    else:
        print(colored("Hi {} you loose the game".format(name),'red'))       #loose msg
        print(colored("Play next time !","red"))
        print(colored("The answer was: {}".format(answer),'green'))
        exit(0)
print(colored("Hi {} you guess the word sucessfully".format(name),'green')) #win msg
print(colored("You won the match",'green'))




