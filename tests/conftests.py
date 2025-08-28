"""Pytest configuration and shared fixtures."""

import pytest
import os
import sys

# Add src to Python path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

@pytest.fixture
def sample_time_series_data():
    """Sample time series data for testing."""
    return [
        {"timestamp": "2024-01-01", "value": 100, "category": "A"},
        {"timestamp": "2024-01-02", "value": 150, "category": "A"}, 
        {"timestamp": "2024-01-03", "value": 120, "category": "B"},
        {"timestamp": "2024-01-04", "value": 180, "category": "B"}
    ]

@pytest.fixture  
def sample_classification_data():
    """Sample classification data for testing."""
    return [
        {"feature1": 1.2, "feature2": 3.4, "label": "class_A"},
        {"feature1": 2.1, "feature2": 1.8, "label": "class_B"},
        {"feature1": 1.8, "feature2": 2.9, "label": "class_A"}
    ]
