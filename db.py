import sqlite3


CREATE_TABLE = """CREATE TABLE IF NOT EXISTS "user-data" (
	"id"	INTEGER,
	"attempts"	INTEGER NOT NULL,
	"wrong-words"	INTEGER NOT NULL,
	"record"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);"""

INIT_ROW = """INSERT INTO `user-data` (`attempts`, `wrong-words`, `record`) VALUES (?, ?, ?)"""

GET_DATA = """SELECT * FROM `user-data`"""

UPDATE_RECORD = """UPDATE `user-data` SET `record`= ? WHERE `id`= 1"""

UPDATE_ATTEMPTS = """UPDATE `user-data` SET `attempts`= ? WHERE `id`= 1"""

UPDATE_WRONG_WORDS = """UPDATE `user-data` SET `wrong-words`= ? WHERE `id`= 1"""

class DB:

    def __init__(self, db_name):
        self.__connect = sqlite3.connect(db_name)
        self._cursor = self.__connect.cursor()
    

    # Init DB
    def init(self):
        self._cursor.execute(CREATE_TABLE)
        data = self.get_data()

        if data == []:
            self._cursor.execute(INIT_ROW, (0, 0, 0))
        
        self.__connect.commit()
    

    def get_data(self):
        self._cursor.execute(GET_DATA)
        data = self._cursor.fetchall()
        return data[0]
    

    def _update_record(self, record):
        self._cursor.execute(UPDATE_RECORD, (record,))


    def _update_attempts(self):
        attempts = self.get_data()[1]
        self._cursor.execute(UPDATE_ATTEMPTS, (attempts+1,))
    

    def _update_wrong_words(self, count):
        wrong_words = self.get_data()[2]
        self._cursor.execute(UPDATE_WRONG_WORDS, (wrong_words+count,))
    

    # Update stat
    def update_data(self, record=None, wrong_words=None, increase_update=False):
        if increase_update: self._update_attempts()
        if record: self._update_record(record)
        if wrong_words: self._update_wrong_words(wrong_words)

        self.__connect.commit()
