import asyncio

import discord
from discord.ext import commands
from discord import Embed
from discord.ext.commands.bot import Bot
from discord.message import Message
from utils.IsEmptyString import is_empty_string
from queue import Queue

class ChatCommand(commands.Cog):

    _responding: bool = False

    _user_messages: Queue = Queue()

    def __init__(self, bot: Bot):
      self.bot: Bot = bot

    @commands.command()
    async def chat(self, ctx: Message) -> None:
      if (
        ctx.author == self.bot.user
        or is_empty_string(ctx.content)
      ):
        return

      if ctx.content.startswith(self.bot.command_prefix):
        user_message = ctx.content[6:]
        self._user_messages.put(user_message)

        if not self._responding:
          await self._respond(ctx)

    async def _respond(self, ctx: Message) -> None:
      self._responding = True

      while not self._user_messages.empty():
        user_message: str = self._user_messages.get()
        gpt_message: str = ''

        async with ctx.channel.typing():
          gpt_message = self.bot.chatGPT.chat(user_message)
          await asyncio.sleep(2)
        
        help_embed: Embed = Embed(
          description=f'{ctx.author.mention}',
          color = discord.Color.random()
        )
        
        help_embed.add_field(
          name = 'User Message',
          value = user_message,
          inline = False,
        )

        help_embed.add_field(
          name = 'ChatGPT Response',
          value = gpt_message,
          inline = False,
        )

        await ctx.channel.send(embed = help_embed)

        self._user_messages.task_done()

      self._responding = False

def setup(bot: Bot) -> None:
  bot.add_cog(ChatCommand(bot))
