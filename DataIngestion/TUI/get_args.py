import argparse as arg
import yaml

def get_args(def_sf, def_lt):

    parser = arg.ArgumentParser(
        # prog = "python3 main.py",
        description="A script to ingest and manage city's public transport data in"
                    "PSQL database. It provides both manual and automated usage"
                    "through the right parameters.",

        epilog="All absent settings are located in config files."
               "Good luck and may the force be with you"
    )

    parser.add_argument(
        '-s',
        '--omit-static',
        action="store_true",
        help="Omit static data ingest"
    )

    parser.add_argument(
        '-l',
        '--omit-live',
        action="store_true",
        help="Omit dynamic data ingest"
    )

    parser.add_argument(
        '-r',
        '--repeat',
        action="store_true",
        help="Put into constant working mode"
    )

