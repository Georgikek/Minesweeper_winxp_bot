import random
import pyautogui
import win32api
import win32con
import time
import keyboard


def click(x, y):  # кликает левой кнопкой мыши
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def rclick(x, y):  # кликает правой кнопкой мыши
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)


def xyi():  # парсит
    pic = pyautogui.screenshot(region=(a[0][0][0], a[0][0][1], 144, 144))
    for inc3 in range(9):
        for inc4 in range(9):
            red1, green1, blue1 = pic.getpixel((inc4 * 16 + 9, inc3 * 16 + 9))
            red2, green2, blue2 = pic.getpixel((inc4 * 16 + 8, inc3 * 16 + 8))
            red3, green3, blue3 = pic.getpixel((inc4 * 16 + 1, inc3 * 16 + 1))
            if (red1, green1, blue1) == (0, 0, 255):
                b[inc3][inc4] = 1
            elif (red2, green2, blue2) == (0, 128, 0):
                b[inc3][inc4] = 2
            elif (red2, green2, blue2) == (255, 0, 0):
                b[inc3][inc4] = 3
            elif (red2, green2, blue2) == (0, 0, 128):
                b[inc3][inc4] = 4
            elif (red2, green2, blue2) == (0, 0, 0):
                b[inc3][inc4] = -1
            elif (red3, green3, blue3) == (192, 192, 192):
                b[inc3][inc4] = -2
    return


