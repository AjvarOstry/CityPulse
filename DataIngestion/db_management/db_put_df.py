from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.sql import quoted_name
from sqlalchemy import table, column
from sqlalchemy.exc import SQLAlchemyError

def db_put_df(conn, df, table_name):

    print(f"Table name: {table_name}")

    cols = [column(c) for c in df.columns]
    tab = table(
        quoted_name(table_name, quote=True),
        *cols,
    )

    ins = insert(tab).values(df.to_dict("records")).on_conflict_do_nothing()

    try:
        conn.execute(ins)

    except SQLAlchemyError as e:
        raise ConnectionError("ERROR: Could not execute insert: \n" + str(e))

