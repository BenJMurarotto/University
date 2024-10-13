const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const app = express();
const port = 3000;
const path = require('path');
let tableCounter = 0; // Variable to count number of unique values in the table.

app.use(express.static(path.join(__dirname, 'public')));

// Connect to SQLite database
const db = new sqlite3.Database('./back/app/misc/ufcdle.db', (err) => {
  if (err) {
    console.error('Error opening database:', err.message);
    return;
  }
  console.log('Connected to the SQLite database.');
});
// Choose a random fighter for game logic
function tableCount() {
  const sql = 'COUNT * from fighters';
  db.all(sql, [], (err, rows) => {
    if (err) {
      console.error('Error fetching', err.message);
      return;
    tableCounter = rows.length;
    console.log(`Row count equals ${tableCounter}`);

    }

  })
}



// API route for dynamic AJAX search.
app.get('/api/data', (req, res) => {
  const searchQuery = req.query.name ? `${req.query.name}%` : '%';
  const sql = 'SELECT * FROM fighters WHERE fname LIKE ?';
  db.all(sql, [searchQuery], (err, rows) => {
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
