phonebook = {}
n = int(input())
for _ in range(n):
    contact = input().split(' ')
    phonebook[contact[0]] = contact[1]

for _ in range(n):
    find_name = input()
    if find_name in phonebook:
        print(find_name + "=" + str(phonebook[find_name]))
    else:
        print("Not found")
#print(phonebook)


