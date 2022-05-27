import pytest
from rest_framework import status

@pytest.mark.django_db(transaction=True)
class TestCreateItem:
    def test_successful_item_creation(self, client, seller_token):
        """
        Test for successful item creation

        GIVEN: A seller enters name, price, image and description of items
        WHEN: The seller submits the form
        THEN: They should get a success response of status code 201, A message that says 'Item has been created successfully'
        """
        with open('tests/test_item/0_U8TbUaajSO7rXk1j.jpg', 'rb') as image:
            data = {
                "name": "An Item",
                "price": 15000.55,
                "description": "This is a random item",
                "image": image
            }
        
            response = client.post("/items/create_item", data=data, **seller_token)
            response_data = response.json()
            print(response_data)
            assert response.status_code == 201
            assert response_data["message"] == "Item has been created successfully"

    def test_create_item_with_invalid_token(self, client, seller_invalid_token):
        """
        Test for unsuccessful item creation due to invalid token

        GIVEN: A seller enters name, price, image and description of items correctly but is using an invalid token
        WHEN: The seller submits the form
        THEN: They should get a success response of status code 401, A message that tells them about the use of invalid token

        """
        with open('tests/test_item/0_U8TbUaajSO7rXk1j.jpg', 'rb') as image:
            data = {
                "name": "An Item",
                "price": 15000.55,
                "description": "This is a random item",
                "image": image
            }
        
            response = client.post("/items/create_item", data=data, **seller_invalid_token)
            response_data = response.json()
            print(response_data)
            assert response.status_code == 401
            assert response_data["detail"] == "Given token not valid for any token type"
            assert response_data["code"] == "token_not_valid"
            assert response_data["messages"][0]["message"] == "Token is invalid or expired"

    def test_create_item_with_no_token(self, client, seller_token):
        """
        Test for unsuccessful item creation due to invalid token

        GIVEN: A seller enters name, price, image and description of items correctly but is not authenticated
        WHEN: The seller submits the form
        THEN: They should get a success response of status code 401, A message that tells them that they are have no provided authentication credentials

        """
        with open('tests/test_item/0_U8TbUaajSO7rXk1j.jpg', 'rb') as image:
            data = {
                "name": "An Item",
                "price": 15000.55,
                "description": "This is a random item",
                "image": image
            }
        
            response = client.post("/items/create_item", data=data)
            response_data = response.json()
            print(response_data)
            assert response.status_code == 401
            assert response_data["detail"] == "Authentication credentials were not provided."

    
    @pytest.mark.parametrize(
        "item_payload, expected_response",
        [
            (
                {},
                (
                    status.HTTP_400_BAD_REQUEST,
                    {
                        "name": [
                            "This field is required."
                        ],
                        "price": [
                            "This field is required."
                        ],
                        "image": [
                            "No file was submitted."
                        ],
                        "description": [
                            "This field is required."
                        ]
                    },
                ),
            ),
            (
                {
                    "name": "A new item",
                    "price": 15000,
                    "description": "This is a new item"
                },
                (
                    status.HTTP_400_BAD_REQUEST,
                    {
                        "image": [
                            "No file was submitted."
                        ]
                    },
                ),
            ),
            (
                {
                    "price": 15000,
                    "description": "This is a new item"
                },
                (
                    status.HTTP_400_BAD_REQUEST,
                    {
                        "name": [
                            "This field is required."
                        ],
                        "image": [
                            "No file was submitted."
                        ]
                    },
                ),
            ),
            (
                {   
                    "name": "AN item",
                    "price": "fifteen thousand",
                    "description": "This is an item"
                },
                (
                    status.HTTP_400_BAD_REQUEST,
                    {
                        "price": [
                            "A valid number is required."
                        ],
                        "image": [
                            "No file was submitted."
                        ]
                    },
                )
            )
        ],
    )
    def test_create_item_unsuccessful(self, client, seller_token, item_payload, expected_response):

        """
        Test for unsuccessful registration
        GIVEN: A seller does not enter all the fields completely or enter the wrong data type
        WHEN: The seller submits the form
        THEN: They should get a bad request response of status code 400
        
        """

        response = client.post("/items/create_item", data=item_payload, **seller_token)
        response_data = response.json()

        assert response.status_code == expected_response[0]
        assert response_data == expected_response[1]