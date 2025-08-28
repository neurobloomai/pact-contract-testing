#!/bin/bash
# Contract test automation script

echo "🧪 Running Neurobloom Contract Tests"
echo "===================================="

# Set up environment
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"

# Run unit tests
echo "📋 Running unit tests..."
pytest tests/unit/ -v

# Run integration tests  
echo "📋 Running integration tests..."
pytest tests/integration/ -v

# Run contract tests (when implemented)
echo "📋 Running contract tests..."
# pytest tests/contract/ -v

# Generate coverage report
echo "📊 Generating coverage report..."
pytest --cov=src --cov-report=html --cov-report=term

echo "✅ All tests completed!"
echo "📈 Coverage report: htmlcov/index.html"
