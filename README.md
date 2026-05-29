# 🤖 Remy Discord Bot

A sleek, modern, and modular Discord bot built with Python using `discord.py`. Remy features a robust command system, custom commands, and a modular architecture utilizing Cogs for event handling and modular extensions.

This repository is designed with security best practices in mind, keeping credentials safe while showcasing a clean bot structure for portfolio presentation.

---

## ✨ Features

- **🚀 Modular Cog System**: Dynamically load and unload bot features (Cogs) without restarting the entire bot.
- **💬 Custom Commands**:
  - `!ping` - Quick connection check (returns a pong!).
  - `!say [message]` - Echoes a message back to the channel.
  - `!userinfo [user]` - Retrieves and displays user IDs.
- **😎 Cog Events & Commands**:
  - `!cool` - Sends a cool sunglasses emoji (`:sunglasses:`).
  - Handles the `on_ready` event modularly to confirm Cog loading.
- **🔒 Secure Credentials**: Utilizes `python-dotenv` to manage secrets locally, preventing sensitive Discord bot tokens from being exposed to GitHub.

---

## 📂 Project Structure

```text
├── cogs/
│   └── events.py       # Modular Cog containing events and command examples
├── main.py             # Entry point of the bot (initializes connection & loads Cogs)
├── utils.py            # Utility module defining Cog structure
├── .env.example        # Reference file for environment variables
├── .gitignore          # Keeps secrets and python cache out of version control
└── README.md           # Project documentation and showcase
```

---

## 🛠️ Setup & Installation

To run this bot locally, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/Naisah/remy-discord-bot.git
cd remy-discord-bot
```

### 2. Install Dependencies
Make sure you have Python installed, then install the required libraries:
```bash
pip install discord.py python-dotenv
```

### 3. Configure Credentials (Securely!)
1. Duplicate the `.env.example` file and rename it to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and replace `your_discord_bot_token_here` with your actual Discord Bot Token:
   ```env
   DISCORD_TOKEN=your_actual_token_here
   ```
   *(Note: The `.env` file is excluded from Git commits via `.gitignore` to keep your credentials safe).*

### 4. Start the Bot
Run the main script to start Remy:
```bash
python main.py
```

---

## 🛡️ Security Showcase

When showcasing code in a portfolio, **never commit raw API keys or bot tokens**. This project demonstrates safe credential management:
- **Environment Separation**: Secrets are stored in a local-only `.env` file.
- **Template Provisioning**: A `.env.example` is committed instead, guiding others on how to set up the bot without exposing private keys.
- **Version Control Exclusions**: The `.gitignore` is fully configured to ignore cache files (`__pycache__/`) and local configurations.
