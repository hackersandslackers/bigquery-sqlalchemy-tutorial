SELECT
  REPLACE(title, ' - Hackers and Slackers', '') as title,
  url,
  REPLACE(REPLACE(url, 'https://hackersandslackers.com/', ''), '/' , '') as slug,
  COUNT(title) AS views
FROM
  hackersgatsbyprod.pages
WHERE
  timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 day)
GROUP BY
  title,
  url
ORDER BY
  COUNT(title) DESC
LIMIT
  500;
