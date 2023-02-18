import requests
import re

from django.shortcuts import render

# Create your views here.
def home(request):
	domain = ""
	isWordpress = ""
	ver = ""
	if request.method == 'POST':
		domain = request.POST['domain']
		# Send a GET request to the domain's homepage
		response = requests.get(f"https://{domain}")

		# Check if WordPress is running on the domain
		wordpress_regex = r"wp-(?:content|includes)"
		wordpress_match = re.search(wordpress_regex, response.text)

		if wordpress_match:
		    # If WordPress is running, output "Yes" and extract the version
		    isWordpress= "Yes"
		    version_regex = r"wp-includes/js/wp-emoji-release.min.js\?ver=([\d.]+)"
		    version_match = re.search(version_regex, response.text)
		    if version_match:
		        version = version_match.group(1)
		        ver=f"WordPress version: {version}"
		    else:
		        ver="WordPress version not found"
		else:
		    # If WordPress is not running, output "No"
		    isWordpress="No"    
	return render(request, 'index.html' ,{'domain': domain,'isWordpress': isWordpress,'ver': ver})

