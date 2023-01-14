import time

import easyocr
import numpy
from PIL import ImageGrab

from pymouse import PyMouse
import difflib

DEBUG = True

# 请自行修改为屏幕分辨率！
# Modify this!
screen_x = 1920 
screen_y = 1080


class Window:
    m = PyMouse()
    x_dim = 1920
    y_dim = 1080
    reader = easyocr.Reader(['ch_sim', 'en'])

    def __init__(self):
        self.x_dim, self.y_dim = self.m.screen_size()

    def resume_game(self):
        self.m.click(int(self.x_dim / 2 / 2), int(self.y_dim / 2 / 3))

    def right_click(self):
        self.m.click(int(self.x_dim / 2 / 2), int(self.y_dim / 2 / 2), button=2)

    def right_item(self):
        self.m.scroll(vertical=-1)

    def left_item(self):
        self.m.scroll(vertical=1)

    def eat(self):
        x, y = int(self.x_dim / 2 / 2), int(self.y_dim / 2 / 2)
        self.m.press(x, y, button=2)
        time.sleep(2)
        self.m.release(x, y, button=2)

    def get_sound(self) -> dict:
        image = ImageGrab.grab(bbox=(screen_x * 3 / 8, screen_y / 4, screen_x / 2, screen_y / 2))
        data = numpy.asarray(image)
        return self.osr(data)

    def osr(self, data):
        result = self.reader.readtext(data)
        # print(result)
        for i in result:
            like = difflib.SequenceMatcher(None,i[1], '免费训练30夯钟获得20000点经验').quick_ratio()
            like2 = difflib.SequenceMatcher(None,i[1], '免费训练5秒获得5点经验').quick_ratio()
            like3 = difflib.SequenceMatcher(None,i[1], '硼认').quick_ratio()
            like4 = difflib.SequenceMatcher(None,i[1], '确认').quick_ratio()
            click_x = int((i[0][0][0] + i[0][2][0])/2)
            click_y = int((i[0][0][1] + i[0][2][1])/2)
            if like > 0.95 or like3 > 0.95 or like4 > 0.95:
                self.m.click(click_x, click_y, 1, 2)
                time.sleep(1)
                self.m.click(int(100), int(100), 1, 1)
            else:
                self.m.click(int(100), int(100), 1, 1)

    
    def get_5_sec(self) -> dict:
        image = ImageGrab.grab(bbox=(0,0,screen_x/2,screen_y/2))
        data = numpy.asarray(image)
        return self.osr(data)


class GameState:
    PAUSE = 1
    HALT = 2
    FISHING = 3


if __name__ == '__main__':
    window = Window()

    while True:
        window.get_5_sec()
        time.sleep(1)
