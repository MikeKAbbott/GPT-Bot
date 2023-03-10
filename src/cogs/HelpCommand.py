import discord

from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.message import Message
from utils.CreateDiscordEmbed import DiscordEmbed

class HelpCommand(commands.Cog):

  def __init__(self, bot: Bot):
    self.bot: Bot = bot

  @commands.command(aliases=['#gpt help'])
  async def help(self, ctx: Message) -> None:
    help_embed: DiscordEmbed = DiscordEmbed(
      title = 'Help Desk for Chit Chat Bot',
      description = 'All commands for the chit chat bot.',
      color = discord.Color.random()
    ).set_author(
      author = 'Chit-Chat-Bot'
    ).set_footer(
      content = f'Requested by @{ctx.author}.'
    )

    for command in self.bot.help_commands:
      help_embed.add_content(
        title = command.get('title'),
        content = command.get('content'),
    )

    await ctx.channel.send(embed = help_embed.embed)

def setup(bot: Bot) -> None:
  bot.add_cog(HelpCommand(bot))
