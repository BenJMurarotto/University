CREATE VIEW movie_summary AS
    SELECT m.movie_title, m.release_date, s.media_type, s.retail_price
    FROM movies AS m
    INNER JOIN stock AS s ON s.movie_id = m.movie_id
    ;

CREATE VIEW old_shipments AS
    SELECT c.first_name, c.last_name, m.movie_id, sh.shipment_id, sh.shipment_date
    FROM customers AS c
    INNER JOIN shipments AS sh ON c.customer_id = sh.customer_id
    INNER JOIN stock AS s ON sh.movie_id = s.movie_id
    WHERE YEAR(shipment_date) < 2010
    ;

CREATE VIEW richie AS
    SELECT movie_title
    FROM movies
    WHERE director_first_name = 'Ron' AND director_last_name = 'Howard'
    ;

CREATE VIEW retail_price_hike AS
    SELECT movie_id, retail_price, retail_price * 1.25
    FROM stock
    ;

CREATE VIEW profits_from_movie AS
    SELECT m.movie_id, m.movie_title, SUM(s.cost_price) - SUM(s.retail_price) AS price_diff  
    FROM movies AS m
    INNER JOIN stock AS s ON s.movie_id = m.movie_id
    GROUP BY m.movie_title
    ;

CREATE VIEW binge_watcher AS
    SELECT m.first_name, m.last_name
    FROM movies AS m
    INNER JOIN shipments AS sh ON c.customer_id = sh.shipment_id
    GROUP BY sh.shipment_date
    HAVING COUNT(sh.shipment_id) > 1

    ;
CREATE VIEW the_sith AS
    SELECT c.first_name, c.last_name
    FROM customers AS c
    INNER JOIN shipments AS sh ON sh.customer_id = c.customer_id
    INNER JOIN stock AS s ON sh.movie_id = s.movie_id
    INNER JOIN movies AS m ON m.movie_id = s.movie_id
    WHERE movie_title  
    GROUP BY customer_id
    HAVING shipment_id