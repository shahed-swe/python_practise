string = "sometime it’s better to go back to your own"
arr = list(map(str, string.split(' ')))
for i in range(len(arr)):
    print(f"Length of:{arr[i]} is {len(arr[i])}")