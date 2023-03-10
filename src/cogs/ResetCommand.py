from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.message import Message

class ResetCommand(commands.Cog):

  def __init__(self, bot):
    self.bot: Bot = bot

  @commands.command(aliases=['#gpt reset'])
  async def reset(self, ctx: Message) -> None:
    self.bot.chatGPT.clear_messages()

    await ctx.channel.send(
      f'<@{ctx.author.id}>\n\nThe conversation has been reset.'
    )

def setup(bot: Bot) -> None:
  bot.add_cog(ResetCommand(bot))
