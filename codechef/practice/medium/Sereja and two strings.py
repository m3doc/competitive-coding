# url https://www.codechef.com/problems/SEATSR

global edit_table
edit_table = list()

# function to initialize edit table
def init_edit_table(original_string_length,final_string_length,a):
    edit_table.append([x*a for x in xrange(original_string_length + 1)])
    # for i in xrange(1, final_string_length + 1):
    #     edit_table.append([i*a] + [0] * original_string_length)


def getMinimum(final_string_counter,original_string_counter,a,b):
    # print len(edit_table)
    # print final_string_counter
    # print original_string_counter
    A = edit_table[final_string_counter][original_string_counter]
    B = edit_table[final_string_counter + 1][original_string_counter]
    C = edit_table[final_string_counter][original_string_counter + 1]
    return min(A+b,B+a,C+a)

# creating the table for number of edits
def create_edit_table(original_string,final_string,a,b,k):
    final_string_length = len(final_string)
    original_string_length = len(original_string)
    init_edit_table(original_string_length,final_string_length,a)

    for final_string_counter in xrange(final_string_length):
        currentMinimum = (final_string_counter+1)*a
        edit_table.append([(final_string_counter+1)*a] + [0] * original_string_length)
        for original_string_counter in xrange(original_string_length):

            if original_string[original_string_counter]==final_string[final_string_counter]:
                edit_table[final_string_counter+1][original_string_counter+1]=getMinimum(final_string_counter, original_string_counter, 0, 0)
            else:
                #edit_table[final_string_counter+1][original_string_counter+1]=min(edit_table[final_string_counter][original_string_counter],edit_table[final_string_counter+1][original_string_counter],edit_table[final_string_counter][original_string_counter+1])+1
                mini = getMinimum(final_string_counter, original_string_counter, a, b)
                # print "mini: ",
                # print mini
                edit_table[final_string_counter + 1][original_string_counter + 1]=mini
            if currentMinimum>edit_table[final_string_counter + 1][original_string_counter + 1]:
                currentMinimum= edit_table[final_string_counter + 1][original_string_counter + 1]
        if currentMinimum>k and (final_string_counter+2)*a>k:
            return -1,edit_table[0][0]


    return 0,edit_table[final_string_length][original_string_length]


def checkMinEdit(stringA,stringB):
    list1 = [0]*26
    list2 = [0]*26
    for i in stringA:
        list1[ord(i)-ord('a')] +=1
    for i in stringB:
        list2[ord(i) - ord('a')] += 1
    diff = 0
    for i in xrange(26):
        diff +=abs(list1[i]-list2[i])
    return diff

def reduceString(stringA,stringB):
    maxIndex = min(len(stringA),len(stringB))
    newStringA = ''
    newStringB = ''
    for i in xrange(maxIndex):
        if stringA[i]==stringB[i]:
            pass
        else:
            newStringA +=stringA[i]
            newStringB +=stringB[i]
    newStringA +=stringA[maxIndex:]
    newStringB +=stringB[maxIndex:]
    return newStringA,newStringB



if __name__ == '__main__':
    t = int(raw_input())
    while t:
        t -=1
        s = raw_input().strip()
        w = raw_input().strip()
        # s = 'a'*100000
        # w = 'a'*99999 + 'b'
        # s='abcd'
        # w='dbe'
        a,b,k = map(int,raw_input().strip().split(" "))
        s, w = reduceString(s, w)
        # print s
        # print w
        if a==0 and b==0:
            print 0
        elif checkMinEdit(s,w)*min(a,b)>k:
            print -1
        else:
            x,y = create_edit_table(s,w,a,b,k)
            # for i in edit_table:
            #     print i
            # print len(edit_table)
            # print edit_table[len(edit_table) - 2][:10]
            # print edit_table[len(edit_table)-1][:10]
            # print edit_table[len(edit_table)]
            if x==-1:
                print x
            else:
                print y
            # print edit_table[len(w)][len(s)]
            del edit_table[:]

