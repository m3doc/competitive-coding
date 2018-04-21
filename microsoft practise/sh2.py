def calculate(s, l, r, k):
    str = s
    start = l
    end = r
    changes = k
    def pre_calculate(str):
        global array
        array = []
        array.append([0] * 26)
        array.append([0] * 26)
        index = 1
        # new_array = []
        # for i in array[index]:
        #     new_array.append(i)
        # array.append(new_array)
        for character in str:
            array[index][ord(character) - ord('a')] += 1
            new_array = []
            for i in array[index]:
                new_array.append(i)
            array.append(new_array)
            index += 1

        return array[:-1]

    def can_be_palindrome(char_array, change):
        # print char_array
        # print change
        odd_values = 0
        for i in char_array:
            if i % 2 == 1:
                odd_values += 1
        # print odd_values
        return odd_values - 1 <= change * 2

    def calculate_diff_array(arr1, arr2):
        new_arr = []
        for i in xrange(len(arr1)):
            new_arr.append(arr2[i] - arr1[i])
        return new_arr

    array = pre_calculate(str)

    # for i in array:
    #     print i

    result = ''
    for i in xrange(len(start)):
        if start[i] == 0 and end[i] == 0:
            sub_array = array[1]
        elif start[i] == 0:
            sub_array = array[end[i] +1]
        else:
            sub_array = calculate_diff_array(array[start[i]], array[end[i] + 1])
        if can_be_palindrome(sub_array, changes[i]):
            result += '1'
        else:
            result += '0'
    return result






if __name__== "__main__":

    print calculate('cdecd', [0,0,0,0], [0,1,2,3], [0,1,1,0])
