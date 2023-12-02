with open('input.txt') as f:
    input_vals = f.read().split()
ans = 0

for val in input_vals:
    x = None 
    y = None  
    check = False
    for i in range(len(val)):
        result = -1
        if val[i].isnumeric():
            if check == False:
                x = int(val[i])
                check = True
            else:
                y = int(val[i])
        elif val[i:].startswith("one"):
            result = 1
        elif val[i:].startswith("two"):
            result = 2
        elif val[i:].startswith("three"):
            result = 3
        elif val[i:].startswith("four"):
            result = 4
        elif val[i:].startswith("five"):
            result = 5
        elif val[i:].startswith("six"):
            result = 6
        elif val[i:].startswith("seven"):
            result = 7
        elif val[i:].startswith("eight"):
            result = 8
        elif val[i:].startswith("nine"):
            result = 9
        elif val[i:].startswith("zero"):
            result = 0
        if result > -1:
            if check == False:
                x = result
                check = True
            else:
                y = result            
        if y==None:
            y = x
    ans+=(x*10+y)
print(ans)