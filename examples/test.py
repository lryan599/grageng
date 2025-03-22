import lancedb
import pandas as pd
import pyarrow as pa
import asyncio
import os

current_file_path = os.path.abspath(__file__)
current_file_dir = os.path.dirname(current_file_path)

uri = os.path.join(current_file_dir, "data/sample-lancedb")
db = asyncio.run(lancedb.connect_async(uri))

df = pd.DataFrame(
    [
        {"vector": [3.1, 4.1], "item": "foo", "price": 10.0},
        {"vector": [5.9, 26.5], "item": "bar", "price": 20.0},
    ]
)


tbl = asyncio.run(db.create_table("table_from_df_async", df))
