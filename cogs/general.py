import discord
from discord.ext import commands
from discord.ext.commands import Bot, Context

PERMISSIONS = discord.Permissions(administrator=True)


class General(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx: Context):
        url = discord.utils.oauth_url(self.bot.user.id, PERMISSIONS, ctx.guild)

        await ctx.send(url)


def setup(bot):
    bot.add_cog(General(bot))
