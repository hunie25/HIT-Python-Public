input_list = input().split()
result = []

for word in input_list:
    for char in word:
        if char not in result and (char.isalpha() or char.isdigit()):
            result.append(char)
print(result)
