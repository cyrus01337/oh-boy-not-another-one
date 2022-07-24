import pathlib
from typing import Optional

import discord
from discord import Guild, Message
from discord.ext import commands
from discord.ext.commands import Bot

import constants


class Boot(commands.Bot):
    @classmethod
    async def command_prefix(cls, bot: Bot, message: Message) -> str | list[str]:
        prefix: Optional[str | list[str]] = constants.PREFIX

        if constants.WHEN_MENTIONED and prefix:
            prefix = commands.when_mentioned_or(prefix)(bot, message)
        elif constants.WHEN_MENTIONED:
            prefix: list[str] = commands.when_mentioned()

        return prefix

    def __init__(self):
        super().__init__(
            command_prefix=Boot.command_prefix,
            intents=constants.INTENTS
        )

        for cog in constants.COGS_DIR.glob("**/*.py"):
            resolved_path = str(cog) \
                .replace(".py", "") \
                .replace("/", ".")

            self.load_extension(resolved_path)

        if constants.ADD_JISHAKU:
            self.load_extension("jishaku")

        self.loop.create_task(self.__ainit__())

    async def __ainit__(self):
        await self.wait_until_ready()

        permissions = discord.Permissions(administrator=True)
        url = discord.utils.oauth_url(self.user.id, permissions)

        print(f"\n{self.user.name} ({self.user.id}) is up and running, baby!")
        print(f"Invite using {url}", end="\n\n")

    @property
    def guild(self) -> Guild:
        return self.get_guild(464446709146320897)

    # def manipulate_extension(self, name: str, *, package: Optional[str]):
    #     pass

    def load_extension(self, name: str, *, package: Optional[str] = None):
        loading_message = f"Loading {name}"

        if package:
            loading_message += f" from {package}"

        print(loading_message)
        super().load_extension(name, package=package)

    def roon(self):
        token = constants.TOKEN

        super().run(token)


def main():
    boot = Boot()

    boot.roon()


if __name__ == "__main__":
    main()
