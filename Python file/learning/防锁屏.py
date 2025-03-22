import time
import pyautogui
print("run in.....")
while True:
    # 移动鼠标
    pyautogui.moveRel(10, 0, duration=0.1)  # 向右移动
    pyautogui.moveRel(-10, 0, duration=0.1)  # 回移
    # 模拟鼠标点击
    pyautogui.click()
    # 模拟键盘按键（如按空格）
    pyautogui.press('space')
    time.sleep(5*60)  # 间隔5分钟执行一次

