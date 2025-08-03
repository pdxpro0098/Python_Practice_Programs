def divisibles():
    for i in range(5,25+1):
        if(i % 7== 0 or i%5==0):
            yield i

for num in divisibles():
    print(num)
