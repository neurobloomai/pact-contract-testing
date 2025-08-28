"""HTTP client for Neurobloom AI service."""

import requests
from typing import Dict
from .models import AnalysisRequest, AnalysisResponse


class NeuroBloomClient:
    """HTTP client for interacting with Neurobloom AI service."""
    
    def __init__(self, base_url: str, timeout: int = 30):
        """Initialize client with base URL and timeout."""
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': 'neurobloom-client/1.0'
        })
    
    def analyze_data(self, request: AnalysisRequest) -> AnalysisResponse:
        """Send data for AI analysis."""
        url = f"{self.base_url}/api/v1/analyze"
        
        try:
            response = self.session.post(
                url,
                json=request.to_dict(),
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                return AnalysisResponse.from_dict(response.json())
            else:
                raise Exception(
                    f"Analysis failed: {response.status_code} - {response.text}"
                )
                
        except requests.exceptions.RequestException as e:
            raise Exception(f"Request failed: {str(e)}")
    
    def health_check(self) -> Dict:
        """Check service health."""
        url = f"{self.base_url}/health"
        
        try:
            response = self.session.get(url, timeout=5)
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Health check failed: {str(e)}")
    
    def close(self):
        """Close the session."""
        self.session.close()
