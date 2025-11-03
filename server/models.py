from config import db
from sqlalchemy_serializer import SerializerMixin

# Many-to-many association table (optional, men rekòmande)
class UserMovie(db.Model, SerializerMixin):
    __tablename__ = "user_movies"
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"), primary_key=True)
    user_rating = db.Column(db.Float)  # user-submittable attribute
    favorite = db.Column(db.Boolean, default=False)

    user = db.relationship("User", back_populates="movies_assoc")
    movie = db.relationship("Movie", back_populates="users_assoc")


class User(db.Model, SerializerMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)

    # One-to-many relationship
    reviews = db.relationship("Review", back_populates="user", cascade="all, delete-orphan")

    # Many-to-many relationship
    movies_assoc = db.relationship("UserMovie", back_populates="user")
    movies = db.relationship("Movie", secondary="user_movies", back_populates="users")

    def __repr__(self):
        return f"<User {self.id}: {self.username}>"


class Movie(db.Model, SerializerMixin):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    director = db.Column(db.String)
    release_year = db.Column(db.Integer)
    genre = db.Column(db.String)
    rating = db.Column(db.Float)

    # One-to-many relationship
    reviews = db.relationship("Review", back_populates="movie", cascade="all, delete-orphan")

    # Many-to-many relationship
    users_assoc = db.relationship("UserMovie", back_populates="movie")
    users = db.relationship("User", secondary="user_movies", back_populates="movies")

    def __repr__(self):
        return f"<Movie {self.id}: {self.title}>"


class Review(db.Model, SerializerMixin):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"), nullable=False)

    # Relationships
    user = db.relationship("User", back_populates="reviews")
    movie = db.relationship("Movie", back_populates="reviews")

    def __repr__(self):
        return f"<Review {self.id}: User {self.user_id}, Movie {self.movie_id}>"
