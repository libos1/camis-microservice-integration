# main.py
# FastAPI Service: High-Performance Alert Gateway

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio
from datetime import datetime

# Define the data structure for an incoming alert (using Pydantic)
class AlertRequest(BaseModel):
    student_id: str
    alert_type: str  # e.g., "ATTENDANCE_MISSED" or "FEE_DUE"
    recipient_phone: str
    message_content: str

app = FastAPI()

@app.post("/api/v1/alert/trigger")
async def trigger_alert(request: AlertRequest):
    """
    API endpoint for the core CAMIS system to send an alert request.
    This runs asynchronously for speed.
    """
    print(f"[{datetime.now()}] Incoming Alert for: {request.student_id}")

    # --- Simulate high-speed alert processing ---
    # In a real app, this would queue SMS/Email delivery (e.g., using a background task queue)
    await asyncio.sleep(0.01)  # Simulate minimal processing time

    if request.alert_type == "ATTENDANCE_MISSED":
        log_status = "SUCCESS: SMS queued for parent."
    else:
        log_status = "SUCCESS: Email notification sent."

    return {
        "status": log_status, 
        "request_time": datetime.now().isoformat()
    }

# FastAPI's simple health check endpoint
@app.get("/health")
def health_check():
    return {"status": "Alert Gateway is Online"}
