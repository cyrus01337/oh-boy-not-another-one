import traceback

import discord
from discord.ext import commands
from discord.ext.commands import Bot, CommandError, Context


class Errors(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: Context, error: CommandError):
        real_error = getattr(error, "original", error)
        breakdown = traceback.format_exception(type(real_error), real_error, real_error.__traceback__)
        output = "".join(breakdown)

        await ctx.send(f"```\n{output}\n```")


def setup(bot):
    bot.add_cog(Errors(bot))
