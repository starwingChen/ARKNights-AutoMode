import time
import pyautogui as pg

pg.FAILSAFE = True
pg.PAUSE = 0.5


def note():
    print('请输入挂机时间，单位为分钟')
    duration = int(input())
    start = time.perf_counter()

    print(f'程序将在 5 秒后开始，请在时间内切换到游戏窗口')
    for i in range(5, 0, -1):
        print(f'倒计时：{i}')
        time.sleep(1)
    return duration, start


def auto_click(path):
    coords = pg.locateOnScreen(path)
    pg.moveTo(pg.center(coords))
    pg.click()


def execute(duration, start):
    duration *= 60
    while time.perf_counter() - start <= duration:
        coords1 = pg.locateOnScreen('./img/start.PNG')
        pg.moveTo(pg.center(coords1))
        pg.click()

        time.sleep(2.5)
        coords2 = pg.locateOnScreen('./img/start2.PNG')
        pg.moveTo(pg.center(coords2))
        pg.click()

        coords3 = None
        while not coords3:
            # print('未找到')
            time.sleep(10)  # 每10秒找一次
            coords3 = pg.locateOnScreen('./img/end.PNG')
        pg.moveTo(pg.center(coords3))
        pg.click()
        time.sleep(4)


if __name__ == '__main__':
    dur, st = note()
    execute(dur, st)
    print(pg.position())  # 1571 906
    # time.sleep(3)
    # coords = pg.locateOnScreen('./img/start2.PNG')
    # pg.moveTo(pg.center(coords))


