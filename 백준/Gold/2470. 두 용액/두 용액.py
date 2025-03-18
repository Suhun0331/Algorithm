n = int(input())

arr = list(map(int, input().split()))
arr.sort()

left, right = 0, n-1
value = float('inf')
answer = [left, right]
while left < right:
    hap = arr[left] + arr[right]
    if value > abs(hap):
        value = abs(hap)
        answer[0], answer[1] = left, right

    if hap > 0:
        right -= 1
    elif hap < 0:
        left += 1
    else:
        break

    
print(arr[answer[0]], arr[answer[1]])
        