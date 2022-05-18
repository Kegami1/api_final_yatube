from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


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
    user = SlugRelatedField(
        read_only=True, slug_field='username'
    )
    following = SlugRelatedField(
        queryset=User.objects.all(), slug_field='username'
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')

    def validate(self, data):
        if self.context['request'].user == data['following']:
            raise serializers.ValidationError("Вы не можете подписаться сами на себя")
        if Follow.objects.filter(
            user=self.context['request'].user,
            following=data['following']
            ).exists():
                raise serializers.ValidationError("Вы уже подписаны")
        return data        


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'