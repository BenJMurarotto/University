import { format } from 'date-fns';
let debounceTimeout;
let selectedFighters = [];
let fighterDivisions = [`Women's Strawweight`, `Women's Flyweight`, `Women's Bantamweight`, `Flyweight`, `Bantamweight`, `Featherweight`, `Lightweight`, `Welterweight`, `Middleweight`, `Light Heavyweight`, `Heavyweight`];
let continentToCountries = {};

document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/countries')
        .then(response => response.json())
        .then(data => {
            continentToCountries = data;
            console.log('Continent to countries mapping loaded:', continentToCountries);
        });
});

document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('search-input');
    const dropdown = document.getElementById('dropdown');
    searchInput.addEventListener('input', () => {
        clearTimeout(debounceTimeout);
        debounceTimeout = setTimeout(() => {
            searchFighter();
        }, 150);
    });

    // Fetch the secret fighter on page load
    getSecretFighter();

    // Hide dropdown when clicking outside
    document.addEventListener('click', (event) => {
        if (!searchInput.contains(event.target) && !dropdown.contains(event.target)) {
            dropdown.style.display = 'none';
        }
    });
});

// Function to retrieve search requests from the client
function searchFighter() {
    const searchQuery = document.getElementById('search-input').value;
    if (searchQuery.length < 2) {
        clearResults();
        return;
    }
    fetch(`/api/data?name=${encodeURIComponent(searchQuery)}`)
        .then(response => response.json())
        .then(data => {
            const dropdown = document.getElementById('dropdown');
            dropdown.innerHTML = ''; // Clear previous results

            if (data.length === 0) {
                dropdown.style.display = 'none'; // Hide dropdown if no results
            } else {
                data.forEach(fighter => {
                    const dropdownDiv = document.createElement('div');
                    dropdownDiv.classList.add('dropdown-item');
                    dropdownDiv.textContent = `${fighter.fname} ${fighter.lname}`;
                    dropdownDiv.addEventListener('click', () => {
                        const fightersTable = document.getElementById('fighters-table');
                        if (fightersTable.style.display === 'none') {
                            fightersTable.style.display = 'table'; // Make the table visible
                        }
                        appendSelectedFighter(fighter); // Add the selected fighter to the table
                        dropdown.style.display = 'none'; // Hide dropdown after selection
                    });
                    dropdown.appendChild(dropdownDiv);
                });
                dropdown.style.display = 'block'; // Show the dropdown with results
            }
        })
        .catch(error => {
            console.error('Error fetching fighter data:', error);
        });
}

