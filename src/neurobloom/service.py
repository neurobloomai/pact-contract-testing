"""AI analysis service implementation."""

import json
import time
from typing import Dict, List, Optional
import openai


class NeuroBloomService:
    """Service for processing AI analysis using OpenAI."""
    
    def __init__(self, openai_api_key: str, default_model: str = "gpt-4"):
        """Initialize service with OpenAI API key."""
        self.openai_client = openai.OpenAI(api_key=openai_api_key)
        self.default_model = default_model
    
    def process_analysis(
        self, 
        data: List[Dict], 
        analysis_type: str, 
        model: Optional[str] = None
    ) -> Dict:
        """Process data analysis using OpenAI."""
        model_to_use = model or self.default_model
        start_time = time.time()
        
        try:
            # Create analysis prompt based on type
            prompt = self._create_analysis_prompt(data, analysis_type)
            
            # Call OpenAI API
            insights = self._call_openai(prompt, model_to_use)
            
            # Calculate processing time
            processing_time = round(time.time() - start_time, 2)
            
            # Generate response
            return {
                "id": f"analysis_{int(time.time() * 1000)}",
                "status": "completed",
                "insights": insights,
                "confidence_score": self._calculate_confidence(insights, data),
                "raw_data": {
                    "model_used": model_to_use,
                    "processing_time": processing_time,
                    "data_points": len(data),
                    "analysis_type": analysis_type
                }
            }
            
        except Exception as e:
            return {
                "id": f"analysis_{int(time.time() * 1000)}",
                "status": "failed",
                "insights": [],
                "confidence_score": 0.0,
                "raw_data": {
                    "error": str(e),
                    "model_used": model_to_use,
                    "processing_time": round(time.time() - start_time, 2)
                }
            }
    
    def _create_analysis_prompt(self, data: List[Dict], analysis_type: str) -> str:
        """Create analysis prompt based on data and type."""
        data_summary = json.dumps(data[:5], indent=2)  # Limit for prompt size
        
        prompts = {
            "time_series": f"Analyze this time series data for trends and patterns:\n{data_summary}",
            "classification": f"Classify and analyze patterns in this data:\n{data_summary}",
            "sales_forecasting": f"Analyze sales data and provide forecasting insights:\n{data_summary}",
            "default": f"Provide insights and analysis for this {analysis_type} data:\n{data_summary}"
        }
        
        return prompts.get(analysis_type, prompts["default"])
    
    def _call_openai(self, prompt: str, model: str) -> List[str]:
        """Call OpenAI API and parse insights."""
        try:
            response = self.openai_client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a data analysis expert. Provide 3-5 key insights in bullet points."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.3
            )
            
            content = response.choices[0].message.content
            # Parse bullet points into list
            insights = [
                line.strip().lstrip('•-*').strip() 
                for line in content.split('\n') 
                if line.strip() and not line.strip().startswith(('Here', 'Based', 'Analysis'))
            ]
            
            return insights[:5]  # Limit to 5 insights
            
        except Exception as e:
            # Fallback to mock insights if OpenAI fails
            return [f"Analysis completed for {len(data)} data points", 
                   f"Error in AI processing: {str(e)}"]
    
    def _calculate_confidence(self, insights: List[str], data: List[Dict]) -> float:
        """Calculate confidence score based on insights and data quality."""
        base_confidence = 0.7
        
        # Adjust based on data size
        data_size_factor = min(len(data) / 100, 0.2)  # Max 0.2 boost
        
        # Adjust based on insights quality
        insights_factor = min(len(insights) * 0.05, 0.1)  # Max 0.1 boost
        
        return min(base_confidence + data_size_factor + insights_factor, 0.95)
