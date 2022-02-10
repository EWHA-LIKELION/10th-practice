from typing import List

# Create your views here.
from django.views.generic import ListView, DetailView
from community.models import Posting

class PostListLV(ListView):
    model = Posting

class PostListDV(DetailView):
    model = Posting
