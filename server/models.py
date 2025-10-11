from config import db
from sqlalchemy_serializer import SerializerMixin

class Movie(db.Model, SerializerMixin):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    director = db.Column(db.String)
    release_year = db.Column(db.Integer)
    genre = db.Column(db.String)
    rating = db.Column(db.Float)

    def __repr__(self):
        return f"<Movie {self.title}>"
