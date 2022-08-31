class Insert:
    __sqlite3 = None

    def __init__(self, __sqlite3):
        super().__init__(__sqlite3)

        self.__sqlite3 = __sqlite3

    def insert(self, table_name, insert_fields, get_select=False):
        """
        :param table_name:
        str. Example: 'User'

        :param insert_fields.
        dict. Fields to insert. Example: {'id': 1, 'first_name': 'Maximilian'}

        :param get_select
        bool. Get select object or not. Example: True

        :return insert:
        Get row_id or select object of row_id
        """
        if isinstance(insert_fields, dict) and insert_fields:
            insert = 'INSERT INTO {table_name} ({fields})'.format(
                table_name=table_name,
                fields=','.join(insert_fields.keys())
            )
            insert_values = list(insert_fields.values())

            values = 'VALUES ('
            for _ in insert_values:
                values += '?,'

            values = values[:-1]
            values += ')'

            sql = f'{insert} {values}'
        else:
            raise ValueError('Parameter "where_fields" must be dict')

        if self.__sqlite3.connect():
            row = None
            try:
                cursor = self.__sqlite3.connection.cursor()
                cursor.execute(sql, insert_values)
                self.__sqlite3.connection.commit()

                if cursor.lastrowid:
                    row = cursor.lastrowid
                    if get_select:
                        row = self.__sqlite3.select(table_name, select_fields='*', where_fields=[
                            {
                                'field': 'id',
                                'value': cursor.lastrowid,
                                'operator': '='
                            }
                        ], limit_field=1)

            except Exception as e:
                print(e)
            finally:
                self.__sqlite3.close_connection()
                return row
