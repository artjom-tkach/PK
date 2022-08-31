class Delete:
    __sqlite3 = None

    def __init__(self, __sqlite3):
        # super().__init__(__sqlite3)
        # Committed because there is no parent

        self.__sqlite3 = __sqlite3
