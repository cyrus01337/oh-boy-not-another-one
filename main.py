import pathlib
from typing import Optional

import discord
from discord.ext import commands

import constants


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or(constants.PREFIX),
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
    def invite(self):
        return discord

    # def manipulate_extension(self, name: str, *, package: Optional[str]):
    #     pass

    def load_extension(self, name: str, *, package: Optional[str] = None):
        loading_message = f"Loading {name}"

        if package:
            loading_message += f" from {package}"

        print(loading_message)
        super().load_extension(name, package=package)

    def run(self):
        token = constants.TOKEN

        super().run(token)


def main():
    bot = Bot()

    bot.run()


if __name__ == "__main__":
    main()
