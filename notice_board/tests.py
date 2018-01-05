# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import PostForm, CommentForm
from django.test import TestCase
from .models import Post, Comment
from django.contrib.auth.models import User
from user_authentication.models import Profile
from django.core.urlresolvers import reverse


class ViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user', email="user@fis.agh.edu.pl", password="alamakota22",
                                             first_name="user", last_name="user")
        self.profile = Profile.objects.create(user=self.user)

        self.admin = User.objects.create_superuser(username='admin', email="admin@mail.com", password="jkadyen3",
                                                   first_name="admin", last_name="admin")
        self.profile = Profile.objects.create(user=self.admin)

        self.post = Post.objects.create(title='title', slug='title', author=self.admin)

    def test_view_detail(self):
        self.client.login(username='user', password='alamakota22')
        response = self.client.get(reverse('notice_board:post_detail', args=[self.post.publish.year,
                                                                             self.post.publish.strftime('%m'),
                                                                             self.post.publish.strftime('%d'),
                                                                             self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/detail.html')


