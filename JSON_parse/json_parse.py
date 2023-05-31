import json

#reading the json file
file = open("sample.json", "r")
sample = file.read()
file.close()
#printing the json file
print(sample)
#assigning the json file into a variable as dict
details = json.loads(sample)

print(details['fruit'])

#looping thru the json file and prints the key and value pairs
for desc in details:
    print(desc, details[desc])