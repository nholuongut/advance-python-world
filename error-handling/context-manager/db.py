import sqlite3
from typing import Dict, List, Any


# define custom error functions
class NotAutherizedError(Exception):
    pass


class NotFoundError(Exception):
    pass


class DbEmptyError(Exception):
    pass


# define the db connection context manager
class SQLite:
    def __init__(self, db_uri) -> None:
        self.database = db_uri

    def __enter__(self):
        print("Opening connection .")
        self.con = sqlite3.connect(database=self.database)
        return self.con.cursor()

    def __exit__(self, type, value, traceback):
        print("Closing connection .")
        self.con.close()


def blog_lst_to_json(item):
    return {
        "id": item[0],
        "published": item[1],
        "title": item[2],
        "content": item[3],
        "public": bool(item[4]),
    }


def fetch_blogs() -> List[Dict[str, Any]]:
    try:
        with SQLite("application.db") as cur:
            # execute the query to fetch all the blogs from db
            cur.execute("SELECT * FROM blogs where public=1;")

            if not cur.fetchall():
                raise DbEmptyError("No blogs database is empty !!")

            # convert db object to json
            json_data = list(map(blog_lst_to_json, cur.fetchall()))

            return json_data

    except sqlite3.OperationalError as e:
        raise NotFoundError(f"Unable to fetch blogs !! Error -> {e}")


def fetch_blog(id: str):
    try:
        with SQLite("application.db") as cur:
            # exzecute the query to get specific blogpost
            cur.execute(f"SELECT * FROM blogs where id=?", [id])

            # fetch the data
            db_obj = cur.fetchone()

            if not db_obj:
                raise NotFoundError(f"Request Blog not found  id:{id}")

            json_obj = blog_lst_to_json(db_obj)

            if not json_obj["public"]:
                raise NotAutherizedError(f"Request Blog is not authorized to view !!")

            return json_obj

    except sqlite3.OperationalError as e:
        raise NotFoundError(f"Unable to fetch blogs !! Error -> {e}")
