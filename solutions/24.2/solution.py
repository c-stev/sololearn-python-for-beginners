total = 0
#your code goes here

total = 0
passengers = 5

while passengers != 0:
    age = int(input())
    passengers -= 1
    if age < 3:
        continue
    total += 100

print(total)