"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from requests.exceptions import RequestException
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

def results(request):
    """Calculates password strength score."""
    assert isinstance(request, HttpRequest)

    # Get email and password from POST request:
    form = request.POST
    emailAddress = form.get("email")
    pw = Password(form.get("password"))

    pw.CalculateScore()     # Calculate password strength

    # Use HaveIBeenPwned API v3 to determine if email address 
    #   has been involved in a security breach: 
    hibp_key = os.environ.get("HIBP_API_KEY")
    pwny = pypwned.pwned(hibp_key)
    try:
        apiMessage = pwny.getAllBreachesForAccount(email=emailAddress)
    except RequestException:
        apiMessage = "Sorry, could not reach HaveIBeenPwned servers. Make sure your Internet connection is stable and try again."

    # TODO: Format statusMessage into human-readable format. 
    if type(apiMessage) is str:
        statusMessage = apiMessage
    else:
        statusMessage = "| "
        for apiData in apiMessage:
            statusMessage += apiData['Name'] + " | "

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

def passwordRequirements(request):
    """Renders the password requirements page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/password-requirements.html',
        {
            'title':'Password Requirements',
            'year':datetime.now().year,
        }
    )