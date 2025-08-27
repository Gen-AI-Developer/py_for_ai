from requests import Response
import requests

def get_response(url: str) -> Response:
    try:
        result = requests.get(url)
    except requests.RequestException as e:
        print(f"Error fetching {url}: {type(e).__name__} with {e}")
        result = Response()
    finally:
        print("Execution completed.")
    return result

def show_response_info(response: Response) -> None:
    print(f"Status Code: {response.status_code}")
    if response.ok:
        print("Response is OK.")
        print(f"OK:", response.ok)
    print(f"Links: {response.links}")
    print(f"Cookies: {response.cookies}")
    print(f"Request Method: {response.request.method}")
    print(f"Encoding: {response.encoding}")
    print(f"Is Redirect: {response.is_redirect}")
    print(f"Headers: {response.headers}")
    print(f"Content: {response.text[:100]}...")  # Print first 100 characters
    print(f"Response URL: {response.url}")
    print(f"Is Permanent Redirect: {response.is_permanent_redirect}")

def main() -> None:
    url = "https://www.google.com"
    response = get_response(url)
    show_response_info(response)

if __name__ == "__main__":
    main()