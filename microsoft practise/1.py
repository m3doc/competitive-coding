fname  = raw_input()
new_file = "bytes_"+fname

count = 0
total = 0
with open(fname) as f:
    content = f.readlines()
    content = [x.strip() for x in content]
    for i in content:
        byte = int(i.split(" ")[-1])
        if byte > 5000:
            count +=1
            total += byte

f= open(new_file,"w+")
f.write(str(count)+'\n')
f.write(str(total))

# print count
# print total