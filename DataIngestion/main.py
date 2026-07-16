import yaml

from data_get_fit.get_static_data import get_static_data
from test_data import test_dataframe
from db_management.db_connect import db_connect
from db_management.db_put_static import db_put_static

def main():

    # TO DO
    # 1. gwt static data V
    # 2. fit static data V
    # 3. check ststic with db ?
    # 4. save static to db
    # 5.
    print("1")

    with open("./configs/general_conf.yaml", "r", encoding="utf-8") as f:
        general_conf = yaml.safe_load(f)
        print("2")

    try:
        static_dict = get_static_data(general_conf["import"]["static_data_path"])
        # static_dict = test_dataframe()
        print("3")
    except Exception as e:
        print(e)
        return 1

    with open("./configs/psql_client_conf.yaml", "r", encoding="utf-8") as f:
        psql_conf = yaml.safe_load(f)
        print("4")

    # db_tab_names = psql_conf["db"]["static-tables"]
    # print(db_tab_names)
    print("5")

    try:
        conn = db_connect(
            psql_conf["client"]["user"],
            psql_conf["client"]["password"],
            psql_conf["db"]["host"],
            psql_conf["db"]["port"],
            psql_conf["db"]["db-name"]
        )
        print("6")
    except:
        return 2

    res = db_put_static(conn, static_dict)
    print(res)

if __name__ == "__main__":
    main()