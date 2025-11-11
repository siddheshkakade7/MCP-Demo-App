import requests
import json

def query_mcp(endpoint, payload):
    try:
        url = f"https://api.modelcontextprotocol.io/{endpoint}"
        response = requests.post(url, json=payload, timeout=5)
        
        # Check if response is JSON
        if 'application/json' in response.headers.get('Content-Type', ''):
            return response.json()
        else:
            # Return error if not JSON
            return {
                "error": "Invalid response from MCP server",
                "status": response.status_code
            }
    except requests.exceptions.RequestException as e:
        # Handle network errors - return clean mock data for demo
        return {
            "status": "success",
            "source": "mock_data",
            "message": "Demo MCP Response (API unavailable - using mock data)",
            "query": payload.get("message", "Hello MCP"),
            "response": {
                "result": "This is a mock response from the MCP Demo App",
                "timestamp": "2025-11-11T00:00:00Z",
                "demo": True
            }
        }
