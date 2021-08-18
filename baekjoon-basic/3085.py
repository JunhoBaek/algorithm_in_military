def check(arr):
    n = len(arr)
    answer = 1

    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            
            if cnt > answer:
                answer = cnt

        cnt = 1
        for j in range(1, n):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt = 1
        
            if cnt > answer:
                answer = cnt
    
    return answer

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(input()))
answer = 0

for i in range(n):
    for j in range(n):
        if j+1 < n:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

            tmp = check(arr)
            if tmp > answer:
                answer = tmp
            
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        
        if i+1 < n:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

            tmp = check(arr)
            if tmp > answer:
                answer = tmp
            
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
print(answer)