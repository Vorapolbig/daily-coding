"""
We have an array A of integers, and an array queries of queries.

For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  Then, the answer to the i-th query is the sum of the even values of A.

(Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)

Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.
"""



def solution(A, queries):
    output = []
    for i in range(len(A)):
        val = queries[i][0]
        index = queries[i][1]
        A[index] += val
        even = 0
        for i in A:
            if i % 2 == 0:
                even += i
        output.append(even)
    return output  

A = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]

print(solution(A, queries))