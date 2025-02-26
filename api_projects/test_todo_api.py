import requests

ENDPOINT = "https://todo.pixegami.io"
#
# response = requests.get(ENDPOINT)
# print(requests)
#
# data = response.json()
# print(data)
#
# status_code = response.status_code
# print(status_code)

def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_can_create_task():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    data = create_task_response.json()
    # print(data)

    task_id = data["task"]["task_id"]
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    # print(get_task_data)

    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]

def test_can_update_task():
    # create a task
    payload = new_task_payload()
    create_task_respononse = create_task(payload)
    assert create_task_respononse.status_code == 200
    task_id = create_task_respononse.json()["task"]["task_id"]
    # update the task
    new_payload = {
        "user_id" : payload["user_id"],
        "task_id" : task_id,
        "content" : "my updated content",
        "is_done" : True,
        }
    update_task_reponse = update_task(new_payload)
    assert update_task_reponse.status_code == 200

    # get and validate the changes
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["is_done"] == new_payload["is_done"]





# Helper functions
def create_task(payload):
    return requests.put(ENDPOINT + "/create-task", json=payload)

def update_task(payload):
    return requests.put(ENDPOINT + "/update-task", json=payload)
def get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")

def new_task_payload():
    return {
        "content": "my_test_content",
        "user_id": "test_user_id",
        "is_done": False
    }