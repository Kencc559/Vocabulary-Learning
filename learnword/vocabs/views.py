#file: vocabs/views.py

from django.shortcuts import render

# Create your views here.
def review_view(request):
    return render(request, "review_list.html")

def learn_eng_website_list_view(request):
    return render(request, "learn_eng_website_list.html")