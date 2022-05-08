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
        WHEN: The seller submits the form
        THEN: They should get a bad request response of status code 400.

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
    
    def test_seller_registration_with_existing_email(self, register_seller, client):
        """

        Test for registration with existing email address
        GIVEN: A seller attempts to register with an email that has already being used
        WHEN: Seller submits form
        THEN: They should get a bad request response of status code 400
        
        """
        data = {
            "first_name": "Ajanaku",
            "last_name": "Idi-Amin",
            "email": register_seller,
            "state_of_residence": "Kampala",
            "password": "oyomesiogo"
        }

        response = client.post("/sellers/register", data=data)
        response_data = response.json()
        
        assert response.status_code == 400
        assert isinstance(response_data, dict)
        assert response_data["email"][0] == "seller with this email already exists."

    def test_seller_registration_with_password_with_incomplete_number_of_password(self, client):
        """
        GIVEN: A seller enters password with less than 10 characters registering
        WHEN: A seller clicks on submit on the form
        THEN: The backend should a 400 error with a message saying "Ensure this field has at least 10 characters"
        """
        data = {
            "first_name": "Ajanaku",
            "last_name": "Idi-Amin",
            "email": "abc@gmail.com",
            "state_of_residence": "Kampala",
            "password": "oyosiogo"
        }
        response = client.post("/sellers/register", data=data)
        response_data = response.json()
        assert response.status_code == 400
        assert isinstance(response_data, dict)
        assert response_data["password"][0] == "Ensure this field has at least 10 characters."
    

    def test_successful_login(self, register_seller, client):
        """
        GIVEN: A seller enters their email and password used when registering
        WHEN: A seller clicks on submit on the form
        THEN: The backend should return refresh and access tokens with status code of 200
        """

        data = {
            "email": register_seller,
            "password": "vision2022"
        }
        response = client.post("/sellers/login", data=data)
        response_data = response.json()
        
        assert response.status_code == 200
        assert isinstance(response_data, dict)
        assert response_data["refresh"]
        assert response_data["access"]

    
    def test_login_with_invalid_password(self, register_seller, client):
        """
        GIVEN: A seller enters their correct email and an invalid password
        WHEN: A seller clicks on submit on the form
        THEN: The backend should return a 401 status code and a message saying 'No active account found with the given credentials
        """
        
        data = {
            "email": register_seller,
            "password": "vision222"
        }
        response = client.post("/sellers/login", data=data)
        response_data = response.json()
        
        assert response.status_code == 401
        assert isinstance(response_data, dict)
        assert response_data["detail"] == "No active account found with the given credentials"