import json

f = open('data.json', 'r+')
data = json.load(f)
print("Current inventory")
for i in data["inventory"]:
  print(i)

list = data

print("Enter the name of the new item to be added")
new_item = input()
new_id = len(data["inventory"]) + 1
new_entry = {"id": new_id, "item_name": new_item}

data["inventory"].append(new_entry)
f.seek(0)


json.dump(data, f)

print("Current inventory")
for i in data["inventory"]:
  print(i["item_name"])

f.close()