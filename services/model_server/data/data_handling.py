from services import db
import pandas as pd
import numpy as np
from io import StringIO


def create_table(table_name, columns, column_types):
    query = 'CREATE TABLE {} (\n'.format(table_name)
    query += '    id SERIAL PRIMARY KEY,\n'
    query += ',\n'.join(['    ' + column + ' ' + column_type for column, column_type in zip(columns, column_types)])
    query += '\n);'
    db.engine.execute(query)


def parse_csv(table_name, filename):
    df = pd.read_csv(filename)
    print(df.columns)
    column_types = []
    for column in df.columns:
        if np.issubdtype(df[column].dtype, np.floating):
            column_types.append('float')
        elif np.issubdtype(df[column].dtype, np.integer):
            column_types.append('int')
        else:
            column_types.append('varchar(255)')
    columns = list(df.columns)
    print(columns)
    print(column_types)
    create_table(table_name, columns, column_types)
    output = StringIO()
    df.to_csv(output, sep='\t', header=False, index=True)
    output.seek(0)
    fake_conn = db.engine.raw_connection()
    cur = fake_conn.cursor()
    cur.copy_from(output, table_name, null='')
    fake_conn.commit()
    cur.close()
