# Advance Content Saver Bot

Advance Telegram Bot that can work as Message/Files Forwarder from Restricted or Non-Restricted Channels/Groups/Bots.

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

## Support

[![Instagram](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/768px-Instagram_icon.png)](https://instagram.com/devagagn.in)
[![YouTube](https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png)](https://youtube.com/dev_gagan)
[![Telegram](https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/1024px-Telegram_logo.svg.png)](https://t.me/dev_gagan)
[![GitHub](https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg)](https://github.com/devgaganin)
[![Website](https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Font_Awesome_5_brands_website.svg/1024px-Font_Awesome_5_brands_website.svg.png)](https://devgagan.in)

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
