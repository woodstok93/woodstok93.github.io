from app.database import get_db

class Reservas:
    def __init__(self, id=None, nombre=None, email=None, mensaje=None ):
        self.id= id 
        self.email = email
        self.mensaje = mensaje
        self.nombre = nombre
       

    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id:
            cursor.execute("""
                UPDATE reservas SET Email = %s, id= %s, mensaje = %s, nombre = %s
                WHERE id = %s
            """, (self.nombre, self.email, self.mensaje, self.id))
        else:
            cursor.execute("""
                INSERT INTO reservas (email, nombre, email, id) VALUES (%s, %s, %s, %s)
            """, (self.nombre, self.email, self.id, self.mensaje))
            self.id= cursor.lastrowid
        db.commit()
        cursor.close()

    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM reservas")
        rows = cursor.fetchall()
        movies = []
        for row in rows:
            movies.append(Reservas(id=row[0], email=row[1], nombre=row[2], mensaje=row[3] ))

        #movies = [Movie(id_movie=row[0], title=row[1], director=row[2], release_date=row[3], banner=row[4]) for row in rows]
        cursor.close()
        return Reservas

    @staticmethod
    def get_by_id(Id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM reservas WHERE id_movie = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Reservas(id=row[0], email=row[1], nombre=row[2], mensaje=row[3] )
        return None

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM reservas WHERE id_reservas = %s", (self.id_reservas,))
        db.commit()
        cursor.close()

    def serialize(self):
        return {
            'id_reservas': self.id_reservas,
            'nombre': self.nombre,
            'email': self.email,
            'mensaje': self.mensaje.strftime('%Y-%m-%d'),
            
        }