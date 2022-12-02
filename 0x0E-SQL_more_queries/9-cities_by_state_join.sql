-- joins two tables
-- Using inner join to two two table.
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id;
