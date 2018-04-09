# generic

from rest_framework import generics

from .serializers import BlogPostSerializer
from postings.models import BlogPost

class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView): # DetailView CreateView FormView
    lookup_field        = 'pk' # slug, id # url(r'^(?P<pk>\d+)')
    serializer_class    = BlogPostSerializer
    #queryset            = BlogPost.objects.all()

    def get_queryset(self):
        return BlogPost.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return BlogPost.objects.get(pk=pk)
