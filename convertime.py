# 秒数を入力して時:分:秒に変換するプログラム

print("秒数を入力してください。")
seconds = int(input("=>"))

hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

print(hours,":",minutes,":",seconds)
