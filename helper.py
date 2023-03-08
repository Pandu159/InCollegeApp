import json
import feed

# this function opens the jobs.json file and returns a dictionary of values
# EDIT this function now opens multiple json files a returns a dictionary of values
def getJson(fileName):
    try:
        with open(fileName + ".json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def returnToOption(selection, username):
    if selection == 0:
        feed.selectOption(username)
    else:
        print("Not a valid option")
        exit(-1)
