import time

def focus_clock(minutes):
    seconds = minutes * 60
    end_time = time.time() + seconds

    while time.time() < end_time:
        remaining_time = end_time - time.time()
        minutes = int(remaining_time // 60)
        seconds = int(remaining_time % 60)

        print(f"Remaining Time: {minutes:02d}:{seconds:02d}", end='\r')
        time.sleep(1)

    print("Time's up!")

# 设置专注时间为25分钟
focus_clock(25)
