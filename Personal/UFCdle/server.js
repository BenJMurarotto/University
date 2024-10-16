const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const app = express();
const port = 3000;
const path = require('path');
const Papa = require('papaparse');
const fs = require('fs');
const csvFile = fs.readFileSync('./public/countriesbycontinent.csv', 'utf-8');
let countriesToContinent = {}

app.use(express.static(path.join(__dirname, 'public')));

// Connect to SQLite database
const db = new sqlite3.Database('./back/app/misc/ufcdle.db', (err) => {
  if (err) {
    console.error('Error opening database:', err.message);
    return;
  }
  console.log('Connected to the SQLite database.');
});

function parseCountryCSV() {
  Papa.parse(csvFile, {
    header: true,
    skipEmptyLines: true,
    complete: function(results) {
        continentToCountries = createMapping(results.data);
        console.log('continentToCountries on server:', continentToCountries); // Check this log
    }
});

}
parseCountryCSV();

function createMapping(data) {
  const mapping = {};
  data.forEach(row => {
    const { Country, Continent } = row;
    if (!mapping[Continent]) {
      mapping[Continent] = [];
    }
    mapping[Continent].push(Country);
  });
  return mapping;
}

app.get('/api/countries', (req, res) => {
  console.log('Sending continentToCountries:', continentToCountries); // Log to see what's being sent
  res.json(continentToCountries);
});



// API route for dynamic AJAX search
app.get('/api/data', (req, res) => {
  const searchQuery = req.query.name ? `%${req.query.name}%` : '%';
  const sql = `
    SELECT * FROM fighters
    WHERE LOWER(fname) LIKE LOWER(?) OR LOWER(lname) LIKE LOWER(?)
  `;
  db.all(sql, [searchQuery, searchQuery], (err, rows) => { // Passing searchQuery twice
    if (err) {
      console.error('Error fetching data:', err.message);
      res.status(500).json({ error: 'Failed to fetch data' });
      return;
    }
    res.json(rows); // Return the matched rows
  });
});

// API route to get a secret fighter by ID
app.get('/api/data/secretfighter', (req, res) => {
  const searchQuery = req.query.id;
  const sql = 'SELECT * FROM fighters WHERE id = ?';
  db.get(sql, [searchQuery], (err, row) => {
    if (err) {
      console.error('Error fetching data:', err.message);
      res.status(500).json({ error: 'Failed to fetch data' });
      return;
    }
    res.json(row); // Return the single matched row
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
