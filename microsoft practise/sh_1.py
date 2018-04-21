# generate the value table for all items
def knapsack(weights,values,maximum_weight):
    heightOfTable = len(values)
    weightTable = [[0 for x in xrange(maximum_weight+1)] for y in xrange(heightOfTable)]
    for column in xrange(weights[0],maximum_weight+1):
        weightTable[0][column]=values[0]
    for row in xrange(1,heightOfTable):
        for column in xrange(maximum_weight+1):
            if column>=weights[row]:
                weightTable[row][column]=max(values[row]+weightTable[row-1][column-weights[row]],weightTable[row-1][column])
            else:
                weightTable[row][column]=weightTable[row-1][column]

    return weightTable


# return the exact items with which we get the maximum value
def traceElementsOfWeights(weights,weightTable,maximum_weight):
    heightOfTable = len(weights)
    steps = []
    for row in xrange(heightOfTable-1,-1,-1):
        if row == 0:
            if weightTable[row][maximum_weight]==0:
                pass
            else:
                steps = [weights[row]] + steps
        else:
            if weightTable[row][maximum_weight]==weightTable[row-1][maximum_weight]:
                pass
            else:
                steps = [weights[row]]+steps
                maximum_weight -= weights[row]
    return steps




weights = [5, 10, 15]
values = [10, 30, 20]
maximum_weight = 100

# weights = [24,20]
# values =  [20,19]
# maximum_weight = 500

def unbounded_knapsack(weight, value, maximum_weight):
    knapsack_values = [0 for i in xrange(maximum_weight + 1)]
    for i in xrange(maximum_weight +1 ):
        for j in xrange(len(weight)):
            if weight[j] <= i:
                knapsack_values[i] = max(knapsack_values[i], knapsack_values[ i - weight[j]] + value[j] )

    print knapsack_values[maximum_weight]




# Complete the function below.

def budgetShopping(n, bundleQuantities, bundleCosts):
    knapsack_values = [0 for i in xrange(n + 1)]
    for i in xrange(n +1 ):
        for j in xrange(len(bundleCosts)):
            if bundleCosts[j] <= i:
                knapsack_values[i] = max(knapsack_values[i], knapsack_values[ i- bundleCosts[j]] + bundleQuantities[j])

    return knapsack_values[n]






def greedy_knapsack(weight, value, maximum_weight):
    new_arr =[]
    for i in xrange(len(weight)):
        new_arr.append((value[i])/weight[i])
    sorted_keys = sorted(range(len(new_arr)), key=lambda k: new_arr[k], reverse=True)
    total_value = 0
    total_weights = []
    # print sorted_keys
    for i in sorted_keys:
        total_value += (maximum_weight/weight[i]) * value[i]
        total_weights.append([(maximum_weight/weight[i]), value[i]])
        maximum_weight = maximum_weight % weight[i]

    print total_value




if __name__=='__main__':

    greedy_knapsack(weights, values, maximum_weight)
    unbounded_knapsack(weights, values, maximum_weight)

    # ###table has the value for all intermediate weights and maximum values which can be acheived
    # table = knapsack(weights,values,maximum_weight)
    # # for x in table:
    # #     print x
    # print table[len(weights)-1][maximum_weight]
    # # for index, i in enumerate(table):
    # #     print i
    #
    # print traceElementsOfWeights(weights,table,maximum_weight)