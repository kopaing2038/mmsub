# MMSUB MOVIES Telegram Bot
**A Telegram bot to upload mmsubtitle movies on your telegram channel**

## Features
- [X] MMSUBTITLE MOVIES.
- [X] MULTIPLE SCREENSHOTS.
- [X] CUSTOM WATERMARK AS SCREENSHOT LOGO.
- [X] MMSUB CHANNEL BUILDER (ie. UPLOAD MULTIPLE CHANNELMYANMAR MOVIES ON YOUR CHANNEL).
- [X] MOVIES DESRIPTION SUPPORT(MMSUBTITLE.CO & CHANNELMYANMAR.ORG).
- [X] ZAWGYI TO UNICODE AUTOCONVERTION.
- [X] JAV ADULT NSFW CHANNEL BUILDER (ie. UPLOAD A THOUNSAND OF JAV MOVIES ON YOUR CHANNEL).
- [X] EASY TO BUILD CHANNEL.

## ToDo 
- [ ] Handle more exceptions.
- [ ] LOGGER support.
- [ ] MMSUB CHANNEL BUILDER (ie. UPLOAD MULTIPLE MMSUBTITLE.CO MOVIES ON YOUR CHANNEL).
- [ ] DIRECT LINK TO UPLOAD MOVIES ON YOUR CHANNEL
- [ ] MULTIPLE CHANNELS SUPPORT

## Deploying

### Deploy on [Heroku](https://heroku.com)
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/modbots/mmsubmovies/main)

### Installation
- Install required modules.
```sh
apt install -y git python3 ffmpeg
```
- Clone this git repository.
```sh 
git clone ttps://github.com/modbots/mmsubmovies
```
- Change Directory
```sh 
cd mmsubmovies
```
- Install requirements with pip3
```sh 
pip3 install -r requirements.txt
```

### Configuration
**There are two Ways for configuring this bot.**
1. Add values to Environment Variables. And add a `ENV` var to Anything to enable it.
2. Add values in [config.py](./bot/config.py). And make sure that no `ENV` environment variables existing.

### Configuration Values
- `BOT_TOKEN` - Get it by contacting to [BotFather](https://t.me/botfather)
- `APP_ID` - Get it by creating app on [my.telegram.org](https://my.telegram.org/apps)
- `API_HASH` - Get it by creating app on [my.telegram.org](https://my.telegram.org/apps)
- `SUDO_USERS` - List of Telegram User ID of sudo users, seperated by space.
- `SUPPORT_CHAT_LINK` - Telegram invite link of support chat.
- `DATABASE_URL` - Postgres database url.
- `DOWNLOAD_DIRECTORY` - Custom path for downloads. Must end with a forward `/` slash. (Default to `./downloads/`)

### Deploy 
```sh 
python3 -m bot
```

## Credits
- [Dan](https://github.com/delivrance) for creating [PyroGram](https://pyrogram.org)
- [Spechide](https://github.com/Spechide) for [gDriveDB.py](./bot/helpers/sql_helper/gDriveDB.py)
- [Shivam Jha](https://github.com/lzzy12) for [Clone Feature](./bot/helpers/gdrive_utils/gDrive.py) from [python-aria-mirror-bot](https://github.com/lzzy12/python-aria-mirror-bot)

## Copyright & License
- Copyright (©) 2021 by [Moedyiu](https://github.com/modbots)
- Licensed under the terms of the [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](./LICENSE)
