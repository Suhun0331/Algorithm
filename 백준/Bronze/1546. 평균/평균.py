num = int(input())

result = list(map(int, input().split()))

maxx = max(result)

for i in range(num):
    result[i] = result[i]/maxx*100
        
average = sum(result)/num

print(average)