# rrr
# 导入time模块
import time

# 定义专注时间和休息时间的长度（单位：秒）
focus_time = 25 * 60
break_time = 5 * 60

# 定义一个函数，用于显示倒计时
def countdown(seconds):
    # 将秒数转换为分和秒
    minutes = seconds // 60
    seconds = seconds % 60
    # 格式化输出
    print(f"{minutes:02d}:{seconds:02d}", end="\r")
    # 每隔一秒刷新一次
    time.sleep(1)

# 定义一个函数，用于播放提示音
def beep():
    # 打印一个换行符，避免覆盖倒计时
    print()
    # 播放提示音（这里用print代替）
    print("Beep!")

# 定义一个变量，用于记录完成的专注次数
focus_count = 0

# 开始循环
while True:
    # 开始专注时间
    print("开始专注时间，请勿分心！")
    for i in range(focus_time):
        countdown(focus_time - i)
    beep()
    # 增加专注次数
    focus_count += 1
    print(f"恭喜您完成了{focus_count}次专注！")
    # 开始休息时间
    print("开始休息时间，请放松一下！")
    for i in range(break_time):
        countdown(break_time - i)
    beep()
