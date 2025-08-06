from collections import Counter
numbers = list(map(int, input().split()))

count = Counter(numbers)
keys = list(count.keys())

i = 0
while i < len(keys):
    num = keys[i]
    freq = count[num]
    if freq % 5 == 0 and num % 10 != 0:
        print(num, end=' ')
    i += 1
