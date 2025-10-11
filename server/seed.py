from config import db, app
from models import Movie

with app.app_context():
    Movie.query.delete()  

    movies = [
        Movie(title="Inception", director="Christopher Nolan", release_year=2010, genre="Sci-Fi", rating=8.8),
        Movie(title="Titanic", director="James Cameron", release_year=1997, genre="Romance", rating=7.8),
        Movie(title="The Matrix", director="Wachowski Sisters", release_year=1999, genre="Action", rating=8.7),
    ]

    db.session.add_all(movies)
    db.session.commit()
    print("Seed terminé !")
