def main() -> None:
    import sqlalchemy as sa
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    import app_1.config as conf

    from .models import Achievement

    engine = create_engine(conf.db_str if conf.db_str is not None else conf.db_conn)

    with Session(engine) as session:
        a1 = session.scalars(sa.select(Achievement).where(Achievement.id == 1)).one_or_none()
    print(a1.description if a1 is not None else "Empty")


if __name__ == "__main__":
    main()
