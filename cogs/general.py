import discord
from discord.ext import commands

PERMISSIONS = discord.Permissions(administrator=True)


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx: commands.Context):
        url = discord.utils.oauth_url(self.bot.user.id, PERMISSIONS, ctx.guild)

        await ctx.send(url)


def setup(bot):
    bot.add_cog(General(bot))
