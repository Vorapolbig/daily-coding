def solution(input):
    thenumber = 9999999
    counter = 0
    print(sorted(input, reverse=True))
    for i in sorted(input, reverse=True):
        if thenumber > i:
            thenumber = i
            counter += 1
        if counter == 3:
            return thenumber
    if counter < 3:
        return max(input)


test1 = [1,3,4,5,6,1,7]
test2 = [1,2,2,3,4,6]
test3 = [1,2]
print(solution(test3))