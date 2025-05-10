from django.shortcuts import render, redirect
from .wordlist import get_random_word

def index(request):
    if 'word' not in request.session:
        request.session['word'] = get_random_word()
        request.session['guesses'] = []
        request.session['lives'] = 6

    word = request.session['word']
    guesses = request.session['guesses']
    lives = request.session['lives']

    display_word = ' '.join([letter if letter in guesses else '_' for letter in word])
    is_won = set(word).issubset(set(guesses))

    if lives <= 0 or is_won:
        return redirect('result')

    if request.method == 'POST':
        letter = request.POST.get('letter', '').upper()
        if letter and letter not in guesses:
            guesses.append(letter)
            if letter not in word:
                lives -= 1

        request.session['guesses'] = guesses
        request.session['lives'] = lives

    return render(request, 'game/game.html', {
        'display_word': display_word,
        'guesses': guesses,
        'lives': lives,
    })

def result(request):
    word = request.session.get('word')
    lives = request.session.get('lives')
    is_won = lives > 0

    context = {'word': word, 'is_won': is_won}
    request.session.flush()
    return render(request, 'game/result.html', context)
