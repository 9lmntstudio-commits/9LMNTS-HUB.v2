"""
9LMNTS STUDIO - Notion Integration
Connect Loa Brain AI Empire with Notion for knowledge management and workflow automation
"""

import asyncio
import logging
import json
from datetime import datetime
from typing import Dict, Any, List, Optional
import requests
from loa_brain import LOABrain

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("NOTION_INTEGRATION")

class NotionIntegration:
    def __init__(self):
        self.api_key = "your_notion_integration_token_here"  # Update with actual token
        self.database_id = "your_notion_database_id_here"  # Update with actual database ID
        self.base_url = "https://api.notion.com/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }
        self.loa_brain = LOABrain()
        
    async def create_lead_database(self) -> Dict:
        """Create Notion database for lead management"""
        
        database_schema = {
            "parent": {"type": "page_id", "page_id": self.database_id},
            "title": [
                {
                    "type": "text",
                    "text": {"content": "🎯 Nine Pillars AI Leads"}
                }
            ],
            "properties": {
                "Lead Name": {"title": {}},
                "Company": {"rich_text": {}},
                "Business Type": {"select": {"options": [
                    {"name": "E-commerce", "color": "blue"},
                    {"name": "SaaS", "color": "green"},
                    {"name": "Digital Agency", "color": "orange"},
                    {"name": "Service Business", "color": "purple"},
                    {"name": "Startup", "color": "red"},
                    {"name": "Traditional Business", "color": "yellow"}
                ]}},
                "Budget": {"number": {"format": "dollar"}},
                "Timeline": {"select": {"options": [
                    {"name": "Urgent (24h)", "color": "red"},
                    {"name": "ASAP (48h)", "color": "orange"},
                    {"name": "1 Week", "color": "yellow"},
                    {"name": "2-4 Weeks", "color": "blue"},
                    {"name": "1+ Month", "color": "gray"}
                ]}},
                "Qualification Score": {"number": {"format": "percent"}},
                "Status": {"select": {"options": [
                    {"name": "🔥 HOT LEAD", "color": "red"},
                    {"name": "✅ WARM LEAD", "color": "orange"},
                    {"name": "🌡️ NURTURE", "color": "yellow"},
                    {"name": "❄️ COLD", "color": "blue"},
                    {"name": "🎯 CLOSED", "color": "green"},
                    {"name": "❌ LOST", "color": "red"}
                ]}},
                "Service Package": {"select": {"options": [
                    {"name": "AI Brand Transformation", "color": "blue"},
                    {"name": "Digital Dominance Starter", "color": "green"},
                    {"name": "AI Business Empire", "color": "purple"},
                    {"name": "Custom AI Solution", "color": "orange"}
                ]}},
                "Expected Revenue": {"number": {"format": "dollar"}},
                "Contact Info": {"rich_text": {}},
                "Requirements": {"rich_text": {}},
                "AI Analysis": {"rich_text": {}},
                "Next Steps": {"multi_select": {"options": [
                    {"name": "Send Proposal", "color": "blue"},
                    {"name": "Schedule Call", "color": "green"},
                    {"name": "Follow Up", "color": "orange"},
                    {"name": "Qualify Further", "color": "yellow"},
                    {"name": "Close Deal", "color": "red"}
                ]}},
                "Created Date": {"date": {}},
                "Last Contact": {"date": {}},
                "Assigned To": {"select": {"options": [
                    {"name": "Loa Brain AI", "color": "blue"},
                    {"name": "Sales Team", "color": "green"},
                    {"name": "Automation", "color": "purple"}
                ]}}
            }
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/databases",
                json=database_schema,
                headers=self.headers
            )
            
            if response.status_code == 200:
                database = response.json()
                logger.info(f"✅ Created Notion database: {database['id']}")
                return {
                    "status": "database_created",
                    "database_id": database["id"],
                    "database_url": database["url"]
                }
            else:
                logger.error(f"❌ Failed to create database: {response.text}")
                return {"status": "error", "error": response.text}
                
        except Exception as e:
            logger.error(f"❌ Error creating database: {e}")
            return {"status": "error", "error": str(e)}
    
    async def add_lead_to_notion(self, lead_info: Dict) -> Dict:
        """Add qualified lead to Notion database"""
        
        # Qualify lead using Loa Brain
        qualification = await self.loa_brain.qualify_lead_instantly(lead_info)
        
        # Create page content
        page_data = {
            "parent": {"database_id": self.database_id},
            "properties": {
                "Lead Name": {"title": [{"text": {"content": lead_info.get("name", "Unknown Lead")}}]},
                "Company": {"rich_text": [{"text": {"content": lead_info.get("company", "")}}]},
                "Business Type": {"select": {"name": lead_info.get("business_type", "Service Business")}},
                "Budget": {"number": lead_info.get("budget", 0)},
                "Timeline": {"select": {"name": lead_info.get("timeline", "1 Week")}},
                "Qualification Score": {"number": qualification["qualification_score"] / 100},
                "Status": {"select": {"name": qualification["level"]}},
                "Expected Revenue": {"number": qualification["estimated_value"]},
                "Contact Info": {"rich_text": [{"text": {"content": json.dumps(lead_info.get("contact_info", {}))}}]},
                "Requirements": {"rich_text": [{"text": {"content": lead_info.get("requirements", "")}}]},
                "AI Analysis": {"rich_text": [{"text": {"content": f"Qualification Score: {qualification['qualification_score']}%\n\nReasons:\n" + "\n".join(qualification["reasons"])}}]},
                "Next Steps": {"multi_select": [{"name": qualification["recommended_action"].split()[0]}]},
                "Created Date": {"date": {"start": datetime.now().isoformat()}},
                "Assigned To": {"select": {"name": "Loa Brain AI"}}
            }
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/pages",
                json=page_data,
                headers=self.headers
            )
            
            if response.status_code == 200:
                page = response.json()
                logger.info(f"✅ Added lead to Notion: {lead_info.get('name')}")
                
                # Trigger CrewAI workflow if hot lead
                if qualification["qualification_score"] >= 80:
                    await self._trigger_crewai_workflow(lead_info, qualification)
                
                return {
                    "status": "lead_added",
                    "page_id": page["id"],
                    "page_url": page["url"],
                    "qualification": qualification
                }
            else:
                logger.error(f"❌ Failed to add lead: {response.text}")
                return {"status": "error", "error": response.text}
                
        except Exception as e:
            logger.error(f"❌ Error adding lead: {e}")
            return {"status": "error", "error": str(e)}
    
    async def _trigger_crewai_workflow(self, lead_info: Dict, qualification: Dict):
        """Trigger CrewAI workflow for hot leads"""
        
        workflow_data = {
            "lead_info": lead_info,
            "qualification": qualification,
            "action": "hot_lead_detected",
            "priority": "high",
            "timestamp": datetime.now().isoformat()
        }
        
        # Send to CrewAI via webhook
        crewai_webhook = "https://your-crewai-webhook-url"
        
        try:
            response = requests.post(
                crewai_webhook,
                json=workflow_data,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                logger.info(f"🚀 Triggered CrewAI workflow for hot lead: {lead_info.get('name')}")
            else:
                logger.error(f"❌ Failed to trigger CrewAI: {response.text}")
                
        except Exception as e:
            logger.error(f"❌ Error triggering CrewAI: {e}")
    
    async def create_proposal_page(self, proposal_data: Dict) -> Dict:
        """Create proposal page in Notion"""
        
        page_data = {
            "parent": {"database_id": self.database_id},
            "properties": {
                "Lead Name": {"title": [{"text": {"content": f"📋 Proposal: {proposal_data.get('client_name', 'Unknown')}"}}]},
                "Company": {"rich_text": [{"text": {"content": proposal_data.get("company", "")}}]},
                "Service Package": {"select": {"name": proposal_data.get("service_package", "Custom AI Solution")}},
                "Status": {"select": {"name": "📋 PROPOSAL SENT"}},
                "Expected Revenue": {"number": proposal_data.get("price", 0)},
                "Next Steps": {"multi_select": [{"name": "Send Invoice"}, {"name": "Get Approval"}]},
                "Created Date": {"date": {"start": datetime.now().isoformat()}}
            }
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/pages",
                json=page_data,
                headers=self.headers
            )
            
            if response.status_code == 200:
                page = response.json()
                logger.info(f"✅ Created proposal page: {proposal_data.get('client_name')}")
                return {
                    "status": "proposal_created",
                    "page_id": page["id"],
                    "page_url": page["url"]
                }
            else:
                logger.error(f"❌ Failed to create proposal: {response.text}")
                return {"status": "error", "error": response.text}
                
        except Exception as e:
            logger.error(f"❌ Error creating proposal: {e}")
            return {"status": "error", "error": str(e)}
    
    async def update_lead_status(self, page_id: str, status: str, notes: str = "") -> Dict:
        """Update lead status in Notion"""
        
        update_data = {
            "properties": {
                "Status": {"select": {"name": status}},
                "Last Contact": {"date": {"start": datetime.now().isoformat()}}
            }
        }
        
        if notes:
            update_data["properties"]["AI Analysis"] = {
                "rich_text": [{"text": {"content": notes}}]
            }
        
        try:
            response = requests.patch(
                f"{self.base_url}/pages/{page_id}",
                json=update_data,
                headers=self.headers
            )
            
            if response.status_code == 200:
                logger.info(f"✅ Updated lead status: {status}")
                return {"status": "updated", "new_status": status}
            else:
                logger.error(f"❌ Failed to update status: {response.text}")
                return {"status": "error", "error": response.text}
                
        except Exception as e:
            logger.error(f"❌ Error updating status: {e}")
            return {"status": "error", "error": str(e)}
    
    async def get_sales_dashboard_data(self) -> Dict:
        """Get sales dashboard data from Notion"""
        
        try:
            # Query database for all leads
            query_data = {
                "database_id": self.database_id,
                "filter": {
                    "property": "Status",
                    "select": {"does_not_equal": "❌ LOST"}
                }
            }
            
            response = requests.post(
                f"{self.base_url}/databases/{self.database_id}/query",
                json=query_data,
                headers=self.headers
            )
            
            if response.status_code == 200:
                data = response.json()
                leads = data.get("results", [])
                
                # Calculate metrics
                total_leads = len(leads)
                hot_leads = len([l for l in leads if l["properties"]["Status"]["select"]["name"] == "🔥 HOT LEAD"])
                warm_leads = len([l for l in leads if l["properties"]["Status"]["select"]["name"] == "✅ WARM LEAD"])
                closed_deals = len([l for l in leads if l["properties"]["Status"]["select"]["name"] == "🎯 CLOSED"])
                
                total_revenue = sum([
                    l["properties"]["Expected Revenue"]["number"] or 0 
                    for l in leads if l["properties"]["Status"]["select"]["name"] == "🎯 CLOSED"
                ])
                
                return {
                    "total_leads": total_leads,
                    "hot_leads": hot_leads,
                    "warm_leads": warm_leads,
                    "closed_deals": closed_deals,
                    "total_revenue": total_revenue,
                    "conversion_rate": (closed_deals / total_leads * 100) if total_leads > 0 else 0,
                    "data_source": "notion"
                }
            else:
                logger.error(f"❌ Failed to query database: {response.text}")
                return {"status": "error", "error": response.text}
                
        except Exception as e:
            logger.error(f"❌ Error getting dashboard data: {e}")
            return {"status": "error", "error": str(e)}

# Initialize Notion integration
notion_integration = NotionIntegration()

async def main():
    """Test Notion integration"""
    print("🚀 9LMNTS Notion Integration - STARTING")
    print("📝 Connecting Loa Brain AI Empire to Notion")
    print("🔗 Enabling Slack + CrewAI + Notion workflow automation")
    
    # Create lead database
    database_result = await notion_integration.create_lead_database()
    print(f"✅ Database Status: {database_result['status']}")
    
    # Test adding a lead
    test_lead = {
        "name": "Test Business",
        "company": "Test Corp",
        "business_type": "E-commerce",
        "budget": 5000,
        "timeline": "Urgent (24h)",
        "requirements": "Need AI automation for content and customer service",
        "contact_info": {
            "email": "test@example.com",
            "phone": "+1-555-0123"
        }
    }
    
    lead_result = await notion_integration.add_lead_to_notion(test_lead)
    print(f"✅ Lead Added: {lead_result['status']}")
    
    # Get dashboard data
    dashboard_data = await notion_integration.get_sales_dashboard_data()
    print(f"📊 Dashboard: {dashboard_data['total_leads']} leads, ${dashboard_data['total_revenue']:,} revenue")
    
    print("\n🎯 Notion Integration Ready:")
    print("   • Lead management database created")
    print("   • AI-powered lead qualification")
    print("   • CrewAI workflow triggers")
    print("   • Real-time sales dashboard")
    print("   • Proposal tracking system")
    
    print("\n🔗 Workflow Automation:")
    print("   • Lead → Notion → CrewAI → Slack → Loa Brain")
    print("   • Qualification → Proposal → Delivery → Payment")
    print("   • 24/7 automated sales pipeline")
    
    print("\n🚀 Complete AI Empire: Loa Brain + N8n + Notion + CrewAI + Slack!")

if __name__ == "__main__":
    asyncio.run(main())
