import time

def pomodoro_timer():
    while True:
        # 专注时间为25分钟
        work_time = 25 * 60 
        
        print("开始专注!")
        
        # 倒计时直到专注时间结束
        for remaining in range(work_time, 0, -1):
            mins = remaining // 60
            secs = remaining % 60
            timer_display = "{:02d}:{:02d}".format(mins, secs)
            print(timer_display, end='\r')
            time.sleep(1)
        
        print("专注时间结束!")
        
        # 短休息5分钟
        rest_time = 5 * 60
        print("开始休息5分钟.")
        for remaining in range(rest_time, 0, -1):
            mins = remaining // 60
            secs = remaining % 60
            timer_display = "{:02d}:{:02d}".format(mins, secs)
            print(timer_display, end='\r')
            time.sleep(1)

        print("休息时间结束!")

if __name__ == '__main__':
    pomodoro_timer()
