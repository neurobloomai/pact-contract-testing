"""Unit tests for data models."""

import pytest
from src.neurobloom.models import AnalysisRequest, AnalysisResponse


class TestAnalysisRequest:
    """Test AnalysisRequest model."""
    
    def test_basic_request(self):
        """Test basic request creation."""
        data = [{"test": "value"}]
        request = AnalysisRequest(
            data=data,
            analysis_type="time_series",
            model="gpt-4"
        )
        
        assert request.data == data
        assert request.analysis_type == "time_series"
        assert request.model == "gpt-4"
    
    def test_default_model(self):
        """Test default model assignment."""
        request = AnalysisRequest(
            data=[],
            analysis_type="classification"
        )
        
        assert request.model == "gpt-4"
    
    def test_to_dict(self):
        """Test dictionary conversion."""
        request = AnalysisRequest(
            data=[{"key": "value"}],
            analysis_type="test",
            model="gpt-3.5"
        )
        
        expected = {
            "data": [{"key": "value"}],
            "analysis_type": "test", 
            "model": "gpt-3.5"
        }
        
        assert request.to_dict() == expected


class TestAnalysisResponse:
    """Test AnalysisResponse model."""
    
    def test_basic_response(self):
        """Test basic response creation."""
        response = AnalysisResponse(
            id="test_123",
            status="completed",
            insights=["insight1", "insight2"],
            confidence_score=0.85,
            raw_data={"key": "value"}
        )
        
        assert response.id == "test_123"
        assert response.status == "completed"
        assert len(response.insights) == 2
        assert response.confidence_score == 0.85
    
    def test_from_dict(self):
        """Test creation from dictionary."""
        data = {
            "id": "test_456",
            "status": "completed",
            "insights": ["test insight"],
            "confidence_score": 0.92,
            "raw_data": {"model": "gpt-4"}
        }
        
        response = AnalysisResponse.from_dict(data)
        
        assert response.id == "test_456"
        assert response.status == "completed"
        assert response.insights == ["test insight"]
        assert response.confidence_score == 0.92
        assert response.raw_data == {"model": "gpt-4"}
