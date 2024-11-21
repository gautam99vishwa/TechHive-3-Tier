document.getElementById('userForm').addEventListener('submit', async function (e) {
    e.preventDefault();
    const name = document.getElementById('name').value;

    const response = await fetch('http://3.110.28.2:5000/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: name })
    });

    const data = await response.json();
    document.getElementById('responseMessage').innerText = data.message;
});

