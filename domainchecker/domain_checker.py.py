import requests
import re

# Input domain name
domain = input("Enter a domain name: ")

# Send a GET request to the domain's homepage
response = requests.get(f"https://{domain}")

# Check if WordPress is running on the domain
wordpress_regex = r"wp-(?:content|includes)"
wordpress_match = re.search(wordpress_regex, response.text)

if wordpress_match:
    # If WordPress is running, output "Yes" and extract the version
    print("Yes")
    version_regex = r"wp-includes/js/wp-emoji-release.min.js\?ver=([\d.]+)"
    version_match = re.search(version_regex, response.text)
    if version_match:
        version = version_match.group(1)
        print(f"WordPress version: {version}")
    else:
        print("WordPress version not found")
else:
    # If WordPress is not running, output "No"
    print("No")
