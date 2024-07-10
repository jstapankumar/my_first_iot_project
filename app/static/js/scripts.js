document.getElementById('create-ae').addEventListener('click', function() {
    fetch('/create_ae', { method: 'POST' })
        .then(response => {
            return response.json().then(data => {
                if (!response.ok) {
                    throw new Error(data.error || 'Failed to create AE');
                }
                return data;
            });
        })
        .then(data => {
            showResponse(data.message || JSON.stringify(data, null, 2));
        })
        .catch(error => showError(error.message));
});

document.getElementById('retrieve-ae').addEventListener('click', function() {
    fetch('/retrieve_ae')
        .then(response => {
            return response.json().then(data => {
                if (!response.ok) {
                    throw new Error(data.error || 'Failed to retrieve AE');
                }
                return data;
            });
        })
        .then(data => {
            showResponse(data.message || JSON.stringify(data, null, 2));
        })
        .catch(error => showError(error.message));
});

document.getElementById('update-ae').addEventListener('click', function() {
    fetch('/update_ae', { method: 'PUT' })
        .then(response => {
            return response.json().then(data => {
                if (!response.ok) {
                    throw new Error(data.error || 'Failed to update AE');
                }
                return data;
            });
        })
        .then(data => {
            showResponse(data.message || JSON.stringify(data, null, 2));
        })
        .catch(error => showError(error.message));
});

document.getElementById('delete-ae').addEventListener('click', function() {
    fetch('/delete_ae', { method: 'DELETE' })
        .then(response => {
            return response.json().then(data => {
                if (!response.ok) {
                    throw new Error(data.error || 'Failed to delete AE');
                }
                return data;
            });
        })
        .then(data => {
            showResponse(data.message || JSON.stringify(data, null, 2));
        })
        .catch(error => showError(error.message));
});

function showResponse(data) {
    const responseDiv = document.getElementById('response');
    responseDiv.innerText = data;
    responseDiv.style.color = 'black';
    responseDiv.style.display = 'block';
}

function showError(error) {
    console.error('Error:', error);
    const responseDiv = document.getElementById('response');
    responseDiv.innerText = `Error: ${error}`;
    responseDiv.style.color = 'red';
    responseDiv.style.display = 'block';
}

