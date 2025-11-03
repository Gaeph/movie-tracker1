from flask import request
from flask_restful import Resource
from config import app, db, api
from models import Movie, User, Review, UserMovie

# ----------------- MOVIES -----------------
class MoviesResource(Resource):
    def get(self):
        movies = [m.to_dict() for m in Movie.query.all()]
        return {"movies": movies}, 200

    def post(self):
        data = request.get_json() or {}
        movie = Movie(
            title=data.get("title"),
            director=data.get("director"),
            release_year=data.get("release_year"),
            genre=data.get("genre"),
            rating=data.get("rating")
        )
        db.session.add(movie)
        db.session.commit()
        return movie.to_dict(), 201

class MovieResource(Resource):
    def get(self, movie_id):
        movie = Movie.query.get_or_404(movie_id)
        return movie.to_dict(), 200

    def patch(self, movie_id):
        movie = Movie.query.get_or_404(movie_id)
        data = request.get_json() or {}
        for k in ("title", "director", "release_year", "genre", "rating"):
            if k in data:
                setattr(movie, k, data[k])
        db.session.commit()
        return movie.to_dict(), 200

    def delete(self, movie_id):
        movie = Movie.query.get_or_404(movie_id)
        db.session.delete(movie)
        db.session.commit()
        return {}, 204

# ----------------- USERS -----------------
class UsersResource(Resource):
    def get(self):
        users = [u.to_dict() for u in User.query.all()]
        return {"users": users}, 200

    def post(self):
        data = request.get_json() or {}
        user = User(
            username=data.get("username"),
            email=data.get("email")
        )
        db.session.add(user)
        db.session.commit()
        return user.to_dict(), 201

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user.to_dict(), 200

# ----------------- REVIEWS -----------------
class ReviewsResource(Resource):
    def get(self):
        reviews = [r.to_dict() for r in Review.query.all()]
        return {"reviews": reviews}, 200

    def post(self):
        data = request.get_json() or {}
        review = Review(
            content=data.get("content"),
            rating=data.get("rating"),
            user_id=data.get("user_id"),
            movie_id=data.get("movie_id")
        )
        db.session.add(review)
        db.session.commit()
        return review.to_dict(), 201

class ReviewResource(Resource):
    def get(self, review_id):
        review = Review.query.get_or_404(review_id)
        return review.to_dict(), 200

# ----------------- USER-MOVIE (Many-to-Many) -----------------
class UserMovieResource(Resource):
    def post(self):
        data = request.get_json() or {}
        assoc = UserMovie(
            user_id=data.get("user_id"),
            movie_id=data.get("movie_id"),
            user_rating=data.get("user_rating"),
            favorite=data.get("favorite", False)
        )
        db.session.add(assoc)
        db.session.commit()
        return assoc.to_dict(), 201

# ----------------- ROUTES -----------------
api.add_resource(MoviesResource, '/movies')
api.add_resource(MovieResource, '/movies/<int:movie_id>')

api.add_resource(UsersResource, '/users')
api.add_resource(UserResource, '/users/<int:user_id>')

api.add_resource(ReviewsResource, '/reviews')
api.add_resource(ReviewResource, '/reviews/<int:review_id>')

api.add_resource(UserMovieResource, '/user_movies')

# ----------------- RUN SERVER -----------------
if __name__ == '__main__':
    app.run(port=5555, debug=True)
