"""
Password Security Tester Module - Analyzes password strength
"""

import re
from colorama import Fore, Style


def test_password(password):
    """
    Analyze password strength and security.
    
    Args:
        password (str): Password to test
    
    Returns:
        tuple: (security_score, findings_list)
    """
    findings = []
    score = 0
    
    print(f"\n{Fore.CYAN}[*] Analyzing Password Strength{Style.RESET_ALL}")
    print("-" * 70)
    
    # Rule 1: Minimum length (≥ 8 characters)
    if len(password) >= 8:
        print(f"{Fore.GREEN}[+] Password Length: PASS (Length: {len(password)} characters){Style.RESET_ALL}")
        findings.append(f"Password length is adequate ({len(password)} characters)")
        score += 2
    else:
        print(f"{Fore.RED}[-] Password Length: FAIL (Length: {len(password)} characters, minimum 8 required){Style.RESET_ALL}")
        findings.append(f"Password is too short ({len(password)} characters, minimum 8 required)")
    
    # Rule 2: Contains uppercase letters
    if re.search(r'[A-Z]', password):
        print(f"{Fore.GREEN}[+] Uppercase Letters: PASS{Style.RESET_ALL}")
        findings.append("Contains uppercase letters")
        score += 2
    else:
        print(f"{Fore.YELLOW}[!] Uppercase Letters: MISSING{Style.RESET_ALL}")
        findings.append("Does not contain uppercase letters (A-Z)")
    
    # Rule 3: Contains lowercase letters
    if re.search(r'[a-z]', password):
        print(f"{Fore.GREEN}[+] Lowercase Letters: PASS{Style.RESET_ALL}")
        findings.append("Contains lowercase letters")
        score += 2
    else:
        print(f"{Fore.YELLOW}[!] Lowercase Letters: MISSING{Style.RESET_ALL}")
        findings.append("Does not contain lowercase letters (a-z)")
    
    # Rule 4: Contains numbers
    if re.search(r'[0-9]', password):
        print(f"{Fore.GREEN}[+] Numbers: PASS{Style.RESET_ALL}")
        findings.append("Contains numeric characters")
        score += 2
    else:
        print(f"{Fore.YELLOW}[!] Numbers: MISSING{Style.RESET_ALL}")
        findings.append("Does not contain numeric characters (0-9)")
    
    # Rule 5: Contains special characters
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'"\\|,.<>\/?]', password):
        print(f"{Fore.GREEN}[+] Special Characters: PASS{Style.RESET_ALL}")
        findings.append("Contains special characters")
        score += 2
    else:
        print(f"{Fore.YELLOW}[!] Special Characters: MISSING{Style.RESET_ALL}")
        findings.append("Does not contain special characters")
    
    # Bonus: Very long password (≥ 16 characters)
    if len(password) >= 16:
        print(f"{Fore.GREEN}[+] BONUS: Very Strong Length (16+ characters){Style.RESET_ALL}")
        findings.append("Bonus: Excellent password length (16+ characters)")
        score = min(score + 1, 10)  # Cap at 10
    
    print("-" * 70)
    
    # Normalize score to 0-10
    final_score = min(score, 10)
    
    # Determine strength rating
    if final_score >= 9:
        strength = "EXCELLENT"
        color = Fore.GREEN
    elif final_score >= 7:
        strength = "STRONG"
        color = Fore.GREEN
    elif final_score >= 5:
        strength = "MODERATE"
        color = Fore.YELLOW
    elif final_score >= 3:
        strength = "WEAK"
        color = Fore.YELLOW
    else:
        strength = "VERY WEAK"
        color = Fore.RED
    
    print(f"\n{Fore.CYAN}Overall Password Strength: {color}{strength}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Security Score: {Fore.YELLOW}{final_score}/10{Style.RESET_ALL}")
    
    # Recommendations
    print(f"\n{Fore.CYAN}Recommendations:{Style.RESET_ALL}")
    if len(password) < 8:
        print(f"  {Fore.YELLOW}• Increase password length to at least 8 characters{Style.RESET_ALL}")
    if not re.search(r'[A-Z]', password):
        print(f"  {Fore.YELLOW}• Add uppercase letters (A-Z){Style.RESET_ALL}")
    if not re.search(r'[a-z]', password):
        print(f"  {Fore.YELLOW}• Add lowercase letters (a-z){Style.RESET_ALL}")
    if not re.search(r'[0-9]', password):
        print(f"  {Fore.YELLOW}• Add numbers (0-9){Style.RESET_ALL}")
    if not re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'"\\|,.<>\/?]', password):
        print(f"  {Fore.YELLOW}• Add special characters (!@#$%^&* etc.){Style.RESET_ALL}")
    if final_score >= 9:
        print(f"  {Fore.GREEN}• Excellent security! Keep this password safe and unique.{Style.RESET_ALL}")
    
    return final_score, findings
