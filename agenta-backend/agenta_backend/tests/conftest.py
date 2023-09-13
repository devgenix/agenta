import pytest
import docker
import asyncio
from fastapi.testclient import TestClient

from agenta_backend.models.db_engine import DBEngine
from agenta_backend.main import app


@pytest.fixture(scope="session", autouse=True)
def test_app():
    client = TestClient(app)
    return client  # provide the test client to the tests
    # teardown code goes here


@pytest.fixture(scope="function")
def test_db_engine():
    # Initialize the DBEngine in 'test' mode
    db_engine = DBEngine()
    test_engine = db_engine.engine()
    yield test_engine
    db_engine.remove_db()


@pytest.fixture(scope="session")
def docker_client():
    return docker.from_env()


@pytest.fixture()
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    
    pending = asyncio.tasks.all_tasks(loop)
    loop.run_until_complete(asyncio.gather(*pending))
    loop.run_until_complete(asyncio.sleep(1))
    
    loop.close()


# def pytest_sessionfinish(session, exitstatus):
#     asyncio.get_event_loop().close()