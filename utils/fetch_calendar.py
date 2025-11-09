
STATIC_CALENDAR_DATA = {
    
    "semester_title": "Fall 2025 Trimester/Semester",
    "last_updated": "2025-11-03", 
    "events": [
        {"date": "Nov 11", "description": "Classes Begin (Trimester)"},
        {"date": "Dec 21 - Jan 7, 2026", "description": "Final Exam Period (B. Pharm)"},
        {"date": "Jan 4, 2026", "description": "Last Date of Admission (Spring 2026)"},
        {"date": "Jan 11, 2026", "description": "Last Day of Grade Submission"},
    ]
}

async def fetch_academic_calendar(program_name=None):
    return STATIC_CALENDAR_DATA

async def get_calendar_options():
    return []