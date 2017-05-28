import sqlite3


class AuthorDTO:
    def __init__(self, pk, name):
        self.id = pk
        self.name = name

    def __str__(self):
        return 'Author <id: {0}, name {1}>'.format(self.id, self.name)


class AuthorDAO:
    def __init__(self, db_name):
        self.db_name = db_name

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def find(self, pk):
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM author WHERE id={0}'.format(pk))
            pk, name = cur.fetchone()
            return AuthorDTO(pk, name)

    def insert(self, name):
        pass

    def delete(self, pk):
        pass

    def update(self, pk, name):
        pass


if __name__ == '__main__':
    dao = AuthorDAO('mylibrary.db')
    a1 = dao.find(2)
    print(a1)