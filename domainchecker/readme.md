<p>Here's a Python script that takes a domain as input, checks if it's running on WordPress, and outputs "Yes" or "No" accordingly. It also extracts the WordPress version if it's running on WordPress.</p>
![alt text](https://github.com/vit-vivekkumar/domain-checher/edit/main/domainchecker/Screenshot (47).png?raw=true)

```
import requests
import re

!Input domain name
domain = input("Enter a domain name: ")

!Send a GET request to the domain's homepage
response = requests.get(f"https://{domain}")

! Check if WordPress is running on the domain
wordpress_regex = r"wp-(?:content|includes)"
wordpress_match = re.search(wordpress_regex, response.text)

if wordpress_match:
    ! If WordPress is running, output "Yes" and extract the version
    print("Yes")
    version_regex = r"wp-includes/js/wp-emoji-release.min.js\?ver=([\d.]+)"
    version_match = re.search(version_regex, response.text)
    if version_match:
        version = version_match.group(1)
        print(f"WordPress version: {version}")
    else:
        print("WordPress version not found")
else:
    ! If WordPress is not running, output "No"
    print("No")
```

<p>
To check if a domain is running on WordPress, we use a regular expression (wordpress_regex) to search for the presence of "wp-content" or "wp-includes" in the HTML response of the domain's homepage. These two directories are unique to WordPress installations and are almost always present in WordPress sites.

If the regex pattern is found in the HTML response, it's safe to assume that the domain is running on WordPress. We can then extract the WordPress version by searching for a specific string that indicates the version number.
</p>
