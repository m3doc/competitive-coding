# url: https://leetcode.com/problems/longest-substring-without-repeating-characters/

from collections import defaultdict
def solve(string):
    if string=='':
        return 0
    # Longest = ''
    LongestLen = 0
    visited = {}
    # currentLongest = ''
    currentLongestLen = 0
    startIndex = 0
    def clearVisited(visited,startIndex,lastIndex,string):
        # print visited,startIndex,lastIndex,string
        for character in string[startIndex:lastIndex+1]:
            del visited[character]
        return visited


    for index,character in enumerate(string):
        if character not in visited:
            visited[character]=index
            # currentLongest += character
            currentLongestLen += 1
        else:
            # print visited
            if currentLongestLen>LongestLen:
                LongestLen=currentLongestLen
                currentLongest = string[startIndex:index]
            # print visited
            currentLongestLen = index - visited[character]
            temp = visited[character] + 1
            visited = clearVisited(visited, startIndex, visited[character], string)
            startIndex = temp
            # print visited


            # Longest = currentLongest
            visited[character]=index
    if currentLongestLen > LongestLen:
        LongestLen = currentLongestLen
        currentLongest = string[startIndex:index+1]
    return len(currentLongest)

    #
    # pass
    # return

print solve("abba")
# print solve("pwwkew")
# print solve("")
# print solve("a")
# print solve("abcabcbb")
# print solve("bbbbb")
