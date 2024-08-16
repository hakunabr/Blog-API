from .models import BlogPost, Tag
from rest_framework import serializers

class BlogpostSerializer(serializers.ModelSerializer):
    tags = serializers.CharField(write_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'date_posted', 'tags']

    def create(self, validated_data):
        tags_str = validated_data.pop('tags')
        tags_list = tags_str.split()
        blog_post = BlogPost.objects.create(**validated_data)

        for tag_name in tags_list:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            blog_post.tags.add(tag)

        return blog_post