from flask import Blueprint, render_template, request, jsonify
from app.mcp_connector import query_mcp

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('index.html')

@routes.route('/mcp-query', methods=['POST'])
def mcp_query():
    try:
        data = request.json
        result = query_mcp("query-endpoint", data)
        return jsonify(result)
    except Exception as e:
        return jsonify({
            "error": str(e),
            "type": type(e).__name__
        }), 500
