import sqlite3 as sq

class DB(object):
    def __init__(self, user_score) -> None:
        self.connect(user_score)

    def connect(self, user_score):
        with sq.connect("score_db.db") as connection:
            cursor = connection.cursor()
            self.arr_score = []

            cursor.execute("""SELECT best_score FROM Score WHERE id == 1""")
            self.arr_score.append(cursor.fetchone())

            if user_score > self.arr_score[0][0]:
                self.arr_score = []
                
                cursor.execute(f"""UPDATE Score SET best_score = {user_score} WHERE id == 1""")
                cursor.execute("""SELECT best_score FROM Score WHERE id == 1""")
                self.arr_score.append(cursor.fetchone())
    
    def get_score(self):
        return self.arr_score