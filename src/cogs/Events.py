import discord

from discord.ext import commands, tasks
from discord.ext.commands.bot import Bot
from discord.message import Message
from discord.ext.commands import CommandNotFound

class Events(commands.Cog):

    def __init__(self, bot: Bot):
      self.bot: Bot = bot

    @tasks.loop(seconds = 5)
    async def change_status(self) -> None:
      await self.bot.change_presence(
        activity = discord.Game(next(self.bot.statuses))
      )

    @commands.Cog.listener()
    async def on_command_error(self, _, error):
      if isinstance(error, CommandNotFound):
        return

      raise error

    @commands.Cog.listener()
    async def on_ready(self) -> None:
      self.change_status.start()
      print('We have logged in as {0.user}'.format(self.bot))

    @commands.Cog.listener()
    async def on_message(self, ctx: Message) -> None:
      command_names: list = map(
        lambda command: command.name,
        self.bot.commands
      )

      if ctx.content[5:] not in command_names:
        await self.bot.get_command('chat')(ctx)

def setup(bot: Bot) -> None:
  bot.add_cog(Events(bot))
