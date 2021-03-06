# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem?isFullScreen=true
import re

def fun(s):
    # return True if s is a valid email, else return False
    valid_email_regex = '^(\w|\-)+[@]([a-z]|[A-Z]|[0-9])+[.]\w{1,3}$'
    if not re.search(valid_email_regex, s):
        return False
    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)