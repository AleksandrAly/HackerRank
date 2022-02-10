n = int(input())
call_list = []
dict = {}
for i in range(n):  #create list with names and numbers
    name_num = input()
    call_list.append(name_num)
for friends in call_list:  #create dictionary from list elements
    name = friends[:-9]
    num = friends[-8:]
    dict[name] = num

def Friend_Number(search_name):
    """The function find the friend phone number in dictionary by name"""
    if search_name in dict:
        print(search_name, '=', dict[search_name], sep='')
    else:
        print('Not found')
    return

while (True):
    try:
        search_name = input().rstrip() #!!!.rstrip() is nessecary to delete "empty" symbols at the end
        Friend_Number(search_name)
    except EOFError:
        break
