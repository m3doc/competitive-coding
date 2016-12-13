
def problem(points,m,MIN,MAX):
    totalValues = 0
    start = 0
    previous =MAX
    for index,item in enumerate(points[start:]):
        currentDiff=item - points[index]
        if MIN<=currentDiff<=MAX:
            totalValues +=currentDiff
        if m == totalValues:
            return start
        elif m<totalValues:
            if currentDiff


    pass




def findNextStart(points,index,MAX,MIN):
    value = points[index]-points[index-1]
    if value>=MIN:
        return index
    else:
        return findNextStart(points,index+1,MAX,MIN)
def solve(points,m,MIN,MAX,remainingDistance,startingPoint,indexStart):
    for index,item  in enumerate(points[indexStart:]):
        # print index
        # print index-1
        # print points[index-1]
        # # print points
        # print item
        currentDistnace = item-points[indexStart+index-1]

        if currentDistnace>=MIN and currentDistnace<=MAX:
            remainingDistance -=currentDistnace
        elif currentDistnace>MAX and remainingDistance<currentDistnace:
            if remainingDistance >=MIN:
                remainingDistance -=MAX
            elif remainingDistance <MIN:
                if (points[indexStart]-startingPoint) + remainingDistance >=2*MIN:
                    startingPoint +=MIN-remainingDistance
                    return startingPoint
                else:
                    return solve(points, m, MIN, MAX, m, indexStart, indexStart+1)

        else:
            indexToStartWith = findNextStart(points,indexStart+index,MAX,MIN)
            if points[indexToStartWith]-points[indexToStartWith-1]>=MAX:

                startingPoint=points[indexToStartWith] - MAX
                indexStart = indexToStartWith+1
                remainingDistance = m - MAX
            else:
                startingPoint = points[indexToStartWith-1]
                indexStart = indexToStartWith + 1
                remainingDistance = m - (points[indexToStartWith]-points[indexToStartWith-1])


                return solve(points,m,MIN,MAX,remainingDistance,startingPoint,indexStart)
        # print "r: ",
        # print remainingDistance
        if remainingDistance<=0:
            return startingPoint
    return startingPoint







if __name__=="__main__":
    n =int(raw_input().strip())
    points = map(int,raw_input().strip().split(" "))
    m,MIN,MAX = map(int,raw_input().strip().split(" "))
    remainingDistance = m
    remainingDistance -= MAX
    startingPoint = points[0] - MAX
    indexStart = 1
    print solve(points,m,MIN,MAX,remainingDistance,startingPoint,indexStart)

