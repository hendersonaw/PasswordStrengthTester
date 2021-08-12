__author__ = 'Aaron Henderson'

import requests

class OldPwned:
    """Determines if a given email has been involved in a security breach."""

    def _init__(self):
        self.API_KEY = "MY HIBP KEY"
        self.headers = {'hibp-api-key':self.API_KEY}

    def getAllBreachesForAccount(self, email):
        """Determines if a specific email has been involved in a security breach."""
        r = requests.get("https://haveibeenpwned.com/api/v3/breaches/" + email, verify=True)
        
        if r.status_code == 400:
            return "Bad request - the account does not comply with an acceptable format (i.e., it's an empty string)."
        elif r.status_code == 401:
            return "Unauthorised - either no API key was provided or is wasn't valid."
        elif r.status_code == 403:
            return "Forbidden - no user agent has specified the request."
        elif r.status_code == 404:
            return r.json()
            #return "Not found - the account could not be found and has therefore not been pwned."
        elif r.status_code == 429:
            return "Too many requests - the rate limit has been exceeded."
        elif r.status_code == 503:
            return "Service unavailable - usually returned by Cloudflare if the underlying service is unavailable."
        else:
            return r.json()