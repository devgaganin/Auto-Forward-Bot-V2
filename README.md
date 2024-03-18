# Advance Content Saver Bot

Advance Telegram Bot that can work as Message/Files Forwarder from Restricted or Non-Restricted Channels/Groups/Bots. It can save files even if the channel have restrictions of forwarding or else.

## What can this bot do
- Forward public/private channel messages for private user login needed as forward method
- Save/clone individual post by its post link
- Can save multiple post link via `batch` command up to 10K

## Deployment Methods

### VPS Deployment

1. **Initial Setup**:
   - Edit both `__init__.py` and `config.py` files with your variables.

2. **Clone and Run**:
   - Clone your forked and edited repository:
     ```bash
     git clone forked_edited_repo_link
     ```
   - Navigate to the repository directory:
     ```bash
     cd repo_name
     ```
   - Copy `__init__.py` to the `src/devagagan` directory:
     ```bash
     cp __init__.py src/devagagan
     ```
   - Run the bot:
     ```bash
     python main.py && cd src && python -m devgagan
     ```

### Heroku Deployment

1. **Setup on Heroku**:
   - Go to [Heroku Dashboard](https://dashboard.heroku.com) and create a new app.
   - Connect your GitHub repository to Heroku.
   - Search and deploy the forked repository.
   - Back to the app view and refresh the page.

2. **Configure Dynos**:
   - Configure dynos for `devagagan1` and `devgagan2`.

## Additional Notes

- Make sure to replace `forked_edited_repo_link` with the link to your forked and edited repository.
- Replace `repo_name` with the name of your repository.
- Update the `__init__.py` and `config.py` files with your bot's specific variables before deployment.
- Ensure that your bot is configured correctly according to the requirements of the Telegram Bot API.

## How to edit `__init__.py`

```
# variables
API_ID = "1234567" #config("API_ID", default=None, cast=int)
API_HASH = "1167433546577f90e4519b65634b7" #config("API_HASH", default=None)
BOT_TOKEN = "7173773796:AAEYdIdgUg1_SYR7wSaMpgY0" #config("BOT_TOKEN", default=None)
SESSION = "BQHDMOUAIOGZHesmwkhKztZ1bU7NokB1HVLtNKHAnr35ElBp-FQ7IPkvayF0s5JoOGLN44ksi4kqeUNxnG56Vd8Mh_2Lo3ICHSN2J2u0WyYIOj96FBxN2gq_iekABQkL-vdXTB1DrOswqzBJBG9RaGPFVoiEYDAd0iD2vqgT3x2wOz98gBZNKPCGpWQYbGR6GKe66W5SRZRlLWJaEDQcTEIxNF48nIEGW7cwK2AG3eR4-iyVg5Zxaje_ACeNuCN5kLtQsNkGEV23f7-EdLQTG1zKnZ57AjUvYQdJ7o1pdGhkKknUUmOcfG4xn42RbHUwccqD1CmsGLU5Zh-vTbgBGh9AiP79HAAAAAGlHSMFAA" #config("SESSION", default=None)
FORCESUB = "channel username without @" #config("FORCESUB", default=None)
AUTH = "1234567" #config("AUTH", default=None)

```

## Commands Available in Bot - [TEAM SPY](https://t.me/dev_gagan)

- ```/start``` - to start the bot
- ```/batch``` - to download the files in range/bulk by giving one post link and range value
- ```/cancel``` - to cancel the onging /batch task
- ```/stats``` - to viewing the statics of bot
- ```/speedtest``` - can be executed by owner only
- ```/setchat``` - Set forwarding to a channel/group via channel/group ID including -100
- `/forward or /fwd` - to start forward
- `/settings` - to change settings for forward bot
- `restart` - to restart the bot
- `/resetall` - to reset unlink all other users / bot
- `/broadcast` - send bulk message to all users who ever have started the bot
- `/help` - get help about other commands

## Support

[<img src="https://img.icons8.com/ios/50/000000/instagram-new.png"/>](https://instagram.com/devagagn.in)
[<img src="https://img.icons8.com/ios/50/000000/youtube.png"/>](https://youtube.com/@dev_gagan)
[<img src="https://img.icons8.com/ios/50/000000/telegram-app.png"/>](https://t.me/dev_gagan)
[<img src="https://img.icons8.com/ios/50/000000/github--v1.png"/>](https://github.com/devgaganin)
[<img src="https://img.icons8.com/ios/50/000000/domain--v1.png"/>](https://devgagan.in)

## Terms of USE / Modification 
Visit [Terms](https://github.com/devgaganin/Save-Restricted-Content-Bot-Repo/blob/main/TERMS_OF_USE.md) and accept the guidelines.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
