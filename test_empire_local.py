import requests
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("EMPIRE_TEST")

def run_test():
    """
    Simulate a lead submission to the local LOA Brain API
    """
    url = "https://famous-bobcats-press.loca.lt/api/submit-lead"
    
    payload = {
        "name": "Imperial Test Client",
        "email": "success@9lmnts.studio",
        "plan": "premium",
        "projectType": "AI Business Empire",
        "timeline": "Urgent (24h)",
        "description": "Testing the full Nine Pillars orchestration loop. Local -> Notion -> Slack.",
        "company": "Empire Builders Inc",
        "website": "https://9lmntsstudio.com"
    }
    
    logger.info(f"🚀 Sending test lead to {url}...")
    
    try:
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            logger.info("✅ SUCCESS: API accepted the lead!")
            print("\n--- RESULTS ---")
            print(json.dumps(response.json(), indent=2))
            print("\n----------------")
            print("NEXT STEPS:")
            print("1. Check your Notion database (Nine Pillars AI Leads).")
            print("2. Check your Slack channel for the notification.")
        else:
            logger.error(f"❌ FAILED: API returned status {response.status_code}")
            print(response.text)
            
    except Exception as e:
        logger.error(f"❌ ERROR: Could not connect to API. Is 'loa_api.py' running?")
        print(f"Details: {e}")

if __name__ == "__main__":
    run_test()
