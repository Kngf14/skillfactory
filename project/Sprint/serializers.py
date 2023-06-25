from .models import User, Coords, Level, Mountain, ImagesOfMountains
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = User
       fields = ['email', 'phone', 'fam', 'name', 'otc']

class CoordsSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Coords
       fields = ['latitude', 'longitude', 'height']

class LevelSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Level
       fields = ['winter', 'spring', 'summer', 'autumn']

class ImageSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Image
       fields = ['data', 'title']

class MountainSerializer(serializers.HyperlinkedModelSerializer):
   user = UserSerializer()
   coords = CoordsSerializer()
   level = LevelSerializer()
   images = ImageSerializer()

   class Meta:
       model = Mountain
       fields = ['beauty_title', 'title', 'other_titles', 'connect',
                 'add_time', 'author', 'level', 'coords', 'status']
