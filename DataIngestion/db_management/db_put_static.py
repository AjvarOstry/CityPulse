from .db_put_df import db_put_df

def db_put_static(conn, dic):

    exc = ""

    for x in range(1):
        is_ight = True

        for tab, df in dic.items():
            try:
                db_put_df(conn, df, tab)
            except Exception as e:
                is_ight = False
                exc = e
                break

        if is_ight == True:
            conn.commit()
            return True
        else:
            conn.rollback()

    return exc
