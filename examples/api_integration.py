#!/usr/bin/env python3
"""
API Integration Example
=======================

Demonstrates patterns for integrating external APIs with OpenClaw:
- REST API calls
- Data transformation
- Error handling
- Rate limiting

Note: This example uses mock data. In production, replace with actual API calls.

Usage:
    python3 examples/api_integration.py
"""

import json
import time
from datetime import datetime
from pathlib import Path


class APIIntegrationDemo:
    """Demonstrates API integration patterns."""
    
    def __init__(self):
        self.output_dir = Path("api_output")
        self.output_dir.mkdir(exist_ok=True)
    
    def mock_weather_api(self, location):
        """Simulate a weather API call."""
        # Mock data - replace with actual API in production
        return {
            "location": location,
            "temperature": 22,
            "conditions": "Partly cloudy",
            "humidity": 65,
            "wind_speed": 12,
            "timestamp": datetime.now().isoformat()
        }
    
    def mock_github_api(self, repo):
        """Simulate a GitHub API call."""
        # Mock data - replace with actual API in production
        return {
            "repo": repo,
            "stars": 1250,
            "forks": 180,
            "open_issues": 45,
            "last_updated": datetime.now().isoformat()
        }
    
    def mock_news_api(self, query):
        """Simulate a news API call."""
        # Mock data - replace with actual API in production
        return {
            "query": query,
            "results": [
                {
                    "title": "AI Advances Continue",
                    "source": "Tech News",
                    "published": "2026-03-14"
                },
                {
                    "title": "OpenClaw Gains Popularity",
                    "source": "Developer Weekly",
                    "published": "2026-03-13"
                }
            ]
        }
    
    def demo_weather_integration(self):
        """Demonstrate weather API integration."""
        print("\n🌤️  Weather API Integration")
        
        locations = ["San Francisco", "New York", "London"]
        weather_data = []
        
        for location in locations:
            print(f"   Fetching weather for {location}...")
            data = self.mock_weather_api(location)
            weather_data.append(data)
            time.sleep(0.2)  # Simulate rate limiting
        
        # Save results
        output_file = self.output_dir / "weather_data.json"
        output_file.write_text(json.dumps(weather_data, indent=2))
        
        print(f"   ✓ Fetched weather for {len(locations)} locations")
        print(f"   ✓ Saved to: {output_file}")
        
        return weather_data
    
    def demo_github_integration(self):
        """Demonstrate GitHub API integration."""
        print("\n🐙 GitHub API Integration")
        
        repos = [
            "openclaw/openclaw",
            "openai/swarm",
            "langchain-ai/langchain"
        ]
        
        repo_stats = []
        
        for repo in repos:
            print(f"   Fetching stats for {repo}...")
            data = self.mock_github_api(repo)
            repo_stats.append(data)
            time.sleep(0.2)  # Simulate rate limiting
        
        # Save results
        output_file = self.output_dir / "github_stats.json"
        output_file.write_text(json.dumps(repo_stats, indent=2))
        
        print(f"   ✓ Fetched stats for {len(repos)} repositories")
        print(f"   ✓ Saved to: {output_file}")
        
        return repo_stats
    
    def demo_news_aggregation(self):
        """Demonstrate news API aggregation."""
        print("\n📰 News API Aggregation")
        
        queries = ["artificial intelligence", "automation", "OpenClaw"]
        all_news = []
        
        for query in queries:
            print(f"   Searching news for: {query}")
            data = self.mock_news_api(query)
            all_news.append(data)
            time.sleep(0.2)  # Simulate rate limiting
        
        # Save aggregated results
        output_file = self.output_dir / "news_aggregation.json"
        output_file.write_text(json.dumps(all_news, indent=2))
        
        total_articles = sum(len(n["results"]) for n in all_news)
        print(f"   ✓ Aggregated {total_articles} articles")
        print(f"   ✓ Saved to: {output_file}")
        
        return all_news
    
    def demo_data_transformation(self):
        """Demonstrate transforming API data."""
        print("\n🔄 Data Transformation")
        
        # Fetch data
        weather = self.mock_weather_api("Tokyo")
        github = self.mock_github_api("awesome/project")
        
        # Transform into a unified format
        transformed = {
            "timestamp": datetime.now().isoformat(),
            "sources": {
                "weather": {
                    "location": weather["location"],
                    "temp_celsius": weather["temperature"],
                    "conditions": weather["conditions"]
                },
                "repository": {
                    "name": github["repo"],
                    "popularity_score": github["stars"] + github["forks"],
                    "activity_status": "active" if github["open_issues"] > 0 else "inactive"
                }
            }
        }
        
        output_file = self.output_dir / "transformed_data.json"
        output_file.write_text(json.dumps(transformed, indent=2))
        
        print(f"   ✓ Transformed data from multiple sources")
        print(f"   ✓ Saved to: {output_file}")
        
        return transformed
    
    def demo_error_handling(self):
        """Demonstrate error handling patterns."""
        print("\n⚠️  Error Handling")
        
        def safe_api_call(api_func, *args, max_retries=3):
            """Wrapper for safe API calls with retries."""
            for attempt in range(max_retries):
                try:
                    return {"success": True, "data": api_func(*args)}
                except Exception as e:
                    if attempt == max_retries - 1:
                        return {"success": False, "error": str(e)}
                    time.sleep(0.5)  # Wait before retry
        
        # Simulate API calls with error handling
        results = {
            "weather": safe_api_call(self.mock_weather_api, "Paris"),
            "github": safe_api_call(self.mock_github_api, "test/repo")
        }
        
        output_file = self.output_dir / "api_results_with_errors.json"
        output_file.write_text(json.dumps(results, indent=2))
        
        successes = sum(1 for r in results.values() if r["success"])
        print(f"   ✓ Handled {len(results)} API calls")
        print(f"   ✓ Success rate: {successes}/{len(results)}")
        
        return results
    
    def run_all_demos(self):
        """Execute all API integration demonstrations."""
        print("🌐 API Integration Demonstration Suite")
        print("=" * 60)
        
        demos = [
            self.demo_weather_integration,
            self.demo_github_integration,
            self.demo_news_aggregation,
            self.demo_data_transformation,
            self.demo_error_handling
        ]
        
        for demo in demos:
            try:
                demo()
            except Exception as e:
                print(f"   ❌ Demo failed: {e}")
        
        print("\n" + "=" * 60)
        print("✅ API Integration Suite Complete")
        print(f"   Output directory: {self.output_dir}")
        print("\nNote: This demo uses mock data.")
        print("In production, replace mock functions with actual API calls.")


def main():
    """Run the API integration demonstration."""
    demo = APIIntegrationDemo()
    demo.run_all_demos()


if __name__ == "__main__":
    main()
