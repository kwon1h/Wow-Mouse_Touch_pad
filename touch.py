from touch_sdk import Watch
import pyautogui
import time

pyautogui.PAUSE = 0.0001

class MyWatch(Watch):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.drag_start_x = None
        self.drag_start_y = None
        self.dragging = False
        self.scroll_speed = 80
        self.dpi_rate = 2

    def on_tap(self):
        print('탭')
        self.trigger_haptics(1.0, 100)

    def on_touch_down(self, x, y):
        print('터치 다운:', x, y)
        self.drag_start_x = x
        self.drag_start_y = y

    def on_touch_up(self, x, y):
        print('터치 업:', x, y)
        if self.dragging:
            self.dragging = False
            return
        if abs(self.drag_start_x - x) + abs(self.drag_start_y - y) < 10:
            pyautogui.click()

    def on_touch_move(self, x, y):
        if not self.dragging:
            if abs(self.drag_start_x - x) + abs(self.drag_start_y - y) > 10:
                self.dragging = True
        if self.dragging:
            move_x = self.dpi_rate * (x - self.drag_start_x)
            move_y = self.dpi_rate * (y - self.drag_start_y)
            pyautogui.moveRel(move_x,move_y)
            self.drag_start_x = x
            self.drag_start_y = y
    
    def on_rotary(self, direction):
        if direction*1 == 1:
            pyautogui.scroll(-self.scroll_speed)
            print("아래로 스크롤")
        elif direction*1 == -1:
            pyautogui.scroll(self.scroll_speed)
            print("위로 스크롤")

if __name__ == "__main__":
    watch = MyWatch('zxqa')
    watch.start()
