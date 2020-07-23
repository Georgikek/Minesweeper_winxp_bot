import random
import pyautogui
import win32api
import win32con
import time
import keyboard


# кликает левой кнопкой мыши
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# кликает правой кнопкой мыши
def rclick(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)


# парсит
def xyi():
    pic = pyautogui.screenshot(region=(a[0][0][0], a[0][0][1], 480, 256))
    for inc3 in range(16):
        for inc4 in range(30):
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
            elif (red2, green2, blue2) == (128, 0, 0):
                b[inc3][inc4] = 5
            elif (red2, green2, blue2) == (0, 128, 128):
                b[inc3][inc4] = 6
            elif (red2, green2, blue2) == (0, 0, 0):
                b[inc3][inc4] = -1
            elif (red3, green3, blue3) == (192, 192, 192):
                b[inc3][inc4] = -2
    return


# проверка на бессмысленость
def proverka(x, y):
    for non1 in range(3):
        for non2 in range(3):
            if -1 < x-1+non1 < 16 and -1 < y-1+non2 < 30:
                if b[x-1+non1][y-1+non2] == 0:
                    return (True)
    return (False)


# ищет пустые клетки вокруг цифры
def kekich(lol1, lol2):
    parsefectplus[lol1][lol2] = 0
    parsefectpp[lol1][lol2] = 0
    for inc7 in range(3):
        for inc8 in range(3):
            if -1 < lol1 + inc7 - 1 < 16 and -1 < lol2 + inc8 - 1 < 30:
                if b[lol1 + inc7 - 1][lol2 + inc8 - 1] == 0:
                    parsefect[lol1][lol2][inc7][inc8] = 0
                    parsefectplus[lol1][lol2] += 1
                if b[lol1 + inc7 - 1][lol2 + inc8 - 1] == -1:
                    parsefectpp[lol1][lol2] += 1
    if parsefect[lol1][lol2] == [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]:
        parsefect[lol1][lol2][0][0] = -2


a = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
i = 0
pos_face = pyautogui.locateOnScreen('C:\mbot\Lico.png')
# запоминает положения всех клеток
for pos in pyautogui.locateAllOnScreen('C:\mbot\Kletka.png'):
    a[i // 30].append(pos)
    i += 1
while keyboard.is_pressed('q') == False:
    r = True
    b = [[0 for c in range(30)] for m in range(16)]
    polesovpod = [[[-1 for c1 in range(2)] for c in range(7)] for m in range(7)]
    parsefect = [[[[-1 for c1 in range(3)] for m1 in range(3)] for c in range(30)] for m in range(16)]
    parsefectplus = [[0 for c in range(30)] for m in range(16)]
    parsefectpp = [[0 for c in range(30)] for m in range(16)]
    i = random.randint(0, 15)
    click(x=a[i][i][0] + 9, y=a[i][i][1] + 9)
    click(x=a[i][i][0] + 9, y=a[i][i][1] + 9)
    xyi()
    timee = time.time()
    while r:
        p = False
        for inc1 in range(16):
            for inc2 in range(30):
                if proverka(inc1, inc2):
                    q = False
                    z = 0
                    # блок на 1
                    if b[inc1][inc2] == 1:
                        for v in range(3):
                            for c in range(3):
                                if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                    if b[inc1 + v - 1][inc2 + c - 1] == -1:
                                        q = True
                                        break
                        if q:
                            for v in range(3):
                                for c in range(3):
                                    if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                        if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                            click(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                                  y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                            p = True
                            xyi()
                        else:
                            for v in range(3):
                                for c in range(3):
                                    if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                        if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                            z += 1
                                            if z > 1:
                                                break
                                if z > 1:
                                    break
                            if z == 1:
                                for v in range(3):
                                    for c in range(3):
                                        if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                            if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                                rclick(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                                       y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                                p = True
                                xyi()
                                for v in range(3):
                                    for c in range(3):
                                        if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                            if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                                click(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                                      y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                                p = True
                                xyi()
                    q = False
                    z = 0
                    # блок на 2
                    if b[inc1][inc2] == 2:
                        for v in range(3):
                            for c in range(3):
                                if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                    if b[inc1 + v - 1][inc2 + c - 1] == -1:
                                        q += 1
                                        if q == 2:
                                            break
                            if q == 2:
                                break
                        if q == 2:
                            for v in range(3):
                                for c in range(3):
                                    if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                        if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                            click(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                                  y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                            p = True
                            xyi()
                        else:
                            for v in range(3):
                                for c in range(3):
                                    if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                        if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                            z += 1
                                            if z > 2:
                                                break
                                if z > 2:
                                    break
                            if z == 2 and q == 0 or z == 1 and q == 1:
                                for v in range(3):
                                    for c in range(3):
                                        if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                            if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                                rclick(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                                       y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                                p = True
                                xyi()
                                for v in range(3):
                                    for c in range(3):
                                        if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                            if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                                click(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                                      y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                                p = True
                                xyi()
                    q = False
                    z = 0
                    # блок на 3
                    if b[inc1][inc2] == 3:
                        for v in range(3):
                            for c in range(3):
                                if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                    if b[inc1 + v - 1][inc2 + c - 1] == -1:
                                        q += 1
                                        if q == 3:
                                            break
                            if q == 3:
                                break
                        if q == 3:
                            for v in range(3):
                                for c in range(3):
                                    if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                        if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                            click(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                                  y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                            p = True
                            xyi()
                        else:
                            for v in range(3):
                                for c in range(3):
                                    if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                        if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                            z += 1
                                            if z > 3:
                                                break
                                if z > 3:
                                    break
                            if z == 3 and q == 0 or z == 2 and q == 1 or z == 1 and q == 2:
                                for v in range(3):
                                    for c in range(3):
                                        if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                            if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                                rclick(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                                       y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                                p = True
                                xyi()
                                for v in range(3):
                                    for c in range(3):
                                        if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                            if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                                click(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                                      y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                                p = True
                                xyi()
                    q = False
                    z = 0
                    # блок на 4
                    if b[inc1][inc2] == 4:
                        for v in range(3):
                            for c in range(3):
                                if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                    if b[inc1 + v - 1][inc2 + c - 1] == -1:
                                        q += 1
                                        if q == 4:
                                            break
                            if q == 4:
                                break
                        if q == 4:
                            for v in range(3):
                                for c in range(3):
                                    if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                        if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                            click(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                                  y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                            p = True
                            xyi()
                        else:
                            for v in range(3):
                                for c in range(3):
                                    if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                        if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                            z += 1
                                            if z > 4:
                                                break
                                if z > 4:
                                    break
                            if z == 4 and q == 0 or z == 3 and q == 1 or z == 2 and q == 2 or z == 1 and q == 3 or z == 0 and q == 4:
                                for v in range(3):
                                    for c in range(3):
                                        if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                            if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                                rclick(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                                       y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                                p = True
                                xyi()
                                for v in range(3):
                                    for c in range(3):
                                        if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                            if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                                click(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                                      y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                                p = True
                                xyi()
                    q = False
                    z = 0
                    # блок на 5
                    if b[inc1][inc2] == 5:
                        for v in range(3):
                            for c in range(3):
                                if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                    if b[inc1 + v - 1][inc2 + c - 1] == -1:
                                        q += 1
                                        if q == 5:
                                            break
                            if q == 5:
                                break
                        if q == 5:
                            for v in range(3):
                                for c in range(3):
                                    if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                        if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                            click(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                                  y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                            p = True
                            xyi()
                        else:
                            for v in range(3):
                                for c in range(3):
                                    if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                        if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                            z += 1
                                            if z > 5:
                                                break
                                if z > 4:
                                    break
                            if z == 5 and q == 0 or z == 4 and q == 1 or z == 3 and q == 2 or z == 2 and q == 3 or z == 1 and q == 4 or z == 0 and q == 5:
                                for v in range(3):
                                    for c in range(3):
                                        if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                            if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                                rclick(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                                       y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                                p = True
                                xyi()
                                for v in range(3):
                                    for c in range(3):
                                        if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                            if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                                click(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                                      y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                                p = True
                                xyi()
                    q = False
                    z = 0
                    # блок на 6
                    if b[inc1][inc2] == 6:
                        for v in range(3):
                            for c in range(3):
                                if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                    if b[inc1 + v - 1][inc2 + c - 1] == -1:
                                        q += 1
                                        if q == 6:
                                            break
                            if q == 6:
                                break
                        if q == 6:
                            for v in range(3):
                                for c in range(3):
                                    if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                        if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                            click(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                                  y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                            p = True
                            xyi()
                        else:
                            for v in range(3):
                                for c in range(3):
                                    if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                        if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                            z += 1
                                            if z > 6:
                                                break
                                if z > 6:
                                    break
                            if z == 6 and q == 0 or z == 5 and q == 1 or z == 4 and q == 2 or z == 3 and q == 3 or z == 2 and q == 4 or z == 1 and q == 5 or z == 0 and q == 6:
                                for v in range(3):
                                    for c in range(3):
                                        if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                            if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                                rclick(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                                       y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                                p = True
                                xyi()
                                for v in range(3):
                                    for c in range(3):
                                        if -1 < inc1 + v - 1 < 16 and -1 < inc2 + c - 1 < 30:
                                            if b[inc1 + v - 1][inc2 + c - 1] == 0:
                                                click(x=a[inc1 + v - 1][inc2 + c - 1][0] + 9,
                                                      y=a[inc1 + v - 1][inc2 + c - 1][1] + 9)
                                                p = True
                                xyi()
        # блок сложной логики
        if not p:
            for inc1 in range(16):
                if p:
                    break
                for inc2 in range(30):
                    if p:
                        break
                    if proverka(inc1, inc2):
                        if b[inc1][inc2] > 0:
                            if parsefect[inc1][inc2] != [[-2, -1, -1], [-1, -1, -1], [-1, -1, -1]]:
                                kekich(inc1, inc2)
                            for v in range(5):
                                if p:
                                    break
                                for c in range(5):
                                    if p:
                                        break
                                    if proverka(inc1 + v - 2, inc2 + c - 2):
                                        if -1 < inc1 + v - 2 < 16 and -1 < inc2 + c - 2 < 30:
                                            if b[inc1 + v - 2][inc2 + c - 2] > 0 and not (v == 2 and c == 2):
                                                ten = False
                                                net = False
                                                tennet = False
                                                polesovpod = [[[-1 for c1 in range(2)] for ttt in range(7)] for m in range(7)]
                                                if parsefect[inc1 + v - 2][inc2 + c - 2] != [[-2, -1, -1], [-1, -1, -1], [-1, -1, -1]]:
                                                    kekich(inc1 + v - 2, inc2 + c - 2)
                                                    if parsefect[inc1 + v - 2][inc2 + c - 2] != [[-2, -1, -1], [-1, -1, -1], [-1, -1, -1]]:
                                                        for inc9 in range(3):
                                                            for inc10 in range(3):
                                                                if parsefect[inc1][inc2][inc9][inc10] == 0:
                                                                    polesovpod[inc9 + 2][inc10 + 2][0] = 0
                                                                if parsefect[inc1 + v - 2][inc2 + c - 2][inc9][inc10] == 0:
                                                                    polesovpod[inc9 + v][inc10 + c][1] = 0
                                                        for inc9 in range(7):
                                                            for inc10 in range(7):
                                                                if polesovpod[inc9][inc10][0] == 0 and polesovpod[inc9][inc10][1] == -1:
                                                                    net = True
                                                                if polesovpod[inc9][inc10][0] == -1 and polesovpod[inc9][inc10][1] == 0:
                                                                    ten = True
                                                                if polesovpod[inc9][inc10][0] == 0 and polesovpod[inc9][inc10][1] == 0:
                                                                    tennet = True
                                                        if ((net or ten) and not (net and ten)) and tennet:
                                                            if net:
                                                                if b[inc1][inc2] - parsefectpp[inc1][inc2] - b[inc1 + v - 2][inc2 + c - 2] + parsefectpp[inc1 + v - 2][inc2 + c - 2] == parsefectplus[inc1][inc2] - parsefectplus[inc1 + v - 2][inc2 + c - 2]:
                                                                    for inc9 in range(7):
                                                                        for inc10 in range(7):
                                                                            if polesovpod[inc9][inc10][0] == 0 and polesovpod[inc9][inc10][1] == -1:
                                                                                if -1 < inc1-3+inc9 < 16 and -1 < inc2-3+inc10 < 30:
                                                                                    if b[inc1-3+inc9][inc2-3+inc10] == 0:
                                                                                        rclick(a[inc1-3+inc9][inc2-3+inc10][0]+9, a[inc1-3+inc9][inc2-3+inc10][1]+9)
                                                                                        p = True
                                                                                        xyi()
                                                                if b[inc1][inc2] - parsefectpp[inc1][inc2] == b[inc1 + v - 2][inc2 + c - 2] - parsefectpp[inc1 + v - 2][inc2 + c - 2]:
                                                                    for inc9 in range(7):
                                                                        for inc10 in range(7):
                                                                            if polesovpod[inc9][inc10][0] == 0 and polesovpod[inc9][inc10][1] == -1:
                                                                                if -1 < inc1-3+inc9 < 16 and -1 < inc2-3+inc10 < 30:
                                                                                    if b[inc1-3+inc9][inc2-3+inc10] == 0:
                                                                                        click(a[inc1-3+inc9][inc2-3+inc10][0]+9, a[inc1-3+inc9][inc2-3+inc10][1]+9)
                                                                                        p = True
                                                                                        xyi()
                                                            if ten:
                                                                if b[inc1 + v - 2][inc2 + c - 2] - parsefectpp[inc1 + v - 2][inc2 + c - 2] - b[inc1][inc2] + parsefectpp[inc1][inc2] == parsefectplus[inc1 + v - 2][inc2 + c - 2] - parsefectplus[inc1][inc2]:
                                                                    for inc9 in range(7):
                                                                        for inc10 in range(7):
                                                                            if polesovpod[inc9][inc10][0] == -1 and polesovpod[inc9][inc10][1] == 0:
                                                                                if -1 < inc1-3+inc9 < 16 and -1 < inc2-3+inc10 < 30:
                                                                                    if b[inc1-3+inc9][inc2-3+inc10] == 0:
                                                                                        rclick(a[inc1-3+inc9][inc2-3+inc10][0]+9, a[inc1-3+inc9][inc2-3+inc10][1]+9)
                                                                                        p = True
                                                                                        xyi()
                                                                if b[inc1 + v - 2][inc2 + c - 2] - parsefectpp[inc1 + v - 2][inc2 + c - 2] == b[inc1][inc2] - parsefectpp[inc1][inc2]:
                                                                    for inc9 in range(7):
                                                                        for inc10 in range(7):
                                                                            if polesovpod[inc9][inc10][0] == -1 and polesovpod[inc9][inc10][1] == 0:
                                                                                if -1 < inc1-3+inc9 < 16 and -1 < inc2-3+inc10 < 30:
                                                                                    if b[inc1-3+inc9][inc2-3+inc10] == 0:
                                                                                        click(a[inc1-3+inc9][inc2-3+inc10][0]+9, a[inc1-3+inc9][inc2-3+inc10][1]+9)
                                                                                        p = True
                                                                                        xyi()
        # блок случайных нажатий
        if not p:
            while True:
                i = random.randint(0, 15)
                k = random.randint(0, 29)
                if b[i][k] == 0:
                    while keyboard.is_pressed('w'):
                        time.sleep(0.5)
                    click(x=a[i][k][0] + 9, y=a[i][k][1] + 9)
                    xyi()
                    break
        r = not pyautogui.pixelMatchesColor(pos_face[0] + 9, pos_face[1] + 17,
                                            (0, 0, 0)) and not pyautogui.pixelMatchesColor(pos_face[0] + 7,
                                                                                           pos_face[1] + 12, (0, 0, 0))
    if pyautogui.pixelMatchesColor(pos_face[0] + 7, pos_face[1] + 12, (0, 0, 0)):
        print(time.time() - timee)
    click(pos_face[0] + 10, pos_face[1] + 18)
