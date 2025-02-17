"""
ORM -> Object relational-mapper
1. Very good for very simple queries
2. SQLAlchemy
3. Acts as another security layer to minimize risk of sql injections
SP -> Stored procedures
1. Sprocs can be version controlled
2. Sprocs for sql server can be compiled
3. Sprocs can be schema bound
4. Sprocs have statistics

5. By writing a stored procedure you can execute logic without
    the application needing to run
6. Stored procedures in python can be used with various context blocks
    to further ensure security when it comes to roles
7. ORMs can generate simple and non-performant queries
    complex logix can be easier to handle
8. The version of your code that queries the DB can change
    with the schema of the database, without doing so your
    application may be upgraded but your database not yet
"""
from schema import Schema, And, Use, Optional, SchemaError
from contextlib import contextmanager
from psycopg2 import connect


schema = Schema([
    {
        "name": And(str, len),
        "age": And(Use(int), lambda n: 18 <= n <= 65),
        Optional("gender"): And(str, Use(str.lower), lambda s: s in ("squid", "kid"))
    }
])

@contextmanager
def create_db_connection():
    db_conn = connect("dbname=dvdrental user=postgres password=postgres")
    try:
        yield db_conn
    finally:
        db_conn.close()

def get_film_count(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT count(*) FROM film")
        result = cur.fetchall()
    return result

if __name__ == "__main__":
    # Make specific connection with context
    connection = create_db_connection()

    with connection as conn:
        film_count = get_film_count(conn)
        print(film_count)