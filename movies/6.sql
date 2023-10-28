SELECT
  AVG(rating)
FROM
  ratings
  JOIN movies ON ratings.movie_id = movies.id
WHERE
  YEAR = 2012;