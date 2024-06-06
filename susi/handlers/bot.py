from pyrogram import Client
from pyrogram.types import BotCommand

class SusiClient(Client):  # Define a custom client class that inherits from the Client class
    def __init__(self, api_id, api_hash, bot_token):
        """
        Initialize the SusiClient class.
        This function initializes the SusiClient class with the provided API ID, API hash, and bot token.
        """
        # Call the base class constructor with the specified session name, API ID, API hash, and bot token.
        super().__init__(
            "SusiMusic",
            api_id=api_id,
            api_hash=api_hash,
            bot_token=bot_token
        )

    async def start(self):
        """
        Start the bot.
        This function starts the bot by calling the start method of the base class and sets the bot commands.
        """
        # Start the bot by calling the start method of the base class.
        await super().start()

        # Set the bot commands using the set_bot_commands method of the base class.
        await self.set_bot_commands(
            [
                BotCommand("ping", "Check if the bot is online or offline"),
                BotCommand("play", "Play a song or add it to the queue"),
                BotCommand("skip", "Skip the currently playing song"),
                BotCommand("pause", "Pause the current playing song"),
                BotCommand("resume", "Resume playing the paused song"),
                BotCommand("queue", "Display the list of songs currently in the queue"),
            ]
        )

        # Print a success message to indicate that the bot has started successfully.
        print("Bot started successfully.")

    async def stop(self):
        """
        Stop the bot.
        This function stops the bot by calling the stop method of the base class.
        """
        # Stop the bot by calling the stop method of the base class.
        await super().stop()

        print("Bot stopped.")

