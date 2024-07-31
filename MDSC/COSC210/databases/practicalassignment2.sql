CREATE VIEW movie_summary AS
    SELECT m.movie_title, m.release_date, s.media_type, s.retail_price
    FROM movies AS m
    INNER JOIN stock AS s ON s.movie_id = m.movie_id
    ;

CREATE VIEW old_shipments AS
    SELECT c.first_name, c.last_name, s.movie_id, sh.shipment_id, sh.shipment_date
    FROM customers AS c
    INNER JOIN shipments AS sh ON c.customer_id = sh.customer_id
    INNER JOIN stock AS s ON sh.movie_id = s.movie_id
    WHERE EXTRACT(YEAR FROM sh.shipment_date) < 2010
    ;

CREATE VIEW richie AS
    SELECT movie_title
    FROM movies
    WHERE director_first_name = 'Ron' AND director_last_name = 'Howard'
    ;

CREATE VIEW retail_price_hike AS
    SELECT movie_id, retail_price, retail_price * 1.25 AS price_hike
    FROM stock
    ;

CREATE VIEW profits_from_movie AS
    SELECT m.movie_id, m.movie_title, SUM(s.retail_price) - SUM(s.cost_price) AS price_diff  
    FROM movies AS m
    INNER JOIN stock AS s ON s.movie_id = m.movie_id
    GROUP BY m.movie_id
    ORDER BY price_diff ASC
    ;

CREATE VIEW binge_watcher AS
    SELECT sh.shipment_date, c.first_name, c.last_name
    FROM shipments AS sh
    INNER JOIN customers AS c ON c.customer_id = sh.customer_id
    GROUP BY sh.shipment_date, c.first_name, c.last_name
    HAVING COUNT(sh.shipment_id) > 1
    ;


CREATE VIEW the_sith AS
SELECT c.first_name, c.last_name
FROM customers AS c
WHERE c.customer_id NOT IN (
    SELECT DISTINCT c.customer_id
    FROM customers as c
    INNER JOIN shipments sh ON c.customer_id = sh.shipment_id
    INNER JOIN stock s ON sh.media_type = s.media_type
    INNER JOIN movies m ON s.movie_id = m.movie_id
    WHERE movie_title = 'Star Wars: Episode V - The Empire Strikes Back'
);

SELECT c.first_name, c.last_name
FROM customers AS c
(
    SELECT DISTINCT c.customer_id
    FROM customers as c
    INNER JOIN shipments sh ON c.customer_id = sh.shipment_id
    INNER JOIN stock s ON sh.media_type = s.media_type
    INNER JOIN movies m ON s.movie_id = m.movie_id
    WHERE movie_title = '12 Angry Men'
);

