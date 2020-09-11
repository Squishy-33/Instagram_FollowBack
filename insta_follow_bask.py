import json

following = {}
followers = {}

following_names_list = []
followers_names_list = []

with open('connections.json') as ins_con:
    data = json.load(ins_con)


following = data['following']
followers = data['followers']


for k, v in following.items():
    following_names_list.append(k)

for k, v in followers.items():
    followers_names_list.append(k)

followers_set = set(followers_names_list)
diff = [x for x in following_names_list if x not in followers_set]

print(diff)
