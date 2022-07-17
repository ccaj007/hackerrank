# https://www.hackerrank.com/domains/tutorials/30-days-of-code
inp = ['sam 99912222','tom 11122222','harry 12299933']
t = ['sam','edward','harry']

phonebook = {}
# n = int(input())
n=3
for i in range(n):
    #contact = input().split(' ')
    contact = inp[i].split(' ')
    phonebook[contact[0]] = contact[1]

for _ in range(n):
    find_name = input()
    if find_name in phonebook:
        print(find_name + "=" + phonebook[find_name])
    else:
        print("Not found")
#print(phonebook)


