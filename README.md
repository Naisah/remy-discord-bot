# Remy Discord Bot

A Discord bot themed after Remy from Ratatouille, built with `discord.py` and modular cogs.

## Features
- **General Commands**: `!ping`, `!say`, `!userinfo`
- **Remy's Kitchen Cogs**:
  - `!cook` - Remy suggests gourmet recipes or evaluates ingredient pairings.
  - `!rate [dish]` - Let Remy critique your food choices (he holds nothing back!).
  - `!gusteau` - Motivational quotes from Chef Gusteau.
- **Moderation / Extensions**: Dynamic cog reloading (`!load`, `!unload`).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Naisah/remy-discord-bot.git
   cd remy-discord-bot
   ```

2. Install the required libraries:
   ```bash
   pip install discord.py python-dotenv
   ```

3. Create a `.env` file in the root folder and add your Discord bot token:
   ```env
   DISCORD_TOKEN=your_token_here
   ```

4. Start the bot:
   ```bash
   python main.py
   ```
