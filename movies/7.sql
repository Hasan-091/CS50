SELECT
  movies.title,
  ratings.rating
FROM
  movies
  JOIN ratings ON ratings.movie_id = movies.id
WHERE
  YEAR = 2010
ORDER BY
  2 DESC,
  1;