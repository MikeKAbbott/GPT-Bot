import discord
import os

from src.api.ChatGPT import ChatGPT
from discord.ext import commands
from dotenv import load_dotenv
from itertools import cycle

load_dotenv()

class Bot(commands.Bot):

  _extensions: list = [
    'Events',
    'ChatCommand',
    'HelpCommand',
    'ResetCommand',
  ]

  help_commands: list = [
    {
      'name': '#chat [your message here]',
      'value': 'Initiates a conversation with the bot', 
    },
    {
      'name': '#chat Clear',
      'value': 'Resets the conversation',
    },
  ]

  statuses: cycle = cycle([
    'Type "#chat help" for help',
    'Type "#chat [Your message here] to start the conversation',
    'Type "#chat reset" to reset the conversation',
  ])

  def __init__(self):
    super().__init__(
      command_prefix = '#gpt ',
      intent = discord.Intents.all(),
      help_command = None
    )

    self.chatGPT: ChatGPT = ChatGPT()

    self.remove_command('help')
    self._load_cogs()

  def start_client(self) -> None:
    self.run(os.getenv('TOKEN'))

  def _load_cogs(self) -> None:
    for ext in self._extensions:
      try:
        self.load_extension(f'src.cogs.{ext}')

      except Exception as e:
        print(f'Failed to load extension {ext}.')