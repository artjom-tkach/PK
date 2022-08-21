import sqlite3


class Select:
    __sqlite3 = None
    __row_factories = {
        'Row': sqlite3.Row
    }

    def __init__(self, __sqlite3):
        super().__init__(__sqlite3)

        self.__sqlite3 = __sqlite3

    def select(self, table_name, select_fields='*', where_fields=None, limit_field=None, row_factory='Row'):
        """
        :param table_name:
        str. Example: 'User'

        :param select_fields.
        str == '*', tuple. Fields to get. Example: ('id', 'created_at')

        :param where_fields:
        None, list of dict. Fields to set where. Example: [{'field': 'id', 'value': 1, 'operator': '='}, {'field': 'id', 'value': 2, 'operator': '=', 'concat': 'OR'}]

        :param limit_field:
        None, int. Set select limit: Example: 1

        :param row_factory:
        str. Type of sorting: Example: 'Row'

        :return select:
        Getting columns
        """
        if select_fields == '*':
            select = 'SELECT * FROM {table_name}'.format(table_name=table_name)
        elif isinstance(select_fields, tuple) and select_fields:
            select = 'SELECT {fields} FROM {table_name}'.format(fields=','.join(select_fields), table_name=table_name)
        else:
            raise ValueError('Parameter "select_fields" must be str which equal "*" or not an empty tuple')

        where = ''
        where_values = list()

        if where_fields is not None:
            if where_fields and isinstance(where_fields, list):
                where = 'WHERE '

                for idx, where_field in enumerate(where_fields):
                    if isinstance(where_field, dict) and where_field:
                        if 'concat' in where_field:
                            if where_field['concat'] not in ['AND', 'OR'] or idx == 0:
                                raise ValueError(
                                    'Key "concat" in list of dict in param "where_fields" must equal [AND, OR] and must not be first in the list of dict'
                                )
                            where += ' {concat} '.format(concat=where_field['concat'])

                        elif 'concat' not in where_field and idx > 0:
                            raise ValueError(
                                'Key "concat" must be in list of dict in param "where_fields" in subsequent dictionaries after the first'
                            )

                        where += '{field}{operator}?'.format(
                            field=where_field['field'],
                            operator=where_field['operator']
                        )

                        where_values.append(where_field['value'])
                    else:
                        raise ValueError('Parameter "where_fields" must be list of dict')
            else:
                raise ValueError('Parameter "where_fields" must be None or list of dict')

        limit = ''

        if limit_field is not None:
            if str(limit_field).isdigit():
                limit_field = int(limit_field)
                limit += f'LIMIT {limit_field}'
            else:
                raise ValueError('Parameter "limit" must be None or int')

        sql = f'{select} {where} {limit}'

        if self.__sqlite3.connect():
            columns = None
            try:
                if row_factory in self.__row_factories:
                    self.__sqlite3.connection.row_factory = self.__row_factories[row_factory]
                cursor = self.__sqlite3.connection.cursor()
                execute = cursor.execute(sql, where_values)

                if limit_field == 1:
                    columns = execute.fetchone()
                else:
                    columns = execute.fetchall()

            except Exception as e:
                print(e)
            finally:
                self.__sqlite3.close_connection()
                return columns
