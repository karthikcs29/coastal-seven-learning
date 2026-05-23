import sqlite3
from flask import Flask, request, jsonify, render_template, g

app = Flask(__name__)
DATABASE = "movies.db"

# --- Database helpers ---
def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            director TEXT,
            year INTEGER,
            genre TEXT,
            rating REAL
        )
        """)
        db.commit()

# --- Routes ---
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/movies", methods=["GET"])
def get_movies():
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM movies")
    rows = cursor.fetchall()
    movies = [
        {"id": r[0], "title": r[1], "director": r[2], "year": r[3], "genre": r[4], "rating": r[5]}
        for r in rows
    ]
    return jsonify(movies)

@app.route("/movies", methods=["POST"])
def add_movie():
    data = request.json
    cursor = get_db().cursor()
    cursor.execute("INSERT INTO movies (title, director, year, genre, rating) VALUES (?, ?, ?, ?, ?)",
                   (data["title"], data["director"], data["year"], data["genre"], data["rating"]))
    get_db().commit()
    return jsonify({"message": "Movie added!"})

@app.route("/movies/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    data = request.json
    cursor = get_db().cursor()
    cursor.execute("UPDATE movies SET title=?, director=?, year=?, genre=?, rating=? WHERE id=?",
                   (data["title"], data["director"], data["year"], data["genre"], data["rating"], movie_id))
    get_db().commit()
    return jsonify({"message": "Movie updated!"})

@app.route("/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    cursor = get_db().cursor()
    cursor.execute("DELETE FROM movies WHERE id=?", (movie_id,))
    get_db().commit()
    return jsonify({"message": "Movie deleted!"})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
