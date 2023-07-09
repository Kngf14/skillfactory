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

class ImagesOfMountainsSerializer(serializers.ModelSerializer):
   id = serializers.IntegerField(required = False)

   class Meta:
       model = ImagesOfMountains
       fields = ['id', 'data', 'title']

class MountainSerializer(serializers.HyperlinkedModelSerializer):
   user = UserSerializer()
   coords = CoordsSerializer()
   level = LevelSerializer()


   class Meta:
       model = Mountain
       fields = ['beauty_title', 'title', 'other_titles', 'connect',
                 'add_time', 'user', 'level', 'coords', 'status', 'imagesofmountains']

   def create(self, validated_data):
        user_data = validated_data.pop('user')
        coords_data = validated_data.pop('coords')
        level_data = validated_data.pop('level')
        imagesofmountains_data = validated_data.pop('imagesofmountains')

        user_email = user_data.get('email')
        if User.objects.filter(email = user_email).exists():
            user = User.objects.get(email = user_email)

        else:
            user = User.objects.create(**user_data)

        coords = Coords.objects.create(**coords_data)
        level = Level.objects.create(**level_data)

        instance = Mountain.objects.create(user = user, level = level, coords = coords, **validated_data)
        instance.save()

        for imagesofmountains in imagesofmountains_data:
            imagesofmountains.objects.create(mountain = instance, **imagesofmountains_data)
        return instance

   def update(self, instance, validated_data):
        if instance.status == 'NEW':
            if 'user' in validated_data:
                raise serializers.ValidationError()

            if 'coords' in validated_data:
                coords = self.fields['coords']
                coords_instance = instance.coords
                coords_data = validated_data.pop('coords')
                coords.update(coords_instance, coords_data)

            if 'level' in validated_data:
                level = self.fields['level']
                level_instance = instance.level
                level_data = validated_data.pop('level')
                level.update(level_instance, level_data)

            if 'images' in validated_data:
                imagesofmountains_data = validated_data.pop('images')

                for imagesofmountains in imagesofmountains_data:
                    imagesofmountains_id = imagesofmountains.get('id', None)
                    if imagesofmountains_id:
                        inv_imagesofmountains = imagesofmountains.objects.get(id = image_id)
                        inv_imagesofmountains.data = imagesofmountains.get('data', inv_imagesofmountains.data)
                        inv_imagesofmountains.title = imagesofmountains.get('title', inv_imagesofmountains.title)
                        inv_imagesofmountains.save()
                    else:
                        imagesofmountains.objects.create(mountain = instance, **image)

                imagesofmountains_dict = dict((i.id, i) for i in instance.imagesofmountains.all())
                if len(imagesofmountains_data) == 0:
                    for imagesofmountains in imagesofmountains_dict.values():
                        imagesofmountains.delete()

            return super(MountainSerializer, self).update(instance, validated_data)
        raise serializers.ValidationError('Update error. Object status is not <NEW>')