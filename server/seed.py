from config import db
from models import Movie
from faker import Faker

fake = Faker()

def seed():
    db.drop_all()
    db.create_all()
    sample = [
        {"title":"The Matrix","director":"Lana Wachowski","release_year":1999,"genre":"Sci-Fi","rating":8.7},
        {"title":"Inception","director":"Christopher Nolan","release_year":2010,"genre":"Sci-Fi","rating":8.8},
        {"title":"Parasite","director":"Bong Joon-ho","release_year":2019,"genre":"Thriller","rating":8.6},
    ]
    for s in sample:
        m = Movie(**s)
        db.session.add(m)
    db.session.commit()
    print("Seeded sample movies.")

if __name__ == '__main__':
    seed()
