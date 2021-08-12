# PasswordStrengthTester
This web server tests the strength of a given password and determines if a given email address has been involved in a security breach. 

## Requires HaveIBeenPwned API v3
This version requires the use of an API key since v2 is no longer supported. 

## Adding API Key to Environment Variable
To add API key to System Environment variable in Windows, 
1. Open Control Panel and search for "environment" in the search bar. Click on "Edit the system environment variables."
2. Under the "Advanced" tab, click on the button labeled "Environment variables..."
3. In the "System variables" section, click "New..."
4. Enter "HIBP_API_KEY" for variable name and *your API key* for the value. 
5. Click "OK." 
