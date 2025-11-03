from config import db, app
from models import Movie, User, Review, UserMovie

with app.app_context():
    # Clear existing data
    UserMovie.query.delete()
    Review.query.delete()
    Movie.query.delete()
    User.query.delete()

    # ----- Users -----
    users = [
        User(username="alice", email="alice@example.com"),
        User(username="bob", email="bob@example.com")
    ]
    db.session.add_all(users)
    db.session.commit()

    # ----- Movies -----
    movies = [
        Movie(title="Inception", director="Christopher Nolan", release_year=2010, genre="Sci-Fi", rating=8.8),
        Movie(title="Titanic", director="James Cameron", release_year=1997, genre="Romance", rating=7.8),
        Movie(title="The Matrix", director="Wachowski Sisters", release_year=1999, genre="Action", rating=8.7),
    ]
    db.session.add_all(movies)
    db.session.commit()

    # ----- Reviews -----
    reviews = [
        Review(content="Amazing movie!", rating=9, user_id=users[0].id, movie_id=movies[0].id),
        Review(content="Classic romance", rating=8, user_id=users[1].id, movie_id=movies[1].id),
        Review(content="Mind-blowing visuals", rating=9.5, user_id=users[0].id, movie_id=movies[2].id),
    ]
    db.session.add_all(reviews)
    db.session.commit()

    # ----- User-Movie many-to-many -----
    user_movies = [
        UserMovie(user_id=users[0].id, movie_id=movies[0].id, user_rating=9, favorite=True),
        UserMovie(user_id=users[1].id, movie_id=movies[1].id, user_rating=8, favorite=False),
        UserMovie(user_id=users[0].id, movie_id=movies[2].id, user_rating=9.5, favorite=True),
    ]
    db.session.add_all(user_movies)
    db.session.commit()

    print("Seed terminé !")
