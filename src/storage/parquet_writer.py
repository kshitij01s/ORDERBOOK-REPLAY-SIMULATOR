import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

class ParquetWriter:
    def __init__(self, filename):
        self.filename = filename
        self._data = []

    def append_tick(self, tick: dict):
        self._data.append(tick)

    def flush(self):
        if not self._data:
            return
        df = pd.DataFrame(self._data)
        table = pa.Table.from_pandas(df)
        pq.write_table(table, self.filename)
        self._data = []

    def close(self):
        self.flush()
