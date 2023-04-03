import json
from datetime import datetime


def lastApplied(username):
    with open('users.json', 'r') as f:
        users = json.load(f)

    now = datetime.today().date()

    for user in users:
        if user['username'] == username:
            if (now - datetime.fromisoformat(user['lastApplied']).date()).days >= 7:
                return True


def hasProfile(username):
    with open('profiles.json', 'r') as f:
        profiles = json.load(f)

    for user in profiles:
        if username not in user["username"]:
            print("Don't forget to create a profile\n")


def hasMessages(username):
    with open('users.json', 'r') as f:
        users = json.load(f)

    for user in users:
        if username in user["username"]:
            if user["newMessages"] is True:
                print("You have messages waiting for you\n")
            user["newMessages"] = False

    with open("users.json", "w") as f:
        json.dump(users, f)


def numJobsApplied(username):
    with open('users.json', 'r') as f:
        users = json.load(f)

    for user in users:
        if username in user["username"]:
            numJobs = len(user["jobsApplied"])
            print(f"You have currently applied for {numJobs} jobs\n")


def newJobPost(username):
    with open('users.json', 'r') as f:
        users = json.load(f)

    with open('jobs.json', 'r') as f:
        jobs = json.load(f)

    for user in users:
        if username in user["username"]:
            if user["newPosting"] is not None:
                new_posting = user["newPosting"]
                for jobID in new_posting:
                    for job in jobs:
                        if job['jobID'] == jobID:
                            title = job['title']
                            print(f"A new job {title} has been posted.\n")
                            new_posting.remove(jobID)
                user["newPosting"] = new_posting

    with open("users.json", "w") as f:
        json.dump(users, f)

