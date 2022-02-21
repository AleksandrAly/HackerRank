# if you leave other lines of code, an error will be thrown
S = input().strip()
try:
    print(int(S))
except ValueError:
    print("Bad String")

