#!/usr/bin/env python
import pathlib
from typing import Any, Optional

import discord
import dotenv
from discord.ext import commands

COGS_DIR = pathlib.Path("./cogs")
CONFIG: dict[str, Any] = dotenv.dotenv_values(".env")
ADD_JISHAKU: bool = CONFIG["ADD_JISHAKU"]
PREFIX: Optional[str] = CONFIG["PREFIX"]
TOKEN: str = CONFIG["TOKEN"]
WHEN_MENTIONED: bool = CONFIG["WHEN_MENTIONED"]
INTENTS = discord.Intents.default()
