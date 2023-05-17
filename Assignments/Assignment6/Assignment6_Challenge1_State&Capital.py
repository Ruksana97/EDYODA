import json

state_capitals={'Kerala':'Trivandrum','Karnataka':'Bengaluru','Goa':'Panaji','Bihar':'Patna','MadhyaPradesh':'Bhopal','Punjab':'Chandigarh','TamilNadu':'Chennai'}

with open('State_Capitals.json','w') as s:
    json.dump(state_capitals,s)
    print('Added successfully')