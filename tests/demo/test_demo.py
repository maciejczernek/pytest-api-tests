import allure
import pytest

from request_lib.req_collection import JsonPlaceholder


@pytest.mark.api
@allure.parent_suite("API Tests")
@allure.suite("Demo requests")
@allure.title("GET the resource 1")
def test_get_resource_1():
    expected_status_code = 200
    expected_response_time = 0.20
    expected_userId = 1
    expected_id = 1
    expected_title = ("sunt aut facere repellat provident occaecati excepturi "
                      "optio reprehenderit")

    collection = JsonPlaceholder()
    response = collection.get_resource("1")
    res_body = response.json()

    with allure.step(f"Verify the status code is {expected_status_code}"):
        assert response.status_code == expected_status_code

    with allure.step(
            f"Verify the response time is less than {expected_response_time}s"):
        assert response.elapsed.total_seconds() < expected_response_time

    with allure.step(f"Verify the userId is {expected_userId}"):
        assert res_body["userId"] == expected_userId

    with allure.step(f"Verify the id is {expected_id}"):
        assert res_body["id"] == expected_id

    with allure.step(f"Verify the title is {expected_title}"):
        assert res_body["title"] == expected_title


@pytest.mark.api
@allure.parent_suite("API Tests")
@allure.suite("Demo requests")
@allure.title("GET the resource 2")
def test_get_resource_2():
    expected_status_code = 200
    expected_userId = 1
    expected_id = 2
    expected_title = "qui est esse"
    expected_response_time = 0.20

    collection = JsonPlaceholder()
    response = collection.get_resource("2")
    res_body = response.json()

    with allure.step(f"Verify the status code is {expected_status_code}"):
        assert response.status_code == expected_status_code

    with allure.step(
            f"Verify the response time is less than {expected_response_time}s"):
        assert response.elapsed.seconds < expected_response_time

    with allure.step(f"Verify the userId is {expected_userId}"):
        assert res_body["userId"] == expected_userId

    with allure.step(f"Verify the id is {expected_id}"):
        assert res_body["id"] == expected_id

    with allure.step(f"Verify the title is {expected_title}"):
        assert res_body["title"] == expected_title


@pytest.mark.api
@allure.parent_suite("API Tests")
@allure.suite("Demo requests")
@allure.title("GET all resources")
def test_get_all_resources():
    expected_status_code = 200
    expected_response_time = 0.200
    expected_length = 100

    collection = JsonPlaceholder()
    response = collection.get_all_resource()
    res_body = response.json()

    with allure.step(f"Verify the status code is {expected_status_code}"):
        assert response.status_code == expected_status_code

    with allure.step(
            f"Verify the response time is less than {expected_response_time}s"):
        assert response.elapsed.seconds < expected_response_time

    with allure.step("Verify the length of the response body > 0"):
        assert len(res_body) > 0

    with allure.step(
            f"Verify the length of the response body == {expected_length}"):
        assert len(res_body) == expected_length


@pytest.mark.api
@allure.parent_suite("API Tests")
@allure.suite("Demo requests")
@allure.title("DELETE the resource 1")
def test_delete_resource_1():
    expected_status_code = 200
    expected_response_time = 0.20

    collection = JsonPlaceholder()
    response = collection.delete_resource("1")
    res_body = response.json()

    with allure.step(f"Verify the status code is {expected_status_code}"):
        assert response.status_code == expected_status_code

    with allure.step(
            f"Verify the response time is less than {expected_response_time}s"):
        assert response.elapsed.seconds < expected_response_time

    with allure.step(f"Verify the length of the response body == 0"):
        assert len(res_body) == 0


@pytest.mark.api
@allure.parent_suite("API Tests")
@allure.suite("Demo requests")
@allure.title("DELETE the no-existent resource")
def test_delete_resource_no_existent():
    expected_status_code = 404
    expected_response_time = 0.20

    collection = JsonPlaceholder()
    response = collection.delete_resource("")

    with allure.step(f"Verify the status code is {expected_status_code}"):
        assert response.status_code == expected_status_code

    with allure.step(
            f"Verify the response time is less than {expected_response_time}s"):
        assert response.elapsed.seconds < expected_response_time


@pytest.mark.api
@allure.parent_suite("API Tests")
@allure.suite("Demo requests")
@allure.title("POST resource")
def test_post_resource_valid_data():
    expected_status_code = 201
    expected_response_time = 0.20
    expected_response_id = 101
    data = {
        'title': 'foo',
        'body': 'bar',
        'userId': 5
    }

    collection = JsonPlaceholder()
    response = collection.post_resource(data)
    res_body = response.json()

    with allure.step(f"Verify the status code is {expected_status_code}"):
        assert response.status_code == expected_status_code

    with allure.step(
            f"Verify the response time is less than {expected_response_time}s"):
        assert response.elapsed.seconds < expected_response_time

    with allure.step(
            f"Verify the response id is {expected_response_id}"):
        assert res_body["id"] == expected_response_id
