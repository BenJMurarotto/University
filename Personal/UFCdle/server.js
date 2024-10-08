const express = require('express');
const cors = require('cors');
const sqlite3 = require('sqlite3').verbose();
const app = express();
const port = 3000;
const path = require('path');


// Enable CORS for cross-origin requests
app.use(cors());

app.use(express.static(path.join(__dirname, 'public')));

// Connect to SQLite database
const db = new sqlite3.Database('./back/app/misc/ufcdle.db', (err) => {
  if (err) {
    console.error('Error opening database:', err.message);
    return;
  }
  console.log('Connected to the SQLite database.');
});

// API route to fetch data from the SQLite database
app.get('/data', (req, res) => {
  const sql = 'SELECT * FROM fighters'; // Replace with your table name
  db.all(sql, [], (err, rows) => {
    if (err) {
      console.error('Error fetching data:', err.message);
      res.status(500).json({ error: 'Failed to fetch data' });
      return;
    }
    res.json(rows);
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
