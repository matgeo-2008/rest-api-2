from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

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
