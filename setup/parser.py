from bs4 import BeautifulSoup
import yaml

with open("html/p1.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

emoji_names = [inp.get("value").strip() for inp in soup.find_all("input", class_="inputMini-Un2tP4 input-2g-os5")]
emoji_ids = [span.text.strip() for span in soup.find_all("span", class_="cellId--lByq3")]

emoji_dict = {name: f"<:{name}:{eid}>" for name, eid in zip(emoji_names, emoji_ids)}

with open("../emojis.yaml", "w") as f:
    f.write("---\n")
    yaml.dump(emoji_dict, f, indent=4)
