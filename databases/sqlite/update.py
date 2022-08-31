class Update:
    __sqlite3 = None

    def __init__(self, __sqlite3):
        super().__init__(__sqlite3)

        self.__sqlite3 = __sqlite3

    def update(self, table_name, update_fields, where_fields=None):
        """
        :param table_name:
        str. Example: 'User'

        :param update_fields:
        dict. Fields to update. Example: {'id': 1, 'first_name': 'Maximilian'}

        :param where_fields:
        None, list of dict. Fields to set where. Example: [{'field': 'id', 'value': 1, 'operator': '='}, {'field': 'id', 'value': 2, 'operator': '=', 'concat': 'OR'}]

        :return response:
        bool
        """
        if isinstance(update_fields, dict) and update_fields:
            update = f'UPDATE {table_name} SET '

            for update_field in update_fields.keys():
                update += update_field + '=?,'

            update = update[:-1]
            update_values = list(update_fields.values())
        else:
            raise ValueError('Parameter "update_fields" must be dict')

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

        sql = f'{update} {where}'

        if self.__sqlite3.connect():
            response = False
            try:
                cursor = self.__sqlite3.connection.cursor()
                cursor.execute(sql, update_values + where_values)
                self.__sqlite3.connection.commit()
                response = True
            except Exception as e:
                print(e)
            finally:
                self.__sqlite3.close_connection()
                return response
