from django.test import Client, TestCase
from django.urls import reverse

from wykop.accounts.models import User
from wykop.posts.models import Post


class PostsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('secret')
        self.user.save()
        self.post1 = Post.objects.create(
            title='Post 1', author=self.user,
            text='Post 1 content',
        )
        self.post2 = Post.objects.create(
            title='Post 2', author=self.user,
            text='Post 2 content',
        )
        self.client = Client()

    def test_posts_list(self):
        response = self.client.get(
            reverse('posts:list')
        )
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post2.title)
        self.assertNotContains(response, self.post1.text)
        self.assertNotContains(response, self.post2.text)

    def test_post_detail(self):
        response = self.client.get(
            reverse('posts:detail', args=(self.post1.pk, ))
        )
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)

    def test_post_create(self):
        self.client.login(
            username=self.user.username,
            password='secret',
        )
        title = 'Post 3 title'
        text = 'Post 3 content'
        response = self.client.post(
            reverse('posts:create'),
            {
                'title': title,
                'text': text
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 3)
