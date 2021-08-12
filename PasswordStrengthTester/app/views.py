"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .password import Password
import pypwned, os, json

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
    emailAddress = form.get("email")
    pw = Password(form.get("password"))

    pw.CalculateScore()     # Calculate password strength

    # Use HaveIBeenPwned API v3 to determine if email address 
    #   has been involved in a security breach: 
    hibp_key = os.environ.get("HIBP_API_KEY")
    pwny = pypwned.pwned(hibp_key)
    statusMessage = pwny.getAllBreachesForAccount(email=emailAddress)

    # TODO: Format statusMessage into human-readable format. 

    # Display if user's email address has been compromised: 

    return render(
        request,
        'app/results.html',
        {
            'title':'Results',
            'score':str(pw.strengthScore),
            'message':pw.RankStrengthScore,
            'statusMessage':statusMessage,
            'year':datetime.now().year
        }
    )