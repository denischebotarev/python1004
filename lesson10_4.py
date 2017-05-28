import sqlite3
from lesson10_1 import init_db


class Author:

    db_name = None

    def __init__(self, pk, name):
        self.id = pk
        self.name = name

    def __str__(self):
        return 'Author id - {0}, name - {1}'.format(self.id, self.name)

    @classmethod
    def get(cls, pk):
        with sqlite3.connect(cls.db_name) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM author WHERE id={}'.format(pk))
            pk, name = cur.fetchone()
            return Author(pk, name)


if __name__ == '__main__':
    db_name = 'mylibrary.db'
    init_db(db_name)
    Author.db_name = db_name

    a = Author.get(pk=1)
    print(a)
    print(a.name)