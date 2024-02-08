# runtime complexity: O(n + M)
# space comeplxity: O(n + M)
# constraints: len(arr) > M, arr[i] < M for i in range(arr)
def countingSort(arr, M):

    count = [0] * M

    for v in arr:
        count[v] += 1

    sortedArr = [-1] * sum(count)

    j = 0
    for i in range(M):
        if count[i] != 0:
            for j in range(count[i]):
                sortedArr[j] = i
                j += 1
        
    arr = sortedArr
    return arr
