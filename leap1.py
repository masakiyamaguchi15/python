print('西暦を入れてください')
year = input('=>')

# yearを400で割って余りが0のときはうるう年
if int(year)%400 == 0:
    print("うるう年です")
elif int(year)%100 == 0:
    print("うるう年ではないです。")
elif int(year)%4 == 0:
    print("うるう年です")
else:
    print("うるう年ではないです。")




