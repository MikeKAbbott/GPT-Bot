from __future__ import annotations

from discord import Embed

class DiscordEmbed():

  def __init__(self, **kwargs):
    self.embed: Embed = Embed(
      **kwargs
    )

  def add_content(self, title: str, content: str) -> DiscordEmbed:
    self.embed.add_field(
      name = title,
      value = content,
      inline = False,
    )

    return self

  def set_author(self, author: str) -> DiscordEmbed:
    self.embed.set_author(
      name = author
    )

    return self

  def set_color(self, color: str) -> DiscordEmbed:
    self.embed.color = color

    return self

  def set_footer(self, content: str) -> DiscordEmbed:
    self.embed.set_footer(
      text = content
    )

    return self
  