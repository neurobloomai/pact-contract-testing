"""Demo script showing Neurobloom client usage."""

import sys
import os
import time

# Add src to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from src.neurobloom.client import NeuroBloomClient
from src.neurobloom.models import AnalysisRequest
from tests.integration.mock_server import MockNeuroBloomServer


def demo_neurobloom_workflow():
    """Demonstrate the complete workflow."""
    print("🧠 Neurobloom AI Analysis Demo")
    print("=" * 40)
    
    # Start mock server
    server = MockNeuroBloomServer(port=8082)
    server.start()
    
    try:
        # Wait for server readiness
        time.sleep(1)
        
        # Create client
        client = NeuroBloomClient('http://127.0.0.1:8082')
        
        # Test health check
        print("🏥 Health Check...")
        health = client.health_check()
        print(f"   Status: {health['status']}")
        
        # Sample data
        sample_data = [
            {"timestamp": "2024-01-01", "sales": 1200, "region": "north"},
            {"timestamp": "2024-01-02", "sales": 1350, "region": "north"},
            {"timestamp": "2024-01-03", "sales": 1180, "region": "south"},
            {"timestamp": "2024-01-04", "sales": 1400, "region": "south"}
        ]
        
        # Test different analysis types
        analysis_types = ["time_series", "classification", "sales_forecasting"]
        
        for analysis_type in analysis_types:
            print(f"\n📊 Testing {analysis_type} analysis...")
            
            request = AnalysisRequest(
                data=sample_data,
                analysis_type=analysis_type,
                model="gpt-4"
            )
            
            result = client.analyze_data(request)
            
            print(f"   ID: {result.id}")
            print(f"   Status: {result.status}")
            print(f"   Confidence: {result.confidence_score}")
            print(f"   Insights ({len(result.insights)}):")
            for i, insight in enumerate(result.insights, 1):
                print(f"     {i}. {insight}")
        
        client.close()
        
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        server.stop()
    
    print("\n✅ Demo completed!")


if __name__ == "__main__":
    demo_neurobloom_workflow()
