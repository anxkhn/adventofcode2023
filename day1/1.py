with open('input.txt') as f:
    input_vals = f.read().split()

ans = 0

for val in input_vals:
    x = None 
    y = None  
    check = False
    for i in val:
        if i.isnumeric():
            if check == False:
                x = int(i)
                check = True
            else:
                y = int(i)
        if y==None:
            y = x
    ans+=(x*10+y)
print(ans)