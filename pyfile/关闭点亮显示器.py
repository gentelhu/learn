import keyboard
import time
import ctypes
import pyautogui

# 关闭显示器
def turn_off_display():
    ctypes.windll.user32.SendMessageW(65535, 274, 61808, 2)

# 打开显示器（模拟按下电源键，可能不适用于所有系统）
def turn_on_display():
    # 模拟鼠标移动以唤醒系统
    pyautogui.moveRel(1, 1)
    pyautogui.moveRel(-1, -1)
    ctypes.windll.user32.SendMessageW(65535, 274, 61808, -1)

display_off = False

def toggle_display(event):
    global display_off
    if event.name == 'f12':
        if not display_off:
            turn_off_display()
            display_off = True
        else:
            turn_on_display()
            display_off = False

keyboard.on_press(toggle_display)
print("程序已启动，按下F12键可以关闭或打开显示器。")
while True:
    time.sleep(0.1)
    