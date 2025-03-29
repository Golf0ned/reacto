<div align="center">
<pre>
                                        █████            
                                       ░░███             
 ████████   ██████   ██████    ██████  ███████    ██████ 
░░███░░███ ███░░███ ░░░░░███  ███░░███░░░███░    ███░░███
 ░███ ░░░ ░███████   ███████ ░███ ░░░   ░███    ░███ ░███
 ░███     ░███░░░   ███░░███ ░███  ███  ░███ ███░███ ░███
 █████    ░░██████ ░░████████░░██████   ░░█████ ░░██████ 
░░░░░      ░░░░░░   ░░░░░░░░  ░░░░░░     ░░░░░   ░░░░░░  
  
---
discord bot that reacts words to messages
</pre>
</div>

Ever seen a discord message, and wanted to do this, but couldn't because there's duplicate letters?

![image](https://github.com/user-attachments/assets/b1ce7666-2e3d-4161-ac6d-a7823137e989)

Well, now you can.

## Features & Commands

### Message React

### React Log

## Installation

### Using the Public Bot

Public bot invite coming soon.

### Hosting it Yourself

1. Clone the repo. Create + activate a virtual environment with your preferred python package manager.
2. Install requirements from `requirements.txt`.
3. Make a copy of `secrets.example.yaml` and rename it `secrets.yaml`.
4. Create an app on the [discord dev portal](https://discord.com/developers/applications).
5. Copy your bot token (`Applications -> <your-bot> -> Bot -> Token -> Reset Token`), and put it in `secrets.yaml`.
6. Use the scripts in `setup/` to a) upload all emojis, and b) generate `emojis.yaml`.
7. Run the bot, and invite it to your server.
8. Happy reacting :)

## To-Do
- [x] Initial bot buildout
- [ ] Add more assets to the bot
- [ ] Update setup scripts
- [ ] React log
- [ ] Make modal inputs less ambiguous
- [ ] Finish documentation
