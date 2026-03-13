"""
Web Scanner Module - Performs website security checks
"""

import requests
from urllib.parse import urlparse
from colorama import Fore, Style


def scan_website(url):
    """
    Perform comprehensive website security scan.
    
    Args:
        url (str): URL to scan (e.g., https://example.com)
    
    Returns:
        tuple: (security_score, findings_list)
    """
    findings = []
    score = 0
    
    # Validate and normalize URL
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    try:
        # Set timeout for request
        headers = {
            'User-Agent': 'SimSecure/1.0 (Security Scanner)'
        }
        
        print(f"\n{Fore.CYAN}[*] Scanning Website: {url}{Style.RESET_ALL}")
        print("-" * 70)
        
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
        response_headers = response.headers
        
        # Check 1: HTTPS Enabled
        if url.startswith('https://'):
            print(f"{Fore.GREEN}[+] HTTPS: Enabled{Style.RESET_ALL}")
            findings.append("HTTPS is enabled - Secure connection established")
            score += 2
        else:
            print(f"{Fore.RED}[-] HTTPS: Disabled (Insecure){Style.RESET_ALL}")
            findings.append("WARNING: HTTPS is not enabled - Unencrypted connection")
        
        # Check 2: X-Frame-Options (Clickjacking protection)
        frame_options = response_headers.get('X-Frame-Options', 'Missing')
        if frame_options != 'Missing':
            print(f"{Fore.GREEN}[+] X-Frame-Options: Present ({frame_options}){Style.RESET_ALL}")
            findings.append(f"X-Frame-Options header present: {frame_options}")
            score += 1
        else:
            print(f"{Fore.YELLOW}[!] X-Frame-Options: Missing{Style.RESET_ALL}")
            findings.append("WARNING: X-Frame-Options header is missing (vulnerable to clickjacking)")
        
        # Check 3: Content-Security-Policy
        csp = response_headers.get('Content-Security-Policy', 'Missing')
        if csp != 'Missing':
            print(f"{Fore.GREEN}[+] Content-Security-Policy: Present{Style.RESET_ALL}")
            findings.append("Content-Security-Policy header is present")
            score += 2
        else:
            print(f"{Fore.YELLOW}[!] Content-Security-Policy: Missing{Style.RESET_ALL}")
            findings.append("WARNING: Content-Security-Policy header is missing (vulnerable to XSS)")
        
        # Check 4: X-XSS-Protection
        xss_protection = response_headers.get('X-XSS-Protection', 'Missing')
        if xss_protection != 'Missing':
            print(f"{Fore.GREEN}[+] X-XSS-Protection: Present{Style.RESET_ALL}")
            findings.append(f"X-XSS-Protection header present: {xss_protection}")
            score += 1
        else:
            print(f"{Fore.YELLOW}[!] X-XSS-Protection: Missing{Style.RESET_ALL}")
            findings.append("WARNING: X-XSS-Protection header is missing")
        
        # Check 5: Strict-Transport-Security (HSTS)
        hsts = response_headers.get('Strict-Transport-Security', 'Missing')
        if hsts != 'Missing':
            print(f"{Fore.GREEN}[+] Strict-Transport-Security: Present{Style.RESET_ALL}")
            findings.append(f"HSTS header present: {hsts}")
            score += 2
        else:
            if url.startswith('https://'):
                print(f"{Fore.YELLOW}[!] Strict-Transport-Security: Missing{Style.RESET_ALL}")
                findings.append("WARNING: HSTS header is missing (no protection against downgrade attacks)")
        
        # Check 6: Server Information Leakage
        server_header = response_headers.get('Server', 'Not detected')
        if server_header != 'Not detected':
            print(f"{Fore.YELLOW}[!] Server Header: {server_header} (Information leakage){Style.RESET_ALL}")
            findings.append(f"Server information leaked: {server_header}")
        else:
            print(f"{Fore.GREEN}[+] Server Header: Not detected (Good){Style.RESET_ALL}")
            findings.append("Server header is not disclosed")
            score += 1
        
        # Check 7: X-Content-Type-Options
        content_type_options = response_headers.get('X-Content-Type-Options', 'Missing')
        if content_type_options == 'nosniff':
            print(f"{Fore.GREEN}[+] X-Content-Type-Options: nosniff{Style.RESET_ALL}")
            findings.append("X-Content-Type-Options header properly configured")
            score += 1
        else:
            print(f"{Fore.YELLOW}[!] X-Content-Type-Options: Missing or Incorrect{Style.RESET_ALL}")
            findings.append("WARNING: X-Content-Type-Options header missing or incorrect")
        
        print("-" * 70)
        
        # Normalize score to 0-10 range
        max_score = 10
        final_score = min(score, max_score)
        
        print(f"\n{Fore.CYAN}Security Score: {Fore.YELLOW}{final_score}/10{Style.RESET_ALL}")
        
        return final_score, findings
    
    except requests.exceptions.MissingSchema:
        print(f"{Fore.RED}[!] Invalid URL: Missing schema (http:// or https://){Style.RESET_ALL}")
        findings.append("ERROR: Invalid URL format - missing http:// or https://")
        return 0, findings
    
    except requests.exceptions.ConnectionError:
        print(f"{Fore.RED}[!] Connection Error: Unable to reach {url}{Style.RESET_ALL}")
        findings.append(f"ERROR: Could not connect to {url}")
        return 0, findings
    
    except requests.exceptions.Timeout:
        print(f"{Fore.RED}[!] Timeout: Request took too long{Style.RESET_ALL}")
        findings.append("ERROR: Request timeout - server did not respond in time")
        return 0, findings
    
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}[!] Request Error: {str(e)}{Style.RESET_ALL}")
        findings.append(f"ERROR: {str(e)}")
        return 0, findings
