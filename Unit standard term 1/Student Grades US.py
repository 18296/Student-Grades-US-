dictionary = {}

def import_file(file):
    while True:
        with open(file) as file:
            for line in file:
                key, info = line.split(",", 1)  # splits each line in doc into a key and info
                data = info.split(",")
                dictionary[key] = data

            file.close()
            break

import_file("student+data.csv")
print(dictionary.get("2"))
print(dictionary["2"])