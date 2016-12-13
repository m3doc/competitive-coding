

# url:  https://www.facebook.com/hackercup/problem/582062045257424/
# important point while calculating small number check for the last index of same number to replace not the very first instance

def solve(number):
    if number==0:
        return number,number
    array=[]
    while number:
        array.insert(0,number%10)
        number /= 10
    sortedNumbers=sorted(range(len(array)), key=lambda k: array[k])
    smallNumber = [x for x in array]
    bigNumber = [x for x in array]
    for index,digit in enumerate(array):
        flag = 0
        for sortedIndex,newDigitIndex in enumerate(sortedNumbers):
            if array[newDigitIndex]<digit and index<newDigitIndex:
                if newDigitIndex!=len(array)-1 and array[newDigitIndex]==array[sortedNumbers[sortedIndex+1]]:
                    pass
                elif array[newDigitIndex] == 0 and index == 0:
                    pass
                else:

                    smallNumber[index]=array[newDigitIndex]
                    smallNumber[newDigitIndex]=digit
                    flag=1
                    break
        if flag:
            break
    for index, digit in enumerate(array):
        flag = 0
        for newDigitIndex in sortedNumbers[::-1]:
            if array[newDigitIndex] > digit and index<newDigitIndex:
                bigNumber[index] = array[newDigitIndex]
                bigNumber[newDigitIndex] = digit
                flag=1
                break
        if flag:
            break
    return ''.join(map(str,smallNumber)),''.join(map(str,bigNumber))


if __name__=="__main__":
    t = int(raw_input().strip())
    case = 0
    while case < t:
        case += 1
        number = int(raw_input().strip())
        smallNumber,bigNumber=solve(number)
        print "Case #" + str(case) + ":",smallNumber,bigNumber

