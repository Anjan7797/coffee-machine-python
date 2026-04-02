import json

def load_data():
    with open("data.json", "r") as file:
        data = json.load(file) # Convert JSON file → Python dictionary
    return data["resources"], data["money"], data["history"]



def save_data(resources, profit, history):
    data = {
        "resources" : resources,
         "money"    : profit,
        "history"   : history,
    }

    with open("data.json", "w") as file:
        json.dump(data, file, indent = 4) #json.dump() = save dictionary → JSON