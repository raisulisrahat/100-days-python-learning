# Here I am showing Problem Solve Day 7

# Web Application Scanning:
# Build a web application scanner using Scapy to discover web applications by analyzing network traffic. Use Requests to interact with these web applications, test for vulnerabilities, and log findings.

import requests
from bs4 import BeautifulSoup

# List of common web application paths
common_paths = [
    "/admin", "/login", "/wp-admin", "/phpmyadmin",
]

# Target URL to scan
target_url = "https://ctsolutionbd.com"

# Initialize a session
session = requests.Session()

def discover_web_applications(base_url, paths):
    discovered_apps = {}
    
    for path in paths:
        url = base_url + path
        response = session.get(url)
        
        if response.status_code == 200:
            # Check if it's a common CMS (e.g., WordPress)
            if "wp-content" in response.text:
                discovered_apps["WordPress"] = url
            # You can add more checks for other CMS, frameworks, or web apps
            
            # Log findings
            print(f"Discovered: {url}")
    
    return discovered_apps

def scan_for_vulnerabilities(apps_to_scan):
    for app_name, app_url in apps_to_scan.items():
        # Here, you can perform various vulnerability scans using Requests
        # For example, you can check for common vulnerabilities like SQL injection, XSS, CSRF, etc.
        
        # Log vulnerability testing results
        print(f"Vulnerability testing results for {app_name} at {app_url}:")

if __name__ == "__main__":
    discovered_apps = discover_web_applications(target_url, common_paths)
    if discovered_apps:
        scan_for_vulnerabilities(discovered_apps)
    else:
        print("No web applications discovered.")
