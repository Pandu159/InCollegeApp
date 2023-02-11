from authentication import *
def HomeScreen():
    print("Welcome to InCollege!")
    print("Meet Jake, a recent college grad in marketing who found out about InCollege at a career fair.")
    print("After creating his profile, connecting with industry professionals, and joining related groups, Jake received a message from a recruiter on InCollege, who was impressed by his profile and wanted to interview him.")
    print("He aced the interview and got the job on the spot. Jake's success shows the value of using InCollege.")


def findJob():
    print("under construction")


def findPeople():
    firstName = input("Please enter the first name: ")
    lastName = input("Please enter the last name: ")

    users = readUsers()

    for user in users:
        if firstName == user["firstName"] and lastName == user["lastName"]:
            print("They are a part of the InCollege system")
            return

    print("They are not yet a part of the InCollege system")



def selectSkill():
    skill = input \
        ("Please select a skill to learn from the list:\n1-Time management\n2-Teamwork\n3-Written communication\n4-Verbal communication\n5-Project management\n6-Return to main menu\n")
    if skill == 1:
        print("under construction")
    elif skill == 2:
        print("under construction")
    elif skill == 3:
        print("under construction")
    elif skill == 4:
        print("under construction")
    elif skill == 5:
        print("under construction")
    elif skill == 6:
        selectOption()
    else:
        print("Not a valid option")
        exit(-1)

def selectOption():
    option = int(input
        ("Please select from the following options:\n1 - Find a job/internship\n2 - Find someone you know\n3 - Learn a new "
         "skill\n0 - To exit"))

    if option == 1:
        findJob()
    elif option == 2:
        findPeople()
    elif option == 3:
        selectSkill()
    elif option == 0:
        return
    else:
        print("Not a valid option")
        exit(-1)
