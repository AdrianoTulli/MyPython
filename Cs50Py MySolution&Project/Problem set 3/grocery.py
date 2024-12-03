order = {
}
while True:
    try:
        item=input().upper().strip()
    except EOFError:
        break
    else:
        if item in order:
            order[item]+=1
        else:
            order[item]=1
for grocery in sorted(order):
   print(order[grocery], grocery, end='\n')
