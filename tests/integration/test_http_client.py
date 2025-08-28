"""HTTP client integration tests."""

import pytest
import requests
import time
from src.neurobloom.client import NeuroBloomClient
from src.neurobloom.models import AnalysisRequest
from .mock_server import MockNeuroBloomServer


class TestNeuroBloomHTTPClient:
    """Test HTTP client with real mock server."""
    
    @pytest.fixture(scope='class')
    def mock_server(self):
        """Start mock server for the test class."""
        server = MockNeuroBloomServer(port=8081)
        server.start()
        
        # Wait for server to be ready
        max_retries = 5
        for i in range(max_retries):
            try:
                response = requests.get('http://127.0.0.1:8081/health', timeout=1)
                if response.status_code == 200:
                    break
            except requests.exceptions.RequestException:
                time.sleep(0.5)
        else:
            pytest.fail("Mock server failed to start")
        
        yield server
        server.stop()
    
    def test_health_check(self, mock_server):
        """Test server health endpoint."""
        client = NeuroBloomClient('http://127.0.0.1:8081')
        
        health_data = client.health_check()
        
        assert health_data['status'] == 'healthy'
        assert health_data['service'] == 'neurobloom-ai'
        assert 'timestamp' in health_data
        
        client.close()
        print("✅ Health check passed")
    
    def test_time_series_analysis(self, mock_server):
        """Test time series analysis with real HTTP calls."""
        client = NeuroBloomClient('http://127.0.0.1:8081')
        
        request_data = AnalysisRequest(
            data=[
                {"timestamp": "2024-01-01", "value": 100},
                {"timestamp": "2024-01-02", "value": 150},
                {"timestamp": "2024-01-03", "value": 120}
            ],
            analysis_type="time_series",
            model="gpt-4"
        )
        
        result = client.analyze_data(request_data)
        
        assert result.status == "completed"
        assert result.confidence_score == 0.87
        assert len(result.insights) == 3
        assert "time_series" in result.insights[0]
        assert result.raw_data["model_used"] == "gpt-4"
        assert result.raw_data["data_points"] == 3
        
        client.close()
        print("✅ Time series analysis test passed")
    
    def test_classification_analysis(self, mock_server):
        """Test classification analysis."""
        client = NeuroBloomClient('http://127.0.0.1:8081')
        
        request_data = AnalysisRequest(
            data=[
                {"feature1": 1.2, "feature2": 3.4, "label": "A"},
                {"feature1": 2.1, "feature2": 1.8, "label": "B"}
            ],
            analysis_type="classification",
            model="gpt-3.5-turbo"
        )
        
        result = client.analyze_data(request_data)
        
        assert result.status == "completed"
        assert result.confidence_score == 0.92
        assert "Classification completed" in result.insights[0]
        assert result.raw_data["model_used"] == "gpt-3.5-turbo"
        
        client.close()
        print("✅ Classification analysis test passed")
    
    def test_invalid_request(self, mock_server):
        """Test error handling with invalid requests."""
        response = requests.post(
            'http://127.0.0.1:8081/api/v1/analyze',
            json={"analysis_type": "time_series"},  # Missing 'data' field
            headers={'Content-Type': 'application/json'}
        )
        
        assert response.status_code == 400
        error_data = response.json()
        assert 'error' in error_data
        assert 'Missing required fields' in error_data['error']
        
        print("✅ Error handling test passed")
