import time
def countdown(tg):
    while tg:
        mins, secs = divmod(tg, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        # print(timer, end="\r")
        print(timer)
        time.sleep(1)
        tg -= 1


    print('Fire in the hole!!')


countdown(5)