a = [[], [], [], [], [], [], [], [], []]
i = 0
pos_face = pyautogui.locateOnScreen('C:\mbot\Lico.png')
for pos in pyautogui.locateAllOnScreen('C:\mbot\Kletka.png'):  # запоминает положения всех клеток
    a[i // 9].append(pos)
    i += 1
while keyboard.is_pressed('q') == False:
    r = True
    b = [[0 for c in range(9)] for m in range(9)]
    i = random.randint(0, 8)
    click(x=a[i][i][0] + 9, y=a[i][i][1] + 9)
    click(x=a[i][i][0] + 9, y=a[i][i][1] + 9)
    time.sleep(0.1)
    xyi()
    timee = time.time()
    while r:
        p = False
        for inc1 in range(9):
            for inc2 in range(9):
                q = False
                z = 0
                if b[inc1][inc2] == 1:  # блок на 1
                    for v in range(3):
                        for c in range(3):
                            if -1 < inc1 + v - 1 < 9 and -1 < inc2 + c - 1 < 9:
                                if b[inc1 + v - 1][inc2 + c - 1] == -1:
                                    q = True
                                    break
                    if q:
                        for v in range(3):
                            for c in range(3):
                                if -1 < inc1 + v - 1 < 9 and -1 < inc2 + c - 1 < 9:
                                    if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                        click(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                              y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                        p = True
                        xyi()
                    else:
                        for v in range(3):
                            for c in range(3):
                                if -1 < inc1 + v - 1 < 9 and -1 < inc2 + c - 1 < 9:
                                    if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                        z += 1
                                        if z > 1:
                                            break
                            if z > 1:
                                break
                        if z == 1:
                            for v in range(3):
                                for c in range(3):
                                    if -1 < inc1 + v - 1 < 9 and -1 < inc2 + c - 1 < 9:
                                        if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                            rclick(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                                   y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                            p = True
                            xyi()
                            for v in range(3):
                                for c in range(3):
                                    if -1 < inc1 + v - 1 < 9 and -1 < inc2 + c - 1 < 9:
                                        if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                            click(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                                  y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                            p = True
                            xyi()
                q = False
                z = 0
                if b[inc1][inc2] == 2:  # блок на 2
                    for v in range(3):
                        for c in range(3):
                            if -1 < inc1 + v - 1 < 9 and -1 < inc2 + c - 1 < 9:
                                if b[inc1 + v - 1][inc2 + c - 1] == -1:
                                    q += 1
                                    if q == 2:
                                        break
                        if q == 2:
                            break
                    if q == 2:
                        for v in range(3):
                            for c in range(3):
                                if -1 < inc1 + v - 1 < 9 and -1 < inc2 + c - 1 < 9:
                                    if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                        click(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                              y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                        p = True
                        xyi()
                    else:
                        for v in range(3):
                            for c in range(3):
                                if -1 < inc1 + v - 1 < 9 and -1 < inc2 + c - 1 < 9:
                                    if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                        z += 1
                                        if z > 2:
                                            break
                            if z > 2:
                                break
                        if z == 2 and q == 0 or z == 1 and q == 1:
                            for v in range(3):
                                for c in range(3):
                                    if -1 < inc1 + v - 1 < 9 and -1 < inc2 + c - 1 < 9:
                                        if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                            rclick(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                                   y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                            p = True
                            xyi()
                            for v in range(3):
                                for c in range(3):
                                    if -1 < inc1 + v - 1 < 9 and -1 < inc2 + c - 1 < 9:
                                        if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                            click(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                                  y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                            p = True
                            xyi()
                q = False
                z = 0
                if b[inc1][inc2] == 3:  # блок на 3
                    for v in range(3):
                        for c in range(3):
                            if -1 < inc1 + v - 1 < 9 and -1 < inc2 + c - 1 < 9:
                                if b[inc1 + v - 1][inc2 + c - 1] == -1:
                                    q += 1
                                    if q == 3:
                                        break
                        if q == 3:
                            break
                    if q == 3:
                        for v in range(3):
                            for c in range(3):
                                if -1 < inc1 + v - 1 < 9 and -1 < inc2 + c - 1 < 9:
                                    if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                        click(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                              y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                        p = True
                        xyi()
                    else:
                        for v in range(3):
                            for c in range(3):
                                if -1 < inc1 + v - 1 < 9 and -1 < inc2 + c - 1 < 9:
                                    if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                        z += 1
                                        if z > 3:
                                            break
                            if z > 3:
                                break
                        if z == 3 and q == 0 or z == 2 and q == 1 or z == 1 and q == 2:
                            for v in range(3):
                                for c in range(3):
                                    if -1 < inc1 + v - 1 < 9 and -1 < inc2 + c - 1 < 9:
                                        if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                            rclick(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                                   y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                            p = True
                            xyi()
                            for v in range(3):
                                for c in range(3):
                                    if -1 < inc1 + v - 1 < 9 and -1 < inc2 + c - 1 < 9:
                                        if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                            click(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                                  y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                            p = True
                            xyi()
                q = False
                z = 0
                if b[inc1][inc2] == 4:  # блок на 4
                    for v in range(3):
                        for c in range(3):
                            if -1 < inc1 + v - 1 < 9 and -1 < inc2 + c - 1 < 9:
                                if b[inc1 + v - 1][inc2 + c - 1] == -1:
                                    q += 1
                                    if q == 4:
                                        break
                        if q == 4:
                            break
                    if q == 4:
                        for v in range(3):
                            for c in range(3):
                                if -1 < inc1 + v - 1 < 9 and -1 < inc2 + c - 1 < 9:
                                    if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                        click(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                              y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                        p = True
                        xyi()
                    else:
                        for v in range(3):
                            for c in range(3):
                                if -1 < inc1 + v - 1 < 9 and -1 < inc2 + c - 1 < 9:
                                    if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                        z += 1
                                        if z > 4:
                                            break
                            if z > 4:
                                break
                        if z == 4 and q == 0 or z == 3 and q == 1 or z == 2 and q == 2 or z == 1 and q == 3 or z == 0 and q == 4:
                            for v in range(3):
                                for c in range(3):
                                    if -1 < inc1 + v - 1 < 9 and -1 < inc2 + c - 1 < 9:
                                        if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                            rclick(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                                   y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                            p = True
                            xyi()
                            for v in range(3):
                                for c in range(3):
                                    if -1 < inc1 + v - 1 < 9 and -1 < inc2 + c - 1 < 9:
                                        if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                            click(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                                  y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                            p = True
                            xyi()
        if not p:  # блок случайных нажатий
            while True:
                i = random.randint(0, 8)
                k = random.randint(0, 8)
                if b[i][k] == 0:
                    click(x=a[i][k][0] + 9, y=a[i][k][1] + 9)
                    time.sleep(0.1)
                    xyi()
                    break
        r = not pyautogui.pixelMatchesColor(pos_face[0] + 9, pos_face[1] + 17, (0, 0, 0)) and not pyautogui.pixelMatchesColor(pos_face[0] + 7, pos_face[1] + 12, (0, 0, 0))
    if pyautogui.pixelMatchesColor(pos_face[0] + 7, pos_face[1] + 12, (0, 0, 0)):
        print(time.time() - timee)
    click(pos_face[0] + 10, pos_face[1] + 18)
