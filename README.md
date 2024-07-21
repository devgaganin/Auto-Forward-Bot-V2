# Advance Content Saver Bot

Advance Telegram Bot that can work as Message/Files Forwarder from Restricted or Non-Restricted Channels/Groups/Bots. It can save files even if the channel have restrictions of forwarding or else.

## What can this bot do
- Forward public/private channel messages for private user login needed as forward method
- Save/clone individual post by its post link
- Can save multiple post link via `batch` command up to 10K

## Deployment Methods

### VPS Deployment

1. **Initial Setup**:
   -`config.py` files with your variables.

2. **Clone and Run**:
   - Clone your forked and edited repository:
     ```bash
     git clone forked_edited_repo_link
     ```
   - Navigate to the repository directory:
     ```bash
     cd repo_name
     ```
   - Run the bot:
     ```bash
     python main.py
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

## Commands Available in Bot - [TEAM SPY](https://t.me/dev_gagan)

- ```/start``` - to start the bot
- ```/cancel``` - to cancel the onging /batch task
- ```/stats``` - to viewing the statics of bot
- `/forward or /fwd` - to start forward
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
