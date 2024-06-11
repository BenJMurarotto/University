import React, { useState } from 'react';
import axios from 'axios';
import './App.css';  // Import the CSS file

const App = () => {
    const [fighterName, setFighterName] = useState('');
    const [searchResults, setSearchResults] = useState([]);
    const [guesses, setGuesses] = useState([]);
    const [error, setError] = useState('');

    const searchFighters = async (name) => {
        try {
            const response = await axios.get(`http://localhost:5000/ajax_search`, {
                params: { fightername: name },
                withCredentials: true
            });
            setSearchResults(response.data);
        } catch (error) {
            console.error('Error fetching fighters:', error);
        }
    };

    const getFighterDetails = async (name) => {
        try {
            const response = await axios.get(`http://localhost:5000/fighter_details`, {
                params: { fightername: name },
                withCredentials: true
            });
            if (response.data.error) {
                setError(response.data.error);
            } else {
                setError('');
                setGuesses(prevGuesses => {
                    if (prevGuesses.length < 6) {
                        return [...prevGuesses, response.data];
                    }
                    return prevGuesses;
                });
            }
        } catch (error) {
            console.error('Error fetching fighter:', error);
            setError('Error fetching fighter details');
        }
    };

    const handleSearchChange = (event) => {
        const name = event.target.value;
        setFighterName(name);
        if (name.length >= 2) {
            searchFighters(name);
        } else {
            setSearchResults([]);
        }
    };

    const handleSearchClick = (name) => {
        setFighterName(name);
        setSearchResults([]);
        getFighterDetails(name);
    };

    const handleGuess = () => {
        if (guesses.length < 6) {
            getFighterDetails(fighterName);
        } else {
            setError('Maximum of 6 guesses reached');
        }
    };

    return (
        <div className="container">
            <div className="search-container">
                <h1 className='header'> UFCdle</h1>
                <input
                    type="text"
                    value={fighterName}
                    onChange={handleSearchChange}
                    placeholder="Enter fighter's name"
                />
                <button className='header' onClick={handleGuess}>Guess</button>
                {error && <p>{error}</p>}
                <div className="search-results">
                    {searchResults.map((fighter, index) => (
                        <p key={index} onClick={() => handleSearchClick(`${fighter.fname} ${fighter.lname}`)}>
                            {fighter.fname} {fighter.lname}
                        </p>
                    ))}
                </div>
            </div>
            <div className="guesses-container">
                {guesses.map((fighter, index) => (
                    <div key={index} className="guess">
                        <p><strong> Guess {index + 1} </strong></p>
                        <p><strong>{fighter.fname} {fighter.lname}</strong></p>
                        <p>Rank: {fighter.rank}</p>
                        <p>Division: {fighter.division}</p>
                        <p>Style: {fighter.style}</p>
                        <p>Country: {fighter.country}</p>
                        <p>Debut: {fighter.debut}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default App;
