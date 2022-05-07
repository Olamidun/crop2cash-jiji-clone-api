import pytest
from seller.factory.factories import SellerFactory

@pytest.mark.django_db
class TestAuthentication:
    def test_successful_seller_registration(self, client):

        """
        
        Test for successful registration

        GIVEN: A seller enters their first name, last name, email, state of residence, and password correctly
        WHEN: The user submits the form
        THEN: They should get a success response of status code 201, A message that says 'You account has been created successfully

        """
        data = {
            "first_name": "Ajanaku",
            "last_name": "Idi-Amin",
            "email": "ajidi.amin@gmail.com",
            "state_of_residence": "Kampala",
            "password": "oyomesiogo"
        }
        response = client.post("/sellers/register", data=data)
        response_data = response.json()
        
        assert response.status_code == 201
        assert isinstance(response_data, dict)
        assert response_data["message"] == "Your account has been created successfully"
    
    def test_unsuccessful_seller_registration(self, client):

        """
        
        Test for successful registration

        GIVEN: A seller enters their first name, last name, state of residence, password correctly then an invalid email
        WHEN: The user submits the form
        THEN: They should get a success response of status code 201, A message that says 'You account has been created successfully

        """
        data = {
            "first_name": "Ajanaku",
            "last_name": "Idi-Amin",
            "email": "ajidi.amin@.com",
            "state_of_residence": "Kampala",
            "password": "oyomesiogo"
        }

        response = client.post("/sellers/register", data=data)
        response_data = response.json()
        
        assert response.status_code == 400
        assert isinstance(response_data, dict)