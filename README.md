Discord bot sample
==================

### Refs
- Discord
  - portal ... https://discord.com/developers/applications
  - docs ..... https://discord.com/developers/docs/intro
- discord.py
  - github ... https://github.com/Rapptz/discord.py
  - docs ..... https://discordpy.readthedocs.io/en/latest/#
  - sample ... https://github.com/Rapptz/RoboDanny


### Prepare the Discord Bot
#### 1. Create the discord bot.
- open: https://discord.com/developers/applications
- 'New Application' > Enter "Name" > 'Create'
- application page > Left Pane 'Bot' > Bild-A-Bot 'Add Bot' > 'Yes, do it!'

#### 2. Get the bot token.
- open: https://discord.com/developers/applications, goto bot page.
- Build-A-Bot pane > Token: 'Copy'

#### 3. Invite a bot to your guild (server).
- open: https://discord.com/developers/applications, goto bot page.
- Left Pane 'OAuth2' > SCOPES: check 'bot'
- Copy URL, and then open browser.
- Invite bot to your guild.


### How to use

1. Setup config.py

```sh
$ cp ./bot/config.py.sample ./bot/config.py
```

2. Add your token to config.py

```config.py
# BOT
bot_token = "xxxxxxxxxxxxxxx" # <--- bot token
```

3. Run

```sh
$ docker-compose build
$ docker-compose run bot python bot.py
Logged in as: sample app (ID: 747806654476714056)
```

4. Check your discord guild, and use command!

```discord
user: >hello
bot: hello, user.
```

