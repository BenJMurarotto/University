import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import Modal from './Modal';

const App = () => {
    const [fighterName, setFighterName] = useState('');
    const [searchResults, setSearchResults] = useState([]);
    const [guesses, setGuesses] = useState([]);
    const [secretFighter, setSecretFighter] = useState(null);
    const [error, setError] = useState('');
    const [showModal, setShowModal] = useState(false);

    useEffect(() => {
        const fetchSecretFighter = async () => {
            try {
                const response = await axios.get('http://localhost:5000/get_secret_fighter', { withCredentials: true });
                console.log('Fetched Secret Fighter:', response.data); // Debugging log
                setSecretFighter(response.data);
            } catch (error) {
                console.error('Error fetching secret fighter:', error);
            }
        };
        fetchSecretFighter();
    }, []);

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

                // Ensure secretFighter is not null before making comparisons
                if (secretFighter && response.data.fname === secretFighter.fname && response.data.lname === secretFighter.lname) {
                    setShowModal(true);
                } else if (guesses.length >= 5) {
                    setShowModal(true);  // Show modal after the sixth guess
                }
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
            setShowModal(true);  // Show modal after the sixth guess
        }
    };

    const isMatch = (attribute, fighter) => {
        return secretFighter && secretFighter[attribute] === fighter[attribute] ? 'match' : '';
    };

    const handleCloseModal = () => {
        setShowModal(false);
    };

    return (
        <div className="container">
            <div className="search-container">
                <h1>UFCdle</h1>
                <input
                    type="text"
                    value={fighterName}
                    onChange={handleSearchChange}
                    placeholder="Enter fighter's name"
                />
                <button onClick={handleGuess}>Guess</button>
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
                        <p className={isMatch('fname', fighter)}><strong>{fighter.fname}</strong></p>
                        <p className={isMatch('lname', fighter)}><strong>{fighter.lname}</strong></p>
                        <p className={isMatch('nickname', fighter)}>Nickname: {fighter.nickname}</p>
                        <p className={isMatch('rank', fighter)}>Rank: {fighter.rank}</p>
                        <p className={isMatch('division', fighter)}>Division: {fighter.division}</p>
                        <p className={isMatch('style', fighter)}>Style: {fighter.style}</p>
                        <p className={isMatch('country', fighter)}>Country: {fighter.country}</p>
                        <p className={isMatch('debut', fighter)}>Debut: {fighter.debut}</p>
                    </div>
                ))}
            </div>
            <Modal show={showModal} handleClose={handleCloseModal} secretFighter={secretFighter} />
        </div>
    );
};

export default App;
