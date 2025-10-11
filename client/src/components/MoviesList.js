import React, { useEffect, useState } from "react";

function MoviesList() {
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:5555/movies")
      .then((r) => r.json())
      .then((data) => {
        setMovies(data.movies); // Flask renvoye { "movies": [...] }
        setLoading(false);
      })
      .catch((err) => {
        console.error("Erreur:", err);
        setLoading(false);
      });
  }, []);

  if (loading) return <h2>Chargement...</h2>;

  return (
    <div style={{ padding: "20px" }}>
      <h1>🎬 Liste des films</h1>
      {movies.length === 0 ? (
        <p>Aucun film trouvé.</p>
      ) : (
        <ul>
          {movies.map((movie) => (
            <li key={movie.id}>
              <strong>{movie.title}</strong> — {movie.director} ({movie.release_year})  
              <em> [{movie.genre}] ⭐ {movie.rating}</em>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default MoviesList;
