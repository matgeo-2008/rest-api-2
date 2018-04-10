from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from rest_framework_jwt.settings import api_settings

payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler = api_settings.JWT_ENCODE_HANDLER

from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

# automated
# new / blank db

from postings.models import BlogPost

User = get_user_model()

class BlogPostAPITestCase(APITestCase):
    def setUp(self):
        user_obj = User(username="test", email="test@example.com")
        user_obj.set_password("pass1234")
        user_obj.save()
        blog_post = BlogPost.objects.create(
                user=user_obj,
                title='New Title',
                content='some_random_content',
            )

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_post(self):
        post_count = BlogPost.objects.count()
        self.assertEqual(post_count, 1)

    def test_get_list(self):
        # test the get list item
        data = {}
        url = api_reverse("api-postings:post-listcreate")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #print(response.data)

    def test_post_item(self):
        # test the get list item
        data = {"title": "some random title", "content": "some more content"}
        url = api_reverse("api-postings:post-listcreate")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_item(self):
        # test the get list item
        blog_post = BlogPost.objects.first()
        data = {}
        url = blog_post.get_api_url()
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)

    def test_update_item(self):
        # test the get list item
        blog_post = BlogPost.objects.first()
        url = blog_post.get_api_url()
        data = {"title": "some random title", "content": "some more content"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_item_with_user(self):
        # test the get list item
        blog_post = BlogPost.objects.first()
        print(blog_post.content)
        url = blog_post.get_api_url()
        data = {"title": "some random title", "content": "some more content"}
        user_obj = User.objects.first()
        payload = payload_handler(user_obj)
        token_rsp = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_rsp) # JWT <token>

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        print(response.data)
