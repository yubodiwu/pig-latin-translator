from django.http import HttpResponse
from django.shortcuts import render
from . import helpers

vowels = list('aeiouAEIOU')
consonants = list('bcdfghjklmnopqrstvwxyzBCDFGHJKLMNOPQRSTVWXYZ')

def home(request):
    return render(request, 'home.html')

def translate(request):
    original_text = request.GET['original_text']
    translation = ''

    for word in original_text.split():
        if word[0] in vowels:
            # vowel
            translation += word
            translation += 'way '
        else:
            # consonant
            first_vowel_ind = get_first_vowel_ind(word)

            translation += word[first_vowel_ind:]
            translation += word[0:first_vowel_ind]
            translation += 'ay '

    return render(request, 'translation.html', {
        'original': original_text,
        'translation': translation
    })

def about(request):
    return render(request, 'about.html')

def get_first_vowel_ind(str):
    for i in range(0, len(str)):
        if str[i] in vowels:
            return i

    return None
