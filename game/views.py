from django.shortcuts import render, redirect
from .forms import PasswordGameForm
from .models import Player
from datetime import datetime

# Define the predetermined password
PREDETERMINED_PASSWORD = "your_predetermined_password"  # Replace with your desired password

# Define the rules for scoring
rules = [
    {"id": 1, "text": "Password must be at least 8 characters", "points": 5, "check": lambda pwd: len(pwd) >= 8},
    {"id": 2, "text": "Must contain a number", "points": 10, "check": lambda pwd: any(c.isdigit() for c in pwd)},
    {"id": 3, "text": "Must contain an uppercase letter", "points": 10, "check": lambda pwd: any(c.isupper() for c in pwd)},
    {"id": 4, "text": "Must contain a special character (!@#$%^&*)", "points": 15, "check": lambda pwd: any(c in "!@#$%^&*" for c in pwd)},
    {"id": 5, "text": "Must contain the word 'password'", "points": 20, "check": lambda pwd: 'password' in pwd.lower()},
    {"id": 6, "text": "Total length must be at least 15 characters", "points": 30, "check": lambda pwd: len(pwd) >= 15},
]

def calculate_score(password):
    score = 0
    for rule in rules:
        if rule["check"](password):
            score += rule["points"]
    return score

def password_game(request):
    if request.method == "POST":
        form = PasswordGameForm(request.POST)
        if form.is_valid():
            player_name = form.cleaned_data['player_name']
            score = calculate_score(PREDETERMINED_PASSWORD)  # Use the predetermined password

            # Save the player's score
            Player.objects.create(name=player_name, score=score)

            # Get the top 10 players
            leaderboard = Player.objects.order_by('-score')[:10]

            return render(request, 'game/game_result.html', {
                'form': form, 'score': score, 'leaderboard': leaderboard
            })
    else:
        form = PasswordGameForm()

    return render(request, 'game/password_game.html', {'form': form})
