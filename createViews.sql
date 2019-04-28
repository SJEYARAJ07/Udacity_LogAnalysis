
CREATE OR REPLACE VIEW calculate_total AS
SELECT
      DATE(time) AS day,
      COUNT(*) AS noofViews
FROM log
GROUP BY day
ORDER BY day;

CREATE OR REPLACE VIEW error_distribution AS
SELECT
      DATE(time) AS day,
      count(*) AS noofViews
FROM log
WHERE status LIKE '%404%'
GROUP BY day;

CREATE OR REPLACE VIEW elevated_error AS
SELECT
      calculate_total.day,
      (ROUND(cast((100*error_distribution.hits) AS NUMERIC) / cast(calculate_total.hits AS NUMERIC), 2)) AS error_rate
FROM calculate_total INNER JOIN error_distribution
ON calculate_total.day = error_distribution.day;

CREATE OR REPLACE VIEW map_articlesauthor AS
SELECT
      title,
      name
FROM articles, authors
WHERE articles.author = authors.id;

CREATE OR REPLACE VIEW map_articlesview AS
SELECT
      articles.title,
      COUNT(log.id) AS views
FROM articles, log
WHERE log.path = CONCAT('/article/', articles.slug)
GROUP BY articles.title
ORDER BY views DESC;
