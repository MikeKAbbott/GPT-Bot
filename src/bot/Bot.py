import discord
import os

from src.api.ChatGPT import ChatGPT
from discord.ext import commands, tasks
from discord.ext.commands.bot import Bot
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
      'title': '#chat [your message here]',
      'content': 'Initiates a conversation with the bot', 
    },
    {
      'title': '#chat Clear',
      'content': 'Resets the conversation',
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

  def run_bot(self) -> None:
    self.run(os.getenv('TOKEN'))

  def _add_methods(self) -> None:
    for method in self._bot_methods:
      self.methods[method] = eval(f'self.{method}')

  def _load_cogs(self) -> None:
    for ext in self._extensions:
      try:
        self.load_extension(f'src.cogs.{ext}')

      except Exception as e:
        print(f'Failed to load extension {ext}.')