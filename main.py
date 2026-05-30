import asyncio
import logging

from bot.client import create_bot
from bot.config import Settings
from bot.database import Database
from web.app import create_app

import uvicorn


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
    )
    settings = Settings.from_env()
    database = Database(settings.database_path)
    await database.connect()
    await database.migrate()

    bot = create_bot(settings, database)
    app = create_app(settings, database, bot)

    web_config = uvicorn.Config(
        app,
        host=settings.web_host,
        port=settings.web_port,
        log_level="info",
    )
    server = uvicorn.Server(web_config)

    await asyncio.gather(
        bot.start(settings.discord_token),
        server.serve(),
    )


if __name__ == "__main__":
    asyncio.run(main())
