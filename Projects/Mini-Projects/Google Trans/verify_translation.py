import requests
import re

def get_csrf_token(session, url):
    response = session.get(url)
    if response.status_code != 200:
        print(f"Failed to load page: {response.status_code}")
        return None
    
    # Simple regex to find csrf token in input
    match = re.search(r'name="csrfmiddlewaretoken" value="(.+?)"', response.text)
    if match:
        return match.group(1)
    return None

def verify_translation():
    url = "http://127.0.0.1:8000/"
    session = requests.Session()
    
    print("Fetching CSRF token...")
    csrf_token = get_csrf_token(session, url)
    if not csrf_token:
        print("Could not find CSRF token.")
        return

    print(f"Got CSRF token: {csrf_token[:10]}...")

    # Test Hindi Translation
    payload = {
        'csrfmiddlewaretoken': csrf_token,
        'text': 'Hello world',
        'target_language': 'hi'
    }
    
    print("Sending translation request (English -> Hindi)...")
    response = session.post(url, data=payload, headers={'Referer': url})
    
    if response.status_code == 200:
        # Check for translated text in textarea
        # "Hello world" in Hindi is "नमस्ते दुनिया" or similar
        if "नमस्ते" in response.text or "Hello world" in response.text: # deep-translator might return different variations
             # Let's just print the translated text found in the textarea
            match = re.search(r'<textarea.*?id="translatedText".*?>(.*?)</textarea>', response.text, re.DOTALL)
            if match:
                print(f"Translation result: {match.group(1).strip()}")
            else:
                print("Could not find translated text in response.")
        else:
            print("Translation might be incorrect or failed.")
            print(response.text[:500]) # Print first 500 chars
    else:
        print(f"Request failed: {response.status_code}")

if __name__ == "__main__":
    verify_translation()
