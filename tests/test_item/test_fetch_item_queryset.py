import pytest

@pytest.mark.django_db
class TestGetItem:
    def test_successful_list_items(self, client):
        """
        Test for successful retrieval of all items

        WHEN: A visitor hits this endpoint, "/items/all_items"
        THEN: They should get a success response of status code 200

        """

        response = client.get('/items/all_items')
        assert response.status_code == 200

    def test_list_items_successful_for_a_seller(self, client, seller_token):
        """
        Test for succesful item retrieval for a seller

        WHEN: A a visitor hits this endpoint "/items/list_items_for_sellers" to see all the lists of items created by a seller
        THEN: They should get a 200 response
        
        """
        response = client.get('/items/list_items_for_sellers', **seller_token)
        assert response.status_code == 200
        assert isinstance(response.json(), list) is True

    

    def test_list_items_for_a_seller_with_no_token(self, client):
        """

        Test for unsuccesful item retrieval for a seller due to no token
        WHEN: A a visitor hits this endpoint "/items/list_items_for_sellers" to see all the lists of items created by a seller and they supply no token
        THEN: They should get a 401 response and a message that says "Authentication credentials were not provided."
        
        """

        response = client.get('/items/list_items_for_sellers')
        assert response.status_code == 401
        assert response.json()['detail'] == "Authentication credentials were not provided."

    def test_list_items_for_a_seller_with_invalid_token(self, client, seller_invalid_token):
        """

        Test for unsuccesful item retrieval for a seller due to invalid token
        WHEN: A a visitor hits this endpoint "/items/list_items_for_sellers" to see all the lists of items created by a seller and they supply and invalid token
        THEN: They should get a 401 response and a message that says "Token is invalid or expired"
        
        """
        response = client.get('/items/list_items_for_sellers', **seller_invalid_token)
        assert response.status_code == 401
        assert response.json()["detail"] == "Given token not valid for any token type"
        assert response.json()["code"] == "token_not_valid"
        assert response.json()["messages"][0]["message"] == "Token is invalid or expired"