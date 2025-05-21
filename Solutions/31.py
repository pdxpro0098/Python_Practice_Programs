def cubeOfSum(late):
    sum = 0
    for i in range(0,len(late)):
        sum += late[i]
    print("The sum of Natural No is:",sum)
    cube = sum**3
    print(f"The cube of {sum} is:",cube)


cubeOfSum((3,2,5,2))
