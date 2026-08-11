import requests


BASE_URL = "http://127.0.0.1:8000"


def get_dashboard():

    response = requests.get(
        f"{BASE_URL}/dashboard/summary"
    )

    return response.json()



def get_project_status():

    response = requests.get(
        f"{BASE_URL}/analytics/project-status"
    )

    return response.json()



def get_task_status():

    response = requests.get(
        f"{BASE_URL}/analytics/task-status"
    )

    return response.json()



def get_task_priority():

    response = requests.get(
        f"{BASE_URL}/analytics/task-priority"
    )

    return response.json()



def get_deadlines():

    response = requests.get(
        f"{BASE_URL}/analytics/upcoming-deadlines"
    )

    return response.json()



def get_recommendations():

    response = requests.get(
        f"{BASE_URL}/ai/recommendations"
    )

    return response.json()



def chat_with_ai(
    session_id,
    message
):

    response = requests.post(
        f"{BASE_URL}/ai/chat",
        json={
            "session_id": session_id,
            "message": message
        }
    )

    return response.json()