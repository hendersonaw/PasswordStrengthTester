"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

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
    password = form.get("password")

    # Tests for password strength: 
    

    # Use HaveIBeenPwned API v3 to determine if email address 
    #   has been involved in a security breach: 

    # Display final strength score: 

    # Display if user's email address has been comprimised: 

    return render(
        request,
        'app/results.html',
        {
            'title':'Results',
            'year':datetime.now().year
        }
    )
