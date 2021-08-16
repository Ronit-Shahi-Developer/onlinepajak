from fastparquet import ParquetFile


class Task(object):
    def __init__(self, **kwargs):
        for field in ('id', 'name', 'owner', 'status'):
            setattr(self, field, kwargs.get(field, None))

    pf = ParquetFile('test_invoices.parquet')
    df = pf.to_pandas()

