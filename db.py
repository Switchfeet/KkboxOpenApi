import pymysql
import charts


db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "1qaz2wsx3edc4",
    "db": "kkbox",
    "charset": "utf8"
}

charts.get_charts()
print("===========================================")


def delete_charts_tracks_from_db():
    try:
        conn = pymysql.connect(**db_settings)

        with conn.cursor() as cursor:
            delete_command = "DELETE FROM charts"

            cursor.execute(delete_command)

            conn.commit()

    except Exception as exc:
        print(exc)


# delete charts tracks from db
delete_charts_tracks_from_db()

# def add_charts_tracks_to_db(charts):
try:
    conn = pymysql.connect(**db_settings)

    with conn.cursor() as cursor:
        add_command = "INSERT INTO charts(id, name, artist)VALUE(%s, %s, %s)"

        charts = charts.get_charts_tracks("Ot9b9neLPHGat4LYK-")
        # print(charts)

        for chart in charts:
            cursor.execute(add_command, (chart["id"], chart["name"], chart["album"]["artist"]["name"]))

        conn.commit()

except Exception as exc:
    print(exc)


# get all charts tracks from db
def get_all_charts_tracks_from_db():
    try:
        conn = pymysql.connect(**db_settings)

        with conn.cursor() as cursor:
            get_command = "SELECT * FROM charts"
            cursor.execute(get_command)
            result = cursor.fetchall()
            print(result)

    except Exception as exc:
        print(exc)


# add charts tracks to db
# add_charts_tracks_to_db()

# get all charts tracks from db
get_all_charts_tracks_from_db()


# get first charts tracks from db
def get_first_chart_tracks_from_db():
    try:
        conn = pymysql.connect(**db_settings)

        with conn.cursor() as cursor:
            get_command = "SELECT * FROM charts"
            cursor.execute(get_command)
            result = cursor.fetchone()
            print(result)

    except Exception as exc:
        print(exc)


# get first charts tracks from db
get_first_chart_tracks_from_db()


# get many charts tracks from db
def get_many_chart_tracks_from_db(num: int):
    try:
        conn = pymysql.connect(**db_settings)

        with conn.cursor() as cursor:
            get_many_command = "SELECT * FROM charts"
            cursor.execute(get_many_command)
            result = cursor.fetchmany(num)
            print(result)

    except Exception as exc:
        print(exc)


# get many charts tracks from db
get_many_chart_tracks_from_db(3)


# get chart tracks by name from db
def get_chart_tracks_by_name_from_db(artist: str):
    try:
        conn = pymysql.connect(**db_settings)

        with conn.cursor() as cursor:
            get_by_name_command = "SELECT * FROM charts WHERE artist = %s"
            cursor.execute(get_by_name_command, (artist,))
            result = cursor.fetchall()
            print(result)

    except Exception as exc:
        print(exc)


# get chart tracks by name from db
get_chart_tracks_by_name_from_db("Jelly Roll")


# edit chart tracks by id from db
def edit_chart_tracks_by_id_from_db(artist: str, track_id: str):
    try:
        conn = pymysql.connect(**db_settings)

        with conn.cursor() as cursor:
            edit_by_id_command = "UPDATE charts SET artist = %s WHERE id = %s"
            cursor.execute(edit_by_id_command, (artist, track_id))

        conn.commit()

    except Exception as exc:
        print(exc)


# edit chart tracks by id from db
edit_chart_tracks_by_id_from_db("Chris Brown (克里斯小子)", "4m7Xi8nHf387oISq81")
# get chart tracks by name from db
get_chart_tracks_by_name_from_db("Jelly Roll")


# delete chart tracks by id from db
def delete_chart_tracks_by_id_from_db(track_id: str):
    try:
        conn = pymysql.connect(**db_settings)

        with conn.cursor() as cursor:
            delete_command = "DELETE FROM charts WHERE id = %s"

            cursor.execute(delete_command, (track_id,))

            conn.commit()

    except Exception as exc:
        print(exc)


# delete chart tracks by id from db
delete_chart_tracks_by_id_from_db("4m7Xi8nHf387oISq81")

get_chart_tracks_by_name_from_db("Chris Brown (克里斯小子)")
