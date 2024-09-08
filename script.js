document.getElementById('summarizer-form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const text = document.getElementById('text-input').value;

    try {
        const response = await fetch('http://127.0.0.1:8000/summarize/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text_string: text })
        });

        if (response.ok) {
            const data = await response.json();
            document.getElementById('summary-text').textContent = `Summary: ${data.summary}`;
        } else {
            throw new Error('Network response was not ok');
        }


    } catch (error) {
        console.error('Error:', error);
        document.getElementById('summary-text').textContent = 'An error occurred while summarizing the text.';
    }
});