import pyautogui
from time import sleep

upload_button = (1370, -630)
file_start = (2000, -490)
file_rename = (1530, -416)
file_offset = 20

def poll_position():
    while True:
        print(pyautogui.position())

def upload_file(offset):
    pyautogui.click(x=upload_button[0], y=upload_button[1])
    
    sleep(.5)

    pyautogui.click(x=file_start[0], y=file_start[1] + offset)
    pyautogui.press('enter')

    sleep(1.5)

    pyautogui.click(x=file_rename[0], y=file_rename[1], clicks=2, interval=0.05)

    sleep(1)

def uploader():
    for i in range(14):
        for j in range(4):
            upload_file(file_offset * i)
            pyautogui.typewrite(f"_{j + 1}", interval=0.05)
            sleep(1)

if __name__ == "__main__":
    sleep(2)
    # poll_position()
    uploader()
