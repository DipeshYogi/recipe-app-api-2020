from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):

    """Setup tasks are tasks that are performed before running tests"""
    def setUp(self):
        self.Client = Client()
        self.admin_user = get_user_model().objects.create_superuser('test@123.com', 'test123')

        self.Client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
                        email='antoher@gmail.com',
                        password='testtest',
                        name='test user')

    def test_user_listed(self):
        """Test if users are listed in users page"""
        url = reverse('admin:core_user_changelist')
        res = self.Client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """test that user edit page works"""
        url = reverse("admin:core_user_change",args=[self.user.id])
        res = self.Client.get(url)

        self.assertEqual(res.status_code,200)  #200 res code for OK

    def test_create_user_page(self):
        """test that user create works"""
        url = reverse("admin:core_user_add")
        res = self.Client.get(url)

        self.assertEqual(res.status_code,200)
