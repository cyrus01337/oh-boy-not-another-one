import discord
from discord.ext import commands


class Roles(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.reason = "Role auto-assignment"

        self.bot.loop.create_task(self.__ainit__())

    @property
    def bots(self) -> discord.Role:
        return self.bot.guild.get_role(761422177798324244)

    @property
    def community(self) -> discord.Role:
        return self.bot.guild.get_role(761425977401933845)

    def _resolve_roles_from_member(self, member: discord.Member) -> list[discord.Role]:
        roles = [
            self.community
        ]

        if member.bot:
            roles.append(self.bots)

        return roles

    async def __ainit__(self):
        await self.bot.wait_until_ready()

        members: list[discord.Member] = self.bot.guild.members

        for member in members:
            roles = self._resolve_roles_from_member(member)

            await member.add_roles(*roles, reason=self.reason)

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        roles = self._resolve_roles_from_member(member)

        await member.add_roles(roles, reason=self.reason)


def setup(bot):
    bot.add_cog(Roles(bot))
