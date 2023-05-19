import sqlite3


class SQLTool:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS catalog (
            oid INTEGER PRIMARY KEY AUTOINCREMENT,
            eid TEXT UNIQUE,
            len_ori INTEGER,    
            len_gaia INTEGER,
            len_ps INTEGER,
            len_2mass INTEGER,
            medra_gaia REAL,
            stdra_gaia REAL,
            meddec_gaia REAL,
            stddec_gaia REAL,
            medra_ps REAL,
            stdra_ps REAL,
            meddec_ps REAL,
            stddec_ps REAL,
            medra_2mass REAL,
            stdra_2mass REAL,
            meddec_2mass REAL,
            stddec_2mass REAL
        )''')

    def insert_data(self, eid, len_ori, len_gaia, len_ps, len_2mass, medra_gaia, stdra_gaia, meddec_gaia, stddec_gaia,
                    medra_ps, stdra_ps, meddec_ps, stddec_ps, medra_2mass, stdra_2mass, meddec_2mass, stddec_2mass):
        values = (
        eid, len_ori, len_gaia, len_ps, len_2mass, medra_gaia, stdra_gaia, meddec_gaia, stddec_gaia, medra_ps, stdra_ps,
        meddec_ps, stddec_ps, medra_2mass, stdra_2mass, meddec_2mass, stddec_2mass)
        self.cursor.execute('''INSERT INTO catalog (eid, len_ori, len_gaia, len_ps, len_2mass, medra_gaia, stdra_gaia, meddec_gaia, stddec_gaia, medra_ps, stdra_ps, meddec_ps, stddec_ps, medra_2mass, stdra_2mass, meddec_2mass, stddec_2mass) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', values)
        self.conn.commit()

    def update_data(self, eid, field, value):
        query = f"UPDATE catalog SET {field} = ? WHERE eid = ?"
        self.cursor.execute(query, (value, eid))
        self.conn.commit()

    def update_data_dict(self, eid, fields):
        # 构造 SET 子句，即 "field1 = ?, field2 = ?, ..."
        set_clause = ', '.join([f"{field} = ?" for field in fields.keys()])

        # 执行 SQL 查询
        query = f"UPDATE catalog SET {set_clause} WHERE eid = ?"
        values = tuple(fields.values()) + (eid,)
        self.cursor.execute(query, values)
        self.conn.commit()

    def delete_data(self, eid):
        self.cursor.execute('''DELETE FROM catalog WHERE eid = ?''', (eid,))
        self.conn.commit()

    def select_all_data(self):
        result_set = self.cursor.execute('''SELECT * FROM catalog''').fetchall()
        for row in result_set:
            print(row)

    def select_data_by_eid(self, eid):
        result_set = self.cursor.execute('''SELECT * FROM catalog WHERE eid = ?''', (eid,)).fetchall()
        for row in result_set:
            print(row)

if __name__ == '__main__':
    sql_tool = SQLTool('database.db')
    sql_tool.create_table()

    # sql_tool.insert_data('example2.fits', 100, 200, 300, 400, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.1, 11.1, 12.1)

    sql_tool.select_all_data()

    sql_tool.update_data('example.fits',"len_gaia", 500)
    sql_tool.select_data_by_eid('example.fits')

    sql_tool.update_data_dict('example.fits', {'medra_gaia': 1.2, 'stddec_ps': 3.4})

    sql_tool.__del__()

    # oid：自增整数类型主键列。
    # eid：文本类型唯一列,保存当天晚上fits文件名。
    # len_ori：整数类型列，内部有多少颗星。
    # len_gaia：整数类型列，代表Gaia目录中的长度。
    # len_ps：整数类型列，代表Pan - STARRS目录中的长度。
    # len_2mass：整数类型列，代表2MASS目录中的长度。
    # medra_gaia：实数类型列，代表Gaia目录中的右赤经中值。
    # stdra_gaia：实数类型列，代表Gaia目录中的右赤经标准偏差。
    # meddec_gaia：实数类型列，代表Gaia目录中的赤纬中值。
    # stddec_gaia：实数类型列，代表Gaia目录中的赤纬标准偏差。
    # medra_ps：实数类型列，代表Pan - STARRS目录中的右赤经中值。
    # stdra_ps：实数类型列，代表Pan - STARRS目录中的右赤经标准偏差。
    # meddec_ps：实数类型列，代表Pan - STARRS目录中的赤纬中值。
    # stddec_ps：实数类型列，代表Pan - STARRS目录中的赤纬标准偏差。
    # medra_2mass：实数类型列，代表2MASS目录中的右赤经中值。
    # stdra_2mass：实数类型列，代表2MASS目录中的右赤经标准偏差。
    # meddec_2mass：实数类型列，代表2MASS目录中的赤纬中值。
    # stddec_2mass：实数类型列，代表2MASS目录中的赤纬标准偏差。


