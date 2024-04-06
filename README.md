# Discord AI Assistant

This is a Discord bot that allows users to ask questions and receive answers from an AI model. The bot uses the Discord API and a custom AI API to provide responses to user queries.

## Features

- **Ping Command**: Users can run the `/ping` command to check the bot's latency.
- **Ask Command**: Users can run the `/ask` command to ask a question and receive a response from the AI model.
  - The `question` parameter is required and specifies the question to be asked.
  - The `model` parameter is optional and specifies the AI model to use (default is "solidity").

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/discord-ai-assistant.git
   ```
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project directory and add the following environment variables:
   ```
   token=your-discord-bot-token
   master_key=your-ai-api-master-key
   ```
4. Run the bot:
   ```
   python main.py
   ```

## Dependencies

- `discord.py`: For interacting with the Discord API.
- `requests`: For making HTTP requests to the AI API.
- `os`: For accessing environment variables.
- `dotenv`: For loading environment variables from a `.env` file.

## Usage

1. Invite the bot to your Discord server.
2. Use the `/ping` command to check the bot's latency.
3. Use the `/ask` command to ask a question and receive a response from the AI model.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open a new issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
