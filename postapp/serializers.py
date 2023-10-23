from rest_framework import serializers
from .models import BlogPost

class CreateBlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title', 'body']

    def save(self):
        blogpost = BlogPost (title=self.validated_data['title'])
        title = self.validated_data['title']

        # Add validations before saving
        if (len(title) >20):                                                                                                             #Make sure that fullname is not more than 50
            raise serializers.ValidationError({'title' : 'Title cannot be more than 20 characters.'})

        blogpost.save()
        return blogpost
