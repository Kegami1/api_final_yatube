from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Post, User, Follow, Group


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(read_only=True,
                            slug_field='username',
                            default=CurrentUserDefault()
                            )
    following = SlugRelatedField(queryset=User.objects.all(),
                                 slug_field='username',
                                 )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Вы уже подписаны'
            )
        ]

    def validate_following(self, value):
        if self.context['request'].user == value:
            raise serializers.ValidationError(
                "Вы не можете подписаться сами на себя")
        return value


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
