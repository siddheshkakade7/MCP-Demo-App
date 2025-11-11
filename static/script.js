function queryMCP() {
    const resultDiv = document.getElementById('result');
    resultDiv.textContent = 'Loading...';
    
    fetch('/mcp-query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: 'Hello MCP' })
    })
    .then(res => res.json())
    .then(data => {
        resultDiv.textContent = JSON.stringify(data, null, 2);
        console.log('MCP Response:', data);
    })
    .catch(err => {
        resultDiv.textContent = 'Error: ' + err.message;
        console.error('MCP Error:', err);
    });
}
