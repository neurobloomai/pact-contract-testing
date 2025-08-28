"""Mock server for testing HTTP client integration."""

from flask import Flask, request, jsonify
import threading
import time
import json
from typing import Optional


class MockNeuroBloomServer:
    """Mock server that mimics Neurobloom AI service."""
    
    def __init__(self, port: int = 8080):
        """Initialize mock server."""
        self.port = port
        self.app = Flask(__name__)
        self.server_thread: Optional[threading.Thread] = None
        self.setup_routes()
        
    def setup_routes(self):
        """Set up Flask routes."""
        
        @self.app.route('/api/v1/analyze', methods=['POST'])
        def analyze():
            data = request.get_json()
            
            # Validate request
            if not data or 'data' not in data or 'analysis_type' not in data:
                return jsonify({'error': 'Missing required fields'}), 400
            
            # Simulate processing time
            time.sleep(0.1)
            
            # Mock different responses based on analysis type
            analysis_type = data['analysis_type']
            model = data.get('model', 'gpt-4')
            data_points = len(data['data'])
            
            # Response based on analysis type
            response_map = {
                'time_series': {
                    'insights': [
                        "Key pattern identified in time_series data",
                        "Strong correlation detected between variables",
                        "Seasonal trend observed with 95% confidence"
                    ],
                    'confidence': 0.87
                },
                'classification': {
                    'insights': [
                        "Classification completed with high accuracy",
                        "3 distinct clusters identified",
                        "Feature importance analysis completed"
                    ],
                    'confidence': 0.92
                },
                'sales_forecasting': {
                    'insights': [
                        "Sales trend shows 15% growth potential",
                        "Regional performance varies significantly",
                        "Recommend focus on north region"
                    ],
                    'confidence': 0.78
                }
            }
            
            response_data = response_map.get(analysis_type, {
                'insights': ["Generic analysis completed"],
                'confidence': 0.65
            })
            
            response = {
                "id": f"analysis_{int(time.time() * 1000)}",
                "status": "completed",
                "insights": response_data['insights'],
                "confidence_score": response_data['confidence'],
                "raw_data": {
                    "model_used": model,
                    "processing_time": round(time.time() % 10, 2),
                    "data_points": data_points,
                    "analysis_type": analysis_type
                }
            }
            
            return jsonify(response), 200
        
        @self.app.route('/health', methods=['GET'])
        def health():
            return jsonify({
                'status': 'healthy', 
                'service': 'neurobloom-ai',
                'timestamp': int(time.time())
            }), 200
    
    def start(self):
        """Start the mock server in a separate thread."""
        if self.server_thread is None or not self.server_thread.is_alive():
            self.server_thread = threading.Thread(
                target=lambda: self.app.run(
                    port=self.port, 
                    debug=False, 
                    use_reloader=False,
                    host='127.0.0.1'
                )
            )
            self.server_thread.daemon = True
            self.server_thread.start()
            time.sleep(1)  # Give server time to start
            print(f"🚀 Mock server started on http://127.0.0.1:{self.port}")
    
    def stop(self):
        """Stop the mock server."""
        print("🛑 Mock server stopped")
