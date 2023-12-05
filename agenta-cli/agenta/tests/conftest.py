import os
import pytest
import asyncio
import requests

# Set global variables
BACKEND_API_HOST = "http://localhost"

@pytest.fixture(scope="session", autouse=True)
def event_loop():
    """Create an instance of the default event loop for each test case."""
    policy = asyncio.get_event_loop_policy()
    res = policy.new_event_loop()
    asyncio.set_event_loop(res)
    res._close = res.close

    yield res

    res._close()  # close event loop


@pytest.fixture(scope="session", autouse=True)
def app_payload():
    return {"name": "cli-test"}
  

@pytest.fixture(scope="session", autouse=True)
def get_user_id():
    response = requests.get(f"{BACKEND_API_HOST}/profile/")
    return response.json()["uid"]

  
@pytest.fixture(scope="session", autouse=True)
def get_user_org_id():
    response = requests.get(f"{BACKEND_API_HOST}/organization/own/")
    return response.json()["id"]
