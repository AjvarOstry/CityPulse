import io

import requests as rq
import zipfile as zip
import pandas as pd

if __name__ == "__main__":
    from fit_static_data import fit_static_data
else:
    from .fit_static_data import fit_static_data


def get_static_data( static_URL = 'https://otwarte.miasto.lodz.pl/wp-content/uploads/2025/06/GTFS.zip' ):

    try:
        resp = rq.get(static_URL)
    except Exception as e:
        raise ConnectionError(
            f"ERROR: Cannot connect to {static_URL}. \n"
            f" Unable to get static data: {e}"
        )

    pd_dictionary = {
        "Calendar": {},
        "Calendar_Dates": {},
        "Routes": {},
        "Shapes": {},
        "Stop_Times": {},
        "Stops": {},
        "Trips": {},
    }

    with zip.ZipFile(io.BytesIO(resp.content)) as archive:

        for k in pd_dictionary.keys():
            with archive.open(str.lower(f"{k}.txt")) as file:
                pd_dictionary[k] = pd.read_csv(file)
                #pd_dictionary[k] = pd_dictionary[k].head(5)

    try:
        pd_dictionary = fit_static_data(pd_dictionary)
    except Exception as e:
        raise Exception(f"ERROR: Couldn't fit static data: {e}")


    return pd_dictionary


if __name__ == "__main__":

    dict = get_static_data()

    for k in dict.keys():
        print(dict[k])



