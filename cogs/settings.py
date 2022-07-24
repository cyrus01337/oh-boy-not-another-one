import copy
import json

import aiofiles
from discord.ext import commands
from discord.ext.commands import Bot, Context


class Settings(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        self.path = "./settings.json"
        self.json_dump_kwargs = {
            "indent": 4,
            "sort_keys": True
        }

    async def set_settings(self, settings: dict):
        async with aiofiles.open(self.path, "w+") as fh:
            encoded = json.dumps(settings, **self.json_dump_kwargs)

            await fh.write(encoded)

    async def get_settings(self) -> dict:
        try:
            async with aiofiles.open(self.path, "r+") as fh:
                content = await fh.read()

                return json.loads(content)
        except (IOError, json.JSONDecodeError):
            async with aiofiles.open(self.path, "w+") as fh:
                settings = {}

                await self.settings(settings)

                return settings

    def format_settings(self, settings: dict) -> str:
        if not settings:
            return "You have no settings"

        return "\n".join((
            f"**{key}:** {value}"
            for key, value in settings.items()
        ))

    @commands.group(invoke_without_command=True)
    async def settings(self, ctx: Context):
        settings = await self.get_settings()
        formatted = self.format_settings(settings)

        await ctx.send(formatted)

    @settings.command(name="get")
    async def settings_get(self, ctx: Context, setting: str = None):
        settings = await self.get_settings()
        setting_found = settings[setting]

        if not (setting or setting_found):
            settings_command = self.bot.get_command("settings")
            pseudo_ctx = copy.copy(ctx)
            pseudo_ctx.command = settings_command

            await self.bot.invoke(pseudo_ctx)
        elif setting_found:
            formatted_setting = f"**{setting.title()}:**"

            await ctx.send(f"{formatted_setting} {setting_found}")


def setup(bot):
    bot.add_cog(Settings(bot))
