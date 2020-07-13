-- max temps by state
-- selects state and max temp from that state grouped by state
select state, MAX(value) AS max_temp FROM temperatures GROUP BY state;
