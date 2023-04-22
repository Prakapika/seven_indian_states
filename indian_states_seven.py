import json

seven_states_india = {
    "Tamilnadu": "Chennai",
    "Telangana" : "Hyderabad",
    "Karnataka" : "Bangalore",
    "Kerela" : "Kochin",
    "Rajasthan" : "Jaipur",
    "Maharastra" : "mumbai",
    "West Bengal" : "Kolkata"
}

with open(r'seven_states_india.json', "w") as file:
    json.dump(seven_states_india, file)

with open(r'seven_states_india.json', "r") as file:
    data = file.readlines()
    print(data)