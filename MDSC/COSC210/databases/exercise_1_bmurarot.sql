CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    last_name VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    address VARCHAR(200),
    city VARCHAR(50),
    state VARCHAR(3) CHECK (state IN ('NSW', 'VIC', 'QLD', 'ACT', 'NT', 'WA', 'SA','TAS')),
    postcode VARCHAR(8)
);

CREATE TABLE Movies (
    movie_id INT PRIMARY KEY,
    movie_title VARCHAR(100) NOT NULL,
    director_first_name VARCHAR(50) NOT NULL,
    director_last_name VARCHAR(50) NOT NULL,
    genre VARCHAR(20),
    release_date DATE,
    studio_name VARCHAR(50),
    CHECK (genre IN ('Action', 'Adventure', 'Comedy', 'Romance', 'Science Fiction', 'Documentary', 'Drama', 'Horror'))
);

CREATE TABLE Stock (
    movie_id INT,
    media_type VARCHAR(20),
    cost_price FLOAT,
    retail_price FLOAT,
    current_stock FLOAT,
    CHECK (media_type IN ('DVD', 'Blu-Ray', 'Stream-Media')),
    CHECK (cost_price > 0),
    CHECK (retail_price > 0),
    CHECK (current_stock >= 0),
    PRIMARY KEY (movie_id, media_type),
    CONSTRAINT fk_movie_id_Stock FOREIGN KEY (movie_id) REFERENCES Movies (movie_id)
);

CREATE TABLE Shipments (
    shipment_id INT PRIMARY KEY,
    customer_id INT,
    movie_id INT,
    media_type VARCHAR(20),
    shipment_date DATE,
    CONSTRAINT fk_customer_id FOREIGN KEY (customer_id) REFERENCES Customers (customer_id),
    CONSTRAINT fk_movie_id_Shipments FOREIGN KEY (movie_id, media_type) REFERENCES Stock (movie_id, media_type),
    CONSTRAINT fk_media_type_Shipments FOREIGN KEY (movie_id, media_type) REFERENCES Stock (movie_id, media_type)
);