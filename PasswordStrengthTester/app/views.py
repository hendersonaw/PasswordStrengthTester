"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .password import Password

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home',
            'year':datetime.now().year,
        }
    )

## Calculates password strength score
def results(request):

    # Get email and password from POST request:
    form = request.POST
    email = form.get("email")
    pw = Password(form.get("password"))

    # Calculate password strength: 
    pw.CalculateScore()

    # Use HaveIBeenPwned API v3 to determine if email address 
    #   has been involved in a security breach: 

    # Display if user's email address has been compromised: 

    return render(
        request,
        'app/results.html',
        {
            'title':'Results',
            'score':str(pw.strengthScore),
            'message':pw.RankStrengthScore,
            'year':datetime.now().year
        }
    )