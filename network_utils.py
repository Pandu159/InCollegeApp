from authentication import *
from feed import *
from helper import *

# Displays pending request when user logs in
def requestDisplay(uName):
    users = readUsers()
    for user in users:
        if user["username"] == uName:
            if len(user["friendRequests"]) != 0:
                print("You have pending friend requests")
                return True
    return False


# This function checks if logged-in user has any friend requests and prompts them to accept or reject the friend request
def checkFriendRequests(uName):
    users = readUsers()
    for user in users:
        if user["username"] == uName:
            if len(user["friendRequests"]) != 0:
                print("You have pending friend requests:")
                for friendRequests in user["friendRequests"]:
                    print(friendRequests)
                friendName = input("Input Friend username you want to accept or reject: ")
                while True:
                    response = input("Do you want to accept or reject the friend request? (A/R): ").upper()
                    if response == "A":
                        addFriend(uName, friendName)
                        addFriend(friendName, uName)
                        removeRequest(uName, friendName)
                        print(f"{friendName} added as a friend.")
                        break
                    elif response == "R":
                        removeRequest(uName, friendName)
                        break
                    else:
                        print("Invalid response.")
                        continue

            else:
                print("You have no pending friend requests.")
                break

    selection = int(input("Input 0 to return to previous screen or 1 to check more friend request: "))
    if selection == 0:
        returnToOption(selection, uName)
    else:
        checkFriendRequests(uName)


# This function lets logged-in user to search people requests and send them requests
def searchAndRequest(uName):
    friendUser = searchUsers()
    if len(friendUser) != 0:
        friendUserName = friendUser[0]["username"]
        print("User Found")
        response = input("Do you want to add them as friends: Y/N ").upper()
        if response == "Y":
            users = readUsers()
            for user in users:
                if user["username"] == friendUserName:
                    user["friendRequests"].append(uName)
            with open("users.json", "w") as f:
                json.dump(users, f)
    else:
        print("No users found.")

    selection = int(input("Input 0 to return to previous screen or 1 to search again: "))
    if selection == 0:
        returnToOption(selection, uName)
    else:
        searchAndRequest(uName)


# This function lets logged-in user to see their network and option to remove friends
def showMyNetwork(uName):
    users = readUsers()
    for user in users:
        if user["username"] == uName:
            if len(user["friends"]) != 0:
                print("You have the following friends in network:")
                for friend in user["friends"]:
                    print(friend)
                while True:
                    response = input("Do you want to remove friends (Y/N): ").upper()
                    if response == "Y":
                        response1 = input("Input Friend name you want to remove: ")
                        removeFriend(uName, response1)
                        removeFriend(response1, uName)
                        print(f"{response1} removed as a friend.")
                        break
                    elif response == "N":
                        print("None of the friends have been removed")
                        break
                    else:
                        print("Invalid response.")
                        continue
            else:
                print("None")
                break

    selection = int(input("Input 0 to return to previous screen or 1 to Show your network: "))
    if selection == 0:
        returnToOption(selection, uName)
    else:
        showMyNetwork(uName)


# helper function for removing friends
def removeFriend(uName, Friendsusers):
    users = readUsers()
    for user in users:
        if user["username"] == uName:
            user["friends"].remove(Friendsusers)
    with open("users.json", "w") as f:
        json.dump(users, f)


# helper function for searching users
def searchUsers():
    lastName = input("Please enter the last name or skip: ")
    university = input("Please enter the University name or skip: ")
    major = input("Please enter the major name or skip: ")

    users = readUsers()
    filteredUsers = []
    for user in users:
        if lastName is not None and user["lastName"] == lastName:
            filteredUsers.append(user)
            break
        elif university is not None and user["college"] == university:
            filteredUsers.append(user)
            break
        elif major is not None and user["major"] == major:
            filteredUsers.append(user)
            break
        else:
            continue

    return filteredUsers


# helper function for adding friend once user accepts the request
def addFriend(uName, friendUsername):
    users = readUsers()
    for user in users:
        if user["username"] == uName:
            user["friends"].append(friendUsername)
    with open("users.json", "w") as f:
        json.dump(users, f)


# helper function for removing friend request once user accepts or rejects them
def removeRequest(uName, friendUsername):
    users = readUsers()
    for user in users:
        if user["username"] == uName:
            user["friendRequests"].remove(friendUsername)
    with open("users.json", "w") as f:
        json.dump(users, f)
