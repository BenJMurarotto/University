import React, { useState } from 'react';
import axios from 'axios';
import './App.css';
import { checkGuess, maxGuesses } from './utils/gameLogic';

function App() {
  const [fighters, setFighters] = useState([]);
  const [search, setSearch] = useState('');
  const [result, setResult] = useState(null);
  const [guessedFighters, setGuessedFighters] = useState([]);
  const [currentGuess, setCurrentGuess] = useState(null);

  const handleSearchChange = (event) => {
    const fightername = event.target.value;
    setSearch(fightername);
    if (fightername.length >= 2) {
      axios.get(`http://localhost:5000/ajax_search?fightername=${fightername}`)
        .then(response => {
          setFighters(response.data);
        })
        .catch(error => {
          console.error('There was an error fetching the fighters!', error);
        });
    } else {
      setFighters([]);
    }
  };

  const selectFighter = (fullName) => {
    setSearch(fullName);
    setFighters([]);
    submitGuess(fullName);
  };

  const submitGuess = (fightername) => {
    console.log('Submitting guess for:', fightername);  // Debugging statement
    if (guessedFighters.some(f => f.fightername === fightername)) {
      alert("You have already guessed this fighter!");
      return;
    }

    if (guessedFighters.length >= maxGuesses) {
      alert("No more guesses allowed!");
      return;
    }

    axios.post('http://localhost:5000/guess', { fightername }, {
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(response => {
        console.log('Response received:', response.data);  // Debugging statement
        const data = response.data;
        if (data.error) {
          alert(data.error);
        } else {
          setGuessedFighters(prevGuessedFighters => [
            ...prevGuessedFighters, 
            { fightername, data: data.fighter }
          ]);
          setCurrentGuess(data.fighter);
          setResult(data);

          if (guessedFighters.length + 1 === maxGuesses) {
            alert(`You've used all your guesses! The secret fighter was: ${data.secret_fighter.fname} ${data.secret_fighter.lname}`);
          }
        }
      })
      .catch(error => {
        console.error('There was an error processing the guess!', error);
      });
  };

  return (
    <div className="App">
      <h1>UFCdle</h1>
      <form id="guess-form" onSubmit={(e) => { e.preventDefault(); submitGuess(search); }}>
        <input
          type="text"
          name="fightername"
          id="fightername"
          value={search}
          onChange={handleSearchChange}
          placeholder="Enter fighter's name"
        />
        <button type="submit">Guess</button>
      </form>
      <div id="search-results">
        {fighters.map((fighter, index) => (
          <div key={index} className="guess-line">
            <p onClick={() => selectFighter(`${fighter.fname} ${fighter.lname}`)}>
              {fighter.fname} {fighter.lname}
            </p>
          </div>
        ))}
      </div>
      <div id="guess-results">
        {guessedFighters.map((guess, index) => (
          <div key={index}>
            <h3>Guess {index + 1}:</h3>
            <p>Name: {guess.data.fname} {guess.data.lname}</p>
            <p>Nickname: {guess.data.nickname}</p>
            <p>Rank: {guess.data.rank}</p>
            <p>Division: {guess.data.division}</p>
            <p>Style: {guess.data.style}</p>
            <p>Country: {guess.data.country}</p>
            <p>Debut: {guess.data.debut}</p>
            <hr />
          </div>
        ))}
        {result && (
          <div>
            <h3>Your Guess:</h3>
            <div>
              {checkGuess(result.fighter, result.secret_fighter).map(({ attr, isMatch }) => (
                <span key={attr} className={isMatch ? 'match' : ''}>
                  {result.fighter[attr]} {isMatch && <strong>{result.fighter[attr]}</strong>} | 
                </span>
              ))}
            </div>
            {guessedFighters.length === maxGuesses && (
              <div>
                <p>The secret fighter was: {result.secret_fighter.fname} {result.secret_fighter.lname}</p>
              </div>
            )}
          </div>
        )}
        {currentGuess && (
          <div>
            <h3>Current Guessed Fighter:</h3>
            <p>Name: {currentGuess.fname} {currentGuess.lname}</p>
            <p>Nickname: {currentGuess.nickname}</p>
            <p>Rank: {currentGuess.rank}</p>
            <p>Division: {currentGuess.division}</p>
            <p>Style: {currentGuess.style}</p>
            <p>Country: {currentGuess.country}</p>
            <p>Debut: {currentGuess.debut}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
