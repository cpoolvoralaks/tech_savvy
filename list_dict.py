# L = [
#     ['Apple', 'Google', 'Microsft'],
#     ['Java','Python', ['Ruby','On Rail'],'PHP'],
#     ['Adam','Bart','Lisa',]
#     ]

# print(L[1][2][0])

# AFC_east = ['New England Patriots',
#             'Buffalo Bills',
#             'Miami Dolphins',
#             'New York Jets']
# print(AFC_east[2][6:])

# name = 'Maddison'
# t = list(name)

# str_team = 'New England Patriots'
# t = str_team.split()
# print(t)
#
# team_name = "$$".join(t)
# print(team_name)

# del AFC_east[-1]
# print(AFC_east)
#
# del AFC[-2:]
# print(AFC)

# Dictionary
# names = ['Bailey', 'Maddison', 'Aob']
# scores = [60, 90, 100]
#
# grades = dict() ## tell python we are creating a new dictionary
# grades['Bailey'] = 60
# grades['Maddison'] = 90
# grades['Aob'] = 100
#
# print(grades)
#
# print(grades['Maddison'])
#
# grades['Aida'] = [99, 98]
# print(grades)
# # print(grades['Penny' in grades])
#
# grades['Aob'] = 'Good' ## aob is key, good is value, the pair of aob and good is an item
#
# print(len(grades))
# print()
#
# for name in grades.keys():
#     print(name)
#
# for whatever in grades.values():
#     print(whatever)
#
# for item in grades.items():
#     print(item)


import urllib.request
import json

APIKEY = '8f62260aa7890d58d9a026e2810341ea'
city = 'Wellesley'
country_code = 'us'
url = 'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'.format(
    city=city, country_code=country_code, APIKEY=APIKEY)

# print(url)
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
print(response_data)

# How do we get current temperature?


