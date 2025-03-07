import pyautogui
from time import sleep

# Global variables to store the positions
upload_button = None
file_rename = None

file_offset = 20

def get_position(label):
    print(f"Move your mouse to {label} position and press Enter...")
    input()
    position = pyautogui.position()
    print(f"{label} position recorded: {position}")
    return position

def setup_positions():
    global upload_button, file_start, file_rename
    upload_button = get_position("Upload Button")
    file_rename = get_position("File Rename")

def upload_file(file_number):
    pyautogui.click(x=upload_button[0], y=upload_button[1])
    
    sleep(1.25)

    pyautogui.press('down', file_number)
    pyautogui.press('enter')

    sleep(1.5)

    pyautogui.click(x=file_rename[0], y=file_rename[1], clicks=2, interval=0.05)

    sleep(1.5)

def uploader():
    for file_num in range(41):
        for emoji_num in range(20):
            sleep(1)
            upload_file(file_num + 1)
            pyautogui.typewrite(f"_{emoji_num + 1}", interval=0.05)

if __name__ == "__main__":
    setup_positions()
    sleep(2)
    uploader()
