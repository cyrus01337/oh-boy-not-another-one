import traceback

import discord
from discord.ext import commands


class Errors(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        real_error = getattr(error, "original", error)
        breakdown = traceback.format_exception(type(real_error), real_error, real_error.__traceback__)
        output = "".join(breakdown)

        await ctx.send(f"```\n{output}\n```")


def setup(bot):
    bot.add_cog(Errors(bot))
