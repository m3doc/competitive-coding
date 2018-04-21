import os
import hashlib



# def new_dash(key):
#     hash_object = hashlib.sha256(key)
#     hex_dig = hash_object.hexdigest()
#     print hex_dig
#     hash_object2 = hashlib.sha256(hex_dig)
#     hex_dig = hash_object2.hexdigest()
#     print hex_dig
#     return hex_dig

def dhash(key):
    hash_object = hashlib.sha256(key)
    hex_dig = hash_object.hexdigest()
    print hex_dig
    hash_object2 = hashlib.sha256(hex_dig)
    hex_dig = hash_object2.hexdigest()
    print hex_dig
    return hex_dig




nterms = 50

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# first two terms
n1 = 0
n2 = 1
count = 0
arr = []
# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
   arr += [dhash(str(n1))]
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       arr += [dhash(str(n1))]
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

print arr


while 1:
    for i in range(0,50,2):
        print arr[i],
    break


while 1:
    if len(arr) <2:
        break
    newarr = []
    for i in range(0, len(arr), 2):
        newarr.append(dhash(arr[i]+arr[i+1]))
    print arr
    print newarr
    arr = newarr
    if len(arr)%2 == 1 and len(arr)!=1:
        arr.append(arr[-1])
print arr

# print new_dash(arr[0])

