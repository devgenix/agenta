import httpx
import pytest
import logging

# Initialize http client
test_client = httpx.Client()
timeout = httpx.Timeout(timeout=5, read=None, write=5)


# Set global variables
BACKEND_API_HOST = "http://localhost"


@pytest.mark.asyncio
def test_create_app(app_payload, get_user_org_id):

    # app_name = app_payload["name"]
    payload = {"app_name": app_payload["name"], "organization_id": get_user_org_id}
    response = test_client.post(
        f"{BACKEND_API_HOST}/apps/",
            json=payload,
            timeout=timeout,
    )
    assert response.status_code == 200