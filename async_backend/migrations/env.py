from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context
from app.models import Base  # импорт моделей

# Настройки Alembic
config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata

# URL базы данных
db_url = config.get_main_option("sqlalchemy.url")

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url=db_url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = create_engine(
        db_url,
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
