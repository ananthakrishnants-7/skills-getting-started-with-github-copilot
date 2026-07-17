from fastapi.testclient import TestClient

import src.app as app_module


client = TestClient(app_module.app)


def test_unregister_participant_from_activity():
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    response = client.delete(f"/activities/{activity_name}/signup?email={email}")

    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"
    assert email not in app_module.activities[activity_name]["participants"]

    # restore the state for later tests
    app_module.activities[activity_name]["participants"].append(email)
