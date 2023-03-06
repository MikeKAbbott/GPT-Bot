from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.message import Message

class Events(commands.Cog):

    def __init__(self, bot: Bot):
      self.bot: Bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
      self.bot.methods['change_status'].start()
      print('We have logged in as {0.user}'.format(self.bot))

    @commands.Cog.listener()
    async def on_message(self, ctx: Message) -> None:
      command_names: list = map(
        lambda command: command.name,
        self.bot.commands
      )

      if ctx.content[6:] not in command_names:
        await self.bot.get_command('chat')(ctx)

def setup(bot: Bot) -> None:
  bot.add_cog(Events(bot))
