from app.database.db import db
from sqlalchemy import text
#obtiene todo de la tabla 'has'
def get_all_has():
    sql = text('SELECT systemid, organizationid FROM has')
    result = db.session.execute(sql)
    rows = result.fetchall()
    return [
        {'systemid': row[0], 'organizationid': row[1]}
        for row in rows
    ] 