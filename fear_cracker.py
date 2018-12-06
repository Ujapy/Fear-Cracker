from sys import exit, argv
script, fear_txt = argv
feartxt = open('fear_txt.txt')

user_name = input("Name:")
print("Nice meeting you %s" % user_name)

def welcome():
    print("FEAR and DREAM CRACKER")
    print("what is ur worst FEAR or what do u always DREAM about that scares you?\n Talk to me, but first tell me your name.")

    #user_name = input("Name:")

    start()
def start():
    print("%s are u having FEAR or a BAD DREAM? \n for fear input 'fear' and for dream input 'dream'" % user_name)
    inner_thought = input("fear or dream: ")

    if inner_thought == "fear":
        print("Ok, %s let's get you out of your fear" % user_name)
        fear()
    
    elif inner_thought == "dream":
        print("It's just a dream, %s, let's help you go over it" % user_name)
        dream()
    else:
        dead("I,m sorry u have to input 'fear' or 'dream' to access our services")
    
def dead(why):
    print(why,"...U are stronger than u think")
    exit(0)

def fear():
    print("Knowing your fear is a great step to overcoming it\nCan you be brief about your fear %s" % user_name)
    fear_input = input("Your fear please: ")
    if len(fear_input) > 10:
        print("\nThis is so heart touching!\n")
        print("%s, "% user_name)
        print(feartxt.read())
        print("if u have something else to say,\nplease forward it to our email adddress.\n \nEmail: fearcracker@gmail.com \n \n")
        dead("Nice talking with u,%s" % user_name)
    elif len(fear_input) < 10:
        print("\n You have to tell me something more about your fear \n for me to help you")
        
    else:
        print("You have to tell me something for me to help you")

    
def dream():
    dead("\n We care so much about u %s,. Our DREAM CRACKER is currently unavailable, \nu can still reach us on \n07031260561" % user_name)
    
start()