"""Data models for Neurobloom AI analysis."""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class AnalysisRequest:
    """Request model for AI analysis."""
    data: List[Dict]
    analysis_type: str
    model: Optional[str] = "gpt-4"
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "data": self.data,
            "analysis_type": self.analysis_type,
            "model": self.model
        }


@dataclass
class AnalysisResponse:
    """Response model for AI analysis results."""
    id: str
    status: str
    insights: List[str]
    confidence_score: float
    raw_data: Dict
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'AnalysisResponse':
        """Create from dictionary (JSON deserialization)."""
        return cls(
            id=data["id"],
            status=data["status"],
            insights=data["insights"],
            confidence_score=data["confidence_score"],
            raw_data=data.get("raw_data", {})
        )
