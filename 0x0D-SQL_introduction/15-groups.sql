-- Displays the score.
-- Script that displays the same scores.
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
