import discord
from discord import Embed
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.message import Message

class HelpCommand(commands.Cog):

  def __init__(self, bot: Bot):
    self.bot: Bot = bot

  @commands.command(aliases=['#chat help'])
  async def help(self, ctx: Message) -> None:
    help_embed: Embed = Embed(
      title = 'Help Desk for Chit Chat Bot',
      description = 'All commands for the chit chat bot.',
      color = discord.Color.random()
    )

    help_embed.set_author(name = 'Chit Chat')

    for command in self.bot.help_commands:
      help_embed.add_field(
        name = command.get('name'),
        value = command.get('value'),
        inline = False,
      )

    help_embed.set_footer(
      text = f'Requested by @{ctx.author}.',
    )

    await ctx.channel.send(embed = help_embed)

def setup(bot: Bot) -> None:
  bot.add_cog(HelpCommand(bot))
