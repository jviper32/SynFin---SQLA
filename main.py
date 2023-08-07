from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

db_url = os.environ.get("SUPABASE_URL")

engine = create_engine(db_url,echo=True)

# commit as you go - used more in the tutorial as it's more flexible
with engine.connect() as conn:
    # commenting this out as I can't create duplicate tables
    # conn.execute(text("CREATE TABLE test_table (x int, y int)"))
    conn.execute(
        text("INSERT INTO test_table (x,y) VALUES (:x, :y)"),
        [{"x":100, "y":200}, {"x":1000, "y":2000}],
    )
    conn.commit()

# begin once - apparently the preferred mode
with engine.begin() as conn:
    conn.execute(
        text("INSERT INTO services (client_id) values (:client_id)"),
        [{"client_id":"64a316dca25eccf9073138e5"}]
    )