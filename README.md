# Movie Tracker

Minimal full-stack Movie Tracker example (Flask backend + React frontend).

## Quick start (backend)
```
cd server
pipenv install
pipenv shell
flask db init
flask db revision -m "create db"
flask db upgrade head
python app.py
```

## Quick start (frontend)
```
npm install --prefix client
npm start --prefix client
```

Frontend runs at http://localhost:3000 and proxies API requests to http://localhost:5555.
