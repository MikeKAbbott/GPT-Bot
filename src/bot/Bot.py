import discord
import os

from api.ChatGPT import ChatGPT
from discord.ext import commands, tasks
from discord.ext.commands.bot import Bot
from dotenv import load_dotenv
from itertools import cycle

load_dotenv()

class Bot():

  _extensions: list = [
    'Events',
    'ChatCommand',
    'HelpCommand',
    'ResetCommand',
  ]

  _help_commands: list = [
    {
      'title': '#chat [your message here]',
      'content': 'Initiates a conversation with the bot', 
    },
    {
      'title': '#chat Clear',
      'content': 'Resets the conversation',
    },
  ]

  _bot_methods: list = [
    'change_status',
  ]

  _bot_statuses: cycle = cycle([
    'Type "#chat help" for help',
    'Type "#chat [Your message here] to start the conversation',
    'Type "#chat reset" to reset the conversation',
  ])

  def __init__(self):
    self.bot: Bot = commands.Bot(
      command_prefix = '#chat ',
      intent = discord.Intents.all(),
      help_command = None
    )

    self.bot.remove_command('help')
    self.bot.chatGPT: ChatGPT = ChatGPT()

    self._add_attributes()
    self._load_cogs()

    self.bot.run(os.getenv('TOKEN'))
  
  @tasks.loop(seconds = 5)
  async def change_status(self) -> None:
    await self.bot.change_presence(
      activity = discord.Game(next(self.bot.statuses))
    )

  def _add_attributes(self) -> None:
    self.bot.methods: dict = {}

    for method in self._bot_methods:
      self.bot.methods[method] = eval(f'self.{method}')

    self.bot.help_commands: list = self._help_commands
    self.bot.statuses: list = self._bot_statuses

  def _load_cogs(self) -> None:
    for ext in self._extensions:
      try:
        self.bot.load_extension(f'cogs.{ext}')
      except Exception as e:
        print(f'Failed to load extension {ext}.')
        print(e)
