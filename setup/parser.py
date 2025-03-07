from time import sleep
from bs4 import BeautifulSoup
import yaml
import pyperclip
import pyautogui

html_location = None
next_button = None

def get_position(label):
    print(f"Move your mouse to {label} position and press Enter...")
    input()
    position = pyautogui.position()
    print(f"{label} position recorded: {position}")
    return position

def setup_positions():
    global html_location, next_button 
    html_location = get_position("Html Location")
    next_button = get_position("Next button")

def copy_html():
    # Open data options
    pyautogui.rightClick()
    sleep(.15)

    pyautogui.press('down', presses=13)

    sleep(.15)

    # Enter copy options
    pyautogui.press('enter')
    sleep(.15)

    # Copy 
    pyautogui.press('enter')
    sleep(.15)

def save_content():
    html_content = pyperclip.paste()

    with open("html/data.html", "a", encoding='utf-8') as f:
        f.write(html_content)
        f.write("\n\n")

def get_html_pages(end_page):
    for i in range(end_page):
        if i > 0:
            pyautogui.click(x=next_button[0], y=next_button[1])
        pyautogui.click(x=html_location[0], y=html_location[1])
        copy_html()
        save_content()
        sleep(.5)
        
        print(f"wrote the {i + 1} page")


def parse_and_save():
    with open("html/data.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    emoji_names = [inp.get("value").strip() for inp in soup.find_all("input", class_="inputMini-Un2tP4 input-2g-os5")]
    emoji_ids = [span.text.strip() for span in soup.find_all("span", class_="cellId--lByq3")]

    emoji_dict = {}

    special_key_map = {
        "space": " ",
        "exclamation": "!",
        "question": "?"
    }

    for name, eid in zip(emoji_names, emoji_ids):
        parts = name.split("_")
        if len(parts) < 3:
            continue  

        key = parts[1]  # like 'k', 'space', 'explanation', etc.

        # Check if the key is a special mapped key
        key = special_key_map.get(key, key)

        full_emoji = f"<:{name}:{eid}>"

        if key not in emoji_dict:
            emoji_dict[key] = []

        emoji_dict[key].append(full_emoji)

    # Write grouped emojis to YAML
    with open("../emojis.yaml", "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.dump(emoji_dict, f, default_flow_style=False, indent=2, default_style='"')


if __name__ == "__main__":

    setup_positions()
    print("Move to discord page in next 3 seconds...")
    sleep(3)
    # 32 is num pages i had after uploads
    get_html_pages(32)

    parse_and_save()



