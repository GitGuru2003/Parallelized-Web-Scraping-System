import pymysql

database = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="scraping_db",
)


def store_data_in_db(data):
    try:
        with database.cursor() as cursor:
            sql = "INSERT INTO web_pages (url, title) VALUES (%s, %s)"
            cursor.execute(sql, (data["url"], data["title"]))

        database.commit()
    except Exception as e:
        print(f"Error storing data in DB: {e}")


def close_db():
    database.close()
