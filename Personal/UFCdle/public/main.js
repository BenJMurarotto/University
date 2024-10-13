let debounceTimeout;
let selectedFighters = []; // Declare globally to keep track of selected fighters

document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('search-input');
    const dropdown = document.getElementById('dropdown'); // Declare dropdown

    searchInput.addEventListener('input', () => {
        clearTimeout(debounceTimeout);
        debounceTimeout = setTimeout(() => {
            searchFighter();
        }, 150);
    });

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

    // Check if the input is at least 2 characters long
    if (searchQuery.length < 2) {
        clearResults();
        return;
    }

    // Fetch search results
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
                        // Show the table after the first valid selection
                        const fightersTable = document.getElementById('fighters-table');
                        if (fightersTable.style.display === 'none') {
                            fightersTable.style.display = 'table'; // Make the table visible
                        }

                        // Add the selected fighter to the table
                        appendSelectedFighter(fighter);
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

// Function to append selected fighter to the table
function appendSelectedFighter(fighter) {
    const fightersTableBody = document.getElementById('fighters-body');
    
    // Check if the fighter is already in the selected list
    if (!selectedFighters.includes(fighter.fname)) {
        if (fightersTableBody.rows.length >= 6) {
            // If there are already 6 rows, remove the oldest one (first row)
            fightersTableBody.deleteRow(0);
        }

        // Create a new row
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${fighter.fname} ${fighter.lname}</td>
            <td>${fighter.division}</td>
            <td>${fighter.rank}</td>
            <td>${fighter.style}</td>
            <td>${fighter.debut}</td>
        `;
        fightersTableBody.appendChild(row);

        // Add the fighter to the selectedFighters array to prevent duplicates
        selectedFighters.push(fighter.fname);
    } else {
        // Create an error message element
        const errorMessage = document.createElement('p');
        errorMessage.textContent = 'Fighter already selected, please enter a different fighter';
        errorMessage.style.color = 'red'; // Optional: Style the error message

        // Optionally, remove the error message after a few seconds
        setTimeout(() => {
            errorMessage.remove();
        }, 3000); // Remove after 3 seconds
    }
}

// Call function to clear search results
function clearResults() {
    const dropdown = document.getElementById('dropdown');
    dropdown.innerHTML = ''; // Clear any previous search results
    dropdown.style.display = 'none'; // Hide the dropdown
}
