import pytest

@pytest.fixture()
def get_server():
    return "192.168.0.1"

@pytest.fixture()
def create_files():
    # приєднуємося
    print("приєднуємося")
    yield 
    # чистимо і відєднуємся
    print("відєдналися")

@pytest.fixture(scope="module", autouse=True)
def create_viual_machine():
    # приєднуємося
    print("Створено ВМ")
    yield 
    # чистимо і відєднуємся
    print("ВМ Знищено")
