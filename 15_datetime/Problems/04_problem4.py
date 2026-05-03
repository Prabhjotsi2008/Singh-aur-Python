# LOG ANALYSER
from datetime import datetime

def calc_seconds(logs):
    login_time = None
    session_duration = 0

    for log in logs:
        time_str, action = log.split(" - ")
        time_obj = datetime.strptime(time_str,"%Y-%m-%d %H:%M:%S")

        if action == "Login":
            login_time = time_obj
        elif action == "Logout" and login_time:
            session = time_obj - login_time
            session_duration += session.total_seconds()
            login_time = None
    
    return session_duration

def time_formatter(seconds):
    hours = seconds // 3600
    minutes = (seconds%3600) // 60
    secs = seconds%60

    return f"{hours} Hours, {minutes} Minutes, {secs} Seconds"

logs = [
    "2026-04-20 10:30:00 - Login",
    "2026-04-20 12:00:00 - Logout",
    "2026-04-20 13:00:00 - Login",
    "2026-04-20 14:15:00 - Logout"
]

seconds = calc_seconds(logs)
output = time_formatter(seconds)

print(f"Total Sessions Duration: {output}")
