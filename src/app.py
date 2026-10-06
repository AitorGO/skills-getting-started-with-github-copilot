"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Practice ball handling, teamwork, and match strategy on the field",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 18,
        "participants": ["alex@mergington.edu", "mia@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Build shooting, passing, and defensive skills through drills and games",
        "schedule": "Wednesdays, 3:30 PM - 5:30 PM",
        "max_participants": 14,
        "participants": ["noah@mergington.edu", "ava@mergington.edu"]
    },
    "Drama Club": {
        "description": "Explore acting, stage presence, and theatrical performance techniques",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 16,
        "participants": ["ella@mergington.edu", "liam@mergington.edu"]
    },
    "Art Workshop": {
        "description": "Create paintings, drawings, and mixed-media projects in a creative studio",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["grace@mergington.edu", "lucas@mergington.edu"]
    },
    "Math Olympiad": {
        "description": "Solve challenging math problems and prepare for competitions",
        "schedule": "Wednesdays, 4:00 PM - 5:00 PM",
        "max_participants": 10,
        "participants": ["isabella@mergington.edu", "henry@mergington.edu"]
    },
    "Science Club": {
        "description": "Conduct experiments and explore topics in biology, chemistry, and physics",
        "schedule": "Fridays, 2:30 PM - 4:00 PM",
        "max_participants": 20,
        "participants": ["charlotte@mergington.edu", "benjamin@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]
    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student is already signed up for this activity")
    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
