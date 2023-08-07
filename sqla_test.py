from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os

load_dotenv()

db_url = os.environ.get("SUPABASE_URL")

engine = create_engine(db_url,echo=True)

'''
with engine.connect() as conn:
    result = conn.execute(text("select x, y from test_table where y > :y"),{"y": 1000})
    for row in result:
        print(f"x: {row.x} y:{row.y}")
'''
'''
with engine.connect() as conn:
    result = conn.execute(text("insert into test_table (x,y) values (:x,:y)"),
                          [{"x":11,"y":12},{"x":44,"y":32}],)
    conn.commit()
'''
stmt = text("select x,y from test_table where y < :y order by x,y")
with Session(engine) as session:
    result = session.execute(stmt,{"y":100})
    for row in result:
        print(f"x: {row.x} y:{row.y}")