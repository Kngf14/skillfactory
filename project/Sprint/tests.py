from mountains.serializers import MountainSerializer
from django.test import TestCase, RequestFactory
from .models import User, Coords, Level, Mountain, ImagesOfMountains
from django.contrib.auth.models import AnonymousUser
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase

def create_Mountain(self):

    return Mountain.objects.create(beauty_title = 'wowtitle', title = 'smthtitle', other_titles = 'othersmth_title', author = self.user,  level = self.level, coord = self.coord, ImagesOfMountains = self.image)

class MountainApiTestCase(TestCase):

    def setup(self):
        self.user = User.objects.create(email = 'exmp@mail.com', phone = '+79121231234', fam = 'khalitov', name = 'ruslan', otc = 'rustamovich')
        self.coord = Coords.objects.create(latitude='60.000', longitude='60.000', height='1200')
        self.level = Level.objects.create(winter = 'winter')

    def tearDown(self):

        pass

    def test_setUpTestData(self):
        new = create_Mountain(self)
        self.assertEqual(new.beauty_title, 'wowtitle')


class PersonViewSetTests(APITestCase):

    def test_list_Mountain(self):

        url = 'http://127.0.0.1:8000%s' % reverse('test_create_Mountain')

        response = self.client.get(url, format='json')
        json = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(json), 4)
