from flask import request
from flask_restful import Resource
from config import app, db, api
from models import Movie
from flask_cors import CORS

CORS(app)

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
        for k in ("title","director","release_year","genre","rating"):
            if k in data:
                setattr(movie, k, data[k])
        db.session.commit()
        return movie.to_dict(), 200

    def delete(self, movie_id):
        movie = Movie.query.get_or_404(movie_id)
        db.session.delete(movie)
        db.session.commit()
        return {}, 204

api.add_resource(MoviesResource, '/movies')
api.add_resource(MovieResource, '/movies/<int:movie_id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
