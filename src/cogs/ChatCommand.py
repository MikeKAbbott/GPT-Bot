import asyncio
import discord

from discord import Embed
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.message import Message
from src.utils.IsEmptyString import is_empty_string
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
        gpt_message: str = ''
        user_message: str = self._user_messages.get()

        async with ctx.channel.typing():
          gpt_message = self.bot.chatGPT.chat(user_message)['content']
          await asyncio.sleep(2)

        chat_embed: Embed = Embed(
          description= f'{ctx.author.mention}',
          color = discord.Color.random()
        )

        chat_embed.add_content('User Message', user_message)
        chat_embed.add_content('ChatGPT Response', gpt_message)

        await ctx.channel.send(embed = chat_embed)

        self._user_messages.task_done()

      self._responding = False

def setup(bot: Bot) -> None:
  bot.add_cog(ChatCommand(bot))
