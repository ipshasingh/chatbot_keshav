let lastVerse = "";

function askKeshav() {
    const question = document.getElementById('question').value;

    fetch('https://keshavai.onrender.com/ask', {
        method: 'POST',
        body: JSON.stringify({ question }),
        headers: { 'Content-Type': 'application/json' }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerText = data.response;

        const lines = data.response.split("\n");
        lastVerse = lines[0];

        document.getElementById('reciteBtn').style.display = 'inline';
    });
}

function reciteVerse() {
    fetch('https://keshavai.onrender.com/recite', {
        method: 'POST',
        body: JSON.stringify({ verse: lastVerse }),
        headers: { 'Content-Type': 'application/json' }
    })
    .then(response => response.blob())
    .then(blob => {
        const audioUrl = URL.createObjectURL(blob);
        const player = document.getElementById('audioPlayer');
        player.src = audioUrl;
        player.style.display = 'block';
        player.play();
    });
}