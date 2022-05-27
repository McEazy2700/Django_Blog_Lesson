from django.shortcuts import render
# Create your views here.

post = [
    {
        'author': 'Eazy',
        'title': 'Test Post',
        'content': 'I love to code',
        'date_added': 'May 28, 2022',
    },
    {
        'author': 'Emmy Sensei',
        'title': 'What\'s for dinner',
        'content': 'I\'m hungry',
        'date_added': 'May 28, 2022',
    }
]

def home(request):
    context = {'posts': post}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})