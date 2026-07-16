from sqlalchemy import create_engine, URL

def db_connect(user, passwd, host, port, db):

    url = URL.create(
        "postgresql+psycopg2",
        username=user,
        password=passwd,
        host=host,
        port=port,
        database=db
    )

    try:
        engine = create_engine(
            url,
            pool_recycle=3600,
            pool_pre_ping=True,
            echo_pool=True,
            hide_parameters=True
        )

        with engine.connect() as conn:
            pass

    except Exception as e:
        raise ConnectionError(f"ERROR: Unable to connect to DB: {e}")

    return engine.connect()