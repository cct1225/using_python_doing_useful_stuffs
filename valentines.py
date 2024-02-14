import time
a="happy valentine\'s day"
b="abcdefghijklmnopqrstuvwxyz '"
z=[]
for c in range(len(a)):
    if z==a:
        break
    for d in range(len(b)):
        if a[c]==b[d]:
            z.append(a[c])
        else:
            print(b[d])
            time.sleep(0.004)
            for x in range(len(z)):
                print(z[x],end="")
        #if a[c]==b[d]:
        #    print("\n")   

            
#for X in range(len(z)):
   # print(z[X],end="",flush=True)
    #time.sleep(0.0001)
