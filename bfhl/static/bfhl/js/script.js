function submitJson() {
    const jsonInput = document.getElementById('jsonInput').value;
    let errorMessage = document.getElementById('errorMessage');
    errorMessage.textContent = '';
    document.getElementById('filteredResponse').textContent = '';
    document.getElementById('responseSection').style.display = 'none';

    try {
        const parsedJson = JSON.parse(jsonInput);
        
        fetch('/bfhl', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(parsedJson)
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('responseSection').style.display = 'block';
            window.apiResponse = data; // Store response globally
            filterResponse();
        })
        .catch(error => {
            console.error('Error:', error);
            errorMessage.textContent = 'An error occurred while processing your request.';
        });
    } catch (error) {
        errorMessage.textContent = 'Invalid JSON format';
    }
}

function filterResponse() {
    const selectedOptions = Array.from(document.getElementById('options').selectedOptions).map(option => option.value);
    const filteredData = {};

    selectedOptions.forEach(option => {
        if (window.apiResponse[option]) {
            filteredData[option] = window.apiResponse[option];
        }
    });

    document.getElementById('filteredResponse').textContent = JSON.stringify(filteredData, null, 2);
}
