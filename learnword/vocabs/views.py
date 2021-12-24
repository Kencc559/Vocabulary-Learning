#file: vocabs/views.py

from django.shortcuts import render

# Create your views here.
def review(request):
    print("review")
    return render(request, "review_list.html")

def reviewword(request):
    print("reviewword")

    return render(request, "review_word.html")

def learn_eng_website_list(request):
    return render(request, "learn_eng_website_list.html")