from tortoise import Tortoise


async def drop_database() -> None:
    conn = Tortoise.get_connection("default")
    await conn.execute_query("DROP SCHEMA public CASCADE;")
    await conn.execute_query("CREATE SCHEMA public;")
    await Tortoise.generate_schemas()
