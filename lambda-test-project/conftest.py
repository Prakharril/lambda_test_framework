import pytest
from utils.driver_factory import get_driver

@pytest.fixture
def driver(request):
    test_name = request.node.name
    driver = get_driver(test_name, build_name="LambdaTest QA Build")
    yield driver
    driver.quit()
