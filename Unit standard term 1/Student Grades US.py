import os
dictionary = {}
# Yaeko Threlkeld

def import_file():
    l = []
    f = os.listdir('.')  # open folder
    for i in range(len(f)):
        if '.csv' in f[i]:
            l.append(f[i])
        elif '.txt' in f[i]:  # if file has extention txt or csv, display it
            l.append(f[i])
        else:
            pass

    print("files available:" + str(l))
    while True:

        file_select = int(input("please select files 1-" + str(len(l)) + "\t"))
        if file_select in range(1, len(l) + 1, 1):
            file = l[file_select - 1]  # starts at 0
            break

    while True:
        with open(file) as file:
            for line in file:
                id, name, info = line.split(",", 2)  # splits each line in doc into id, name, info
                data = info.split(",")
                dictionary[name] = data

            file.close()
            break

def main():
    import_file()
    while True:
        student_name = input("What student are you looking up?\t")  # .lower() this
        try:
            print(dictionary.get(student_name))

        except:
            pass

main()
