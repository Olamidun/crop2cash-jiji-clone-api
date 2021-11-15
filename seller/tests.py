from rest_framework.test import APITestCase
from django.urls import reverse

# Create your tests here.

class SellerTestSetup(APITestCase):

    def setUp(self):
        self.register_url = reverse('seller:register')
        self.login_url = reverse('seller:login')

        seller_data = {
            'first_name': 'Kolapo',
            'last_name': 'Opeoluwa',
            'email':'kolapooolamidun@gmail.com',
            'password': 'vision2021'
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()



class SellerTestView(SellerTestSetup):

    def test_seller_cannot_register_with_no_data(self):
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, 400)

    def test_seller_can_register(self):
        seller_data = {
            'first_name': 'Kolapo',
            'last_name': 'Opeoluwa',
            'email':'kolapooolamidun@gmail.com',
            'state_of_residence': 'Kaduna',
            'password': 'vision2021'
        }
        response = self.client.post(self.register_url, seller_data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['message'], 'Your account has been created successfully')

    
    def test_seller_cannot_login_successfully(self):
        seller_data = {
            'email':'kolapooolamidun@gmail.com',
            'password': 'vision2021'
        }
        response = self.client.post(self.login_url, seller_data, format="json")
        # import pdb
        # pdb.set_trace()
        self.assertEqual(response.status_code, 401)

    def test_seller_can_login_successfully(self):
        seller_login_data = {
            'email':'kolapooolamidun@gmail.com',
            'password': 'vision2021'
        }
        response = self.client.post(self.login_url, seller_login_data, format="json")
        import pdb
        pdb.set_trace()
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'refresh')
        self.assertContains(response, 'access')
