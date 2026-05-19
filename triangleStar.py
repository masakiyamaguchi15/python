# triangle.py

stars = int(input("stars=>"))

for i in range(1, stars+1):
    for j in range(1,i+1):
        print("*", end="")
    print()
    
# 別の書き方
stars = int(input("stars=>"))

for i in range(1, stars + 1):
    print("*" * i)

