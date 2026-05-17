#14:50の送信コード修正（簡略化)
number = int(input("=>"))
counter = 1
sum = 0

while counter <= number: 
    sum = counter+sum
    counter += 1

print(sum)

