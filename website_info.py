import requests

def get_website_info(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)

        # Print the URL and its status code
        print(f"URL: {url}")
        print(f"Status Code: {response.status_code}")

        # Print the response headers
        print("Response Headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")

        # Check if the server is running PHP
        if 'php' in response.headers.get('X-Powered-By', '').lower():
            print("The website is running PHP.")
        else:
            print("The website is not running PHP.")

        # Optional: Print the first 500 characters of the response body
        print("\nResponse Body (first 500 characters):")
        print(response.text[:500])

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")

if __name__ == "__main__":
    website_url = "http://localhost:8081/shop-banhang/"  # Replace with your target website
    get_website_info(website_url)
