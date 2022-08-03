
if __name__ == '__main__':
    n = int(input())
    validname = []
    for i in range(n):
        l = input().split()
        name = l[0]
        email = l[1]
        if email.find("@gmail.com"):
            validname.append(name)
    for i in sorted(validname):
        print(i)

