def sequential_search(list,element):
    index = 0
    found = False 
    while index < len(list) and not found :
        if list[index] == element:
            found = True
        else: 
            index = index + 1
    return found , index
print(sequential_search([1,3,5,7,8,90,4], 90))