// Function to append selected fighter to the table and compare with secret fighter
function appendSelectedFighter(fighter) {
    const fightersTableBody = document.getElementById('fighters-body');
    
    // Check if secretFighter is loaded before comparing
    if (!secretFighter || !secretFighter.id) {
        console.error('Secret fighter not loaded yet.');
        return;
    }
    
    // Check if the fighter is already in the selected list using their unique id
    if (!selectedFighters.includes(fighter.id)) {
        if (fightersTableBody.rows.length >= 6) {
            fightersTableBody.deleteRow(0); // If there are already 6 rows, remove the oldest one
        }

        const row = document.createElement('tr');

        // 1. Full Name Cell (no comparison here)
        const fullNameCell = document.createElement('td');
        fullNameCell.textContent = `${fighter.fname} ${fighter.lname}`;
        row.appendChild(fullNameCell);

        // 2. Division Cell (comparison logic)
        const divisionCell = document.createElement('td');
        if (Math.abs(fighterDivisions.indexOf(fighter.division) - fighterDivisions.indexOf(secretFighter.division)) <= 1) {
            divisionCell.style.color = 'orange';
        }
        if (fighterDivisions.indexOf(fighter.division) < fighterDivisions.indexOf(secretFighter.division)) {
            divisionCell.textContent = fighter.division + ' ▲';
        } else if (fighterDivisions.indexOf(fighter.division) > fighterDivisions.indexOf(secretFighter.division)) {
            divisionCell.textContent = fighter.division + ' ▼';
        } else {
            divisionCell.textContent = fighter.division;
            divisionCell.style.color = 'green';
        }
        row.appendChild(divisionCell);

        // 3. Rank Cell (comparison logic)
        const rankCell = document.createElement('td');
        if (fighter.rank < secretFighter.rank) {
            rankCell.textContent = fighter.rank + ' ▼';
        } else if (fighter.rank > secretFighter.rank) {
            rankCell.textContent = fighter.rank + ' ▲';
        } else {
            rankCell.textContent = fighter.rank;
            rankCell.style.color = 'green';
        }
        row.appendChild(rankCell);

        // 4. Style Cell
        const styleCell = document.createElement('td');
        styleCell.textContent = fighter.style;
        if (fighter.style === secretFighter.style) {
            styleCell.style.color = 'green';
        }
        row.appendChild(styleCell);

        // 5. Country Cell
        const countryCell = document.createElement('td');
        countryCell.textContent = fighter.country;

        if (fighter.country === secretFighter.country) {
            countryCell.style.color = 'green';
        }
            else if (continentToCountries[fighter.country] == continentToCountries[secretFighter.country]) {
                countryCell.style.color = 'orange';
                console.log(continentToCountries[secretFighter.country])
                console.log(continentToCountries[fighter.country])
            }
        row.appendChild(countryCell);

        // 6. Debut Cell

        // Convert debut dates to Date objects if they are in string format
        const fighterDebutDate = new Date(fighter.debut);
        const secretFighterDebutDate = new Date(secretFighter.debut);
        
        // Ensure the dates are valid before formatting and comparing
        if (!isNaN(fighterDebutDate) && !isNaN(secretFighterDebutDate)) {
            // Format the dates using 'MMM yyyy'
            const formattedDebutDate = format(fighterDebutDate, 'MMM yyyy');
            
            // Compare the debut dates
            var debutAddon = fighterDebutDate < secretFighterDebutDate ? ' ▲' : ' ▼';
            
            // Create the table cell for debut
            const debutCell = document.createElement('td');
            debutCell.textContent = formattedDebutDate + debutAddon;
            
            // If the debut dates are the same, highlight the cell in green
            if (fighterDebutDate.getTime() === secretFighterDebutDate.getTime()) {
                debutAddon = ''
                debutCell.style.color = 'green';
            }
            
            // Append the cell to the row
            row.appendChild(debutCell);
        } else {
            console.error('Invalid debut dates:', fighter.debut, secretFighter.debut);
        }

        // Append the row to the table body
        fightersTableBody.appendChild(row);

        // Add the fighter to the selectedFighters array to prevent duplicates
        selectedFighters.push(fighter.id);
    } else {
        displayError('Fighter already selected, please enter a different fighter');
    }
}

// Function to display error message when a fighter is already selected
function displayError(message) {
    const existingErrorMessage = document.getElementById('error-message');
    if (existingErrorMessage) {
        existingErrorMessage.remove();
    }

    const errorMessage = document.createElement('p');
    errorMessage.id = 'error-message';
    errorMessage.textContent = message;
    errorMessage.style.color = 'red';

    document.body.appendChild(errorMessage);

    setTimeout(() => {
        errorMessage.remove();
    }, 3000);
}

function clearResults() {
    const dropdown = document.getElementById('dropdown');
    dropdown.innerHTML = '';
    dropdown.style.display = 'none';
}

let secretFighter = {};
function getSecretFighter() {
    fetch(`/api/data/secretfighter?id=${getRandomInt(173)}`)
    .then(response => response.json())
    .then(data => {
        secretFighter = data;
        console.log('Secret fighter fetched:', secretFighter); // Log the secret fighter
        const secretDiv = document.getElementById('secret-div');
        if (secretDiv) {
            secretDiv.textContent = `${secretFighter.fname} ${secretFighter.lname}`;
        } else {
            console.error('secret-div element not found');
        }
    })
    .catch(error => {
        console.error('Error fetching secret fighter:', error);
    });
}

function getRandomInt(max) {
    return Math.floor(Math.random() * max) + 1;
}
