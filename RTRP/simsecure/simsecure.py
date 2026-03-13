#!/usr/bin/env python3
"""
SimSecure - Professional Cybersecurity Command-Line Tool
A comprehensive ethical security testing utility for authorized security assessments.

License: MIT
Version: 1.0
Author: Security Research Team
"""

import sys
import argparse
import os
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored output
init(autoreset=True)

# Import modules
from modules.web_scan import scan_website
from modules.port_scan import scan_ports
from modules.password_test import test_password
from modules.report import generate_report


def print_banner():
    """
    Display the SimSecure banner and welcome message.
    """
    banner = f"""
{Fore.CYAN}
{'='*79}
{'|':<79}|
|                        {Fore.YELLOW}SIMSECURE v1.0{Fore.CYAN}                              |
|                  {Fore.WHITE}Ethical Security Testing Tool{Fore.CYAN}                   |
|          {Fore.WHITE}For Educational and Authorized Use Only{Fore.CYAN}                 |
{'|':<79}|
{'='*79}
{Style.RESET_ALL}
"""
    print(banner)


def print_disclaimer():
    """
    Display important legal and ethical disclaimer.
    """
    disclaimer = f"""
{Fore.YELLOW}
*** IMPORTANT DISCLAIMER ***
{Fore.WHITE}
This tool is designed for EDUCATIONAL and AUTHORIZED testing purposes only.
Unauthorized access to computer networks is ILLEGAL and subject to prosecution.

By using this tool, you accept full responsibility for:
  - Compliance with applicable laws and regulations
  - Obtaining written authorization before testing any target
  - All consequences of your actions

Misuse can result in criminal charges and civil penalties.

{Style.RESET_ALL}
"""
    print(disclaimer)


def handle_web_scan(args):
    """
    Handle website security scanning command.
    
    Args:
        args: Parsed command-line arguments
    """
    try:
        url = args.target
        score, findings = scan_website(url)
        
        # Generate report if requested
        if args.report:
            report_path = generate_report('WEB', url, findings, score)
            if report_path:
                print(f"\n{Fore.GREEN}[+] Report saved to: {report_path}{Style.RESET_ALL}")
    
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Scan interrupted by user{Style.RESET_ALL}")
        sys.exit(130)
    except Exception as e:
        print(f"{Fore.RED}[!] Error during web scan: {str(e)}{Style.RESET_ALL}")
        sys.exit(1)


def handle_port_scan(args):
    """
    Handle port scanning command.
    
    Args:
        args: Parsed command-line arguments
    """
    try:
        host = args.target
        score, findings = scan_ports(host)
        
        # Generate report if requested
        if args.report:
            report_path = generate_report('PORT', host, findings, score)
            if report_path:
                print(f"\n{Fore.GREEN}[+] Report saved to: {report_path}{Style.RESET_ALL}")
    
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Scan interrupted by user{Style.RESET_ALL}")
        sys.exit(130)
    except Exception as e:
        print(f"{Fore.RED}[!] Error during port scan: {str(e)}{Style.RESET_ALL}")
        sys.exit(1)


def handle_password_test(args):
    """
    Handle password security testing command.
    
    Args:
        args: Parsed command-line arguments
    """
    try:
        password = args.password
        score, findings = test_password(password)
        
        # Generate report if requested
        if args.report:
            report_path = generate_report('PASSWORD', '[User Password Test]', findings, score)
            if report_path:
                print(f"\n{Fore.GREEN}[+] Report saved to: {report_path}{Style.RESET_ALL}")
    
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Test interrupted by user{Style.RESET_ALL}")
        sys.exit(130)
    except Exception as e:
        print(f"{Fore.RED}[!] Error during password test: {str(e)}{Style.RESET_ALL}")
        sys.exit(1)


def print_menu():
    """
    Display interactive menu for selecting security scans.
    """
    menu = f"""
{Fore.CYAN}
=== SIMSECURE SECURITY SCANNER ===
{Style.RESET_ALL}
Available Security Checks:

  {Fore.GREEN}1{Style.RESET_ALL}) Website Security Scanner
     - Check HTTPS, security headers, vulnerabilities
     - Example: https://example.com

  {Fore.GREEN}2{Style.RESET_ALL}) Port Scanner
     - Scan open ports on target host
     - Example: example.com or 192.168.1.1

  {Fore.GREEN}3{Style.RESET_ALL}) Password Strength Tester
     - Analyze password security strength
     - Example: MyPassword123!

  {Fore.GREEN}4{Style.RESET_ALL}) Help & Examples
     - Display detailed help information

  {Fore.GREEN}5{Style.RESET_ALL}) Exit

{Fore.YELLOW}Select an option (1-5):{Style.RESET_ALL} """
    return menu


def interactive_mode():
    """
    Run SimSecure in interactive menu mode.
    """
    while True:
        try:
            print_banner()
            
            choice = input(print_menu()).strip()
            
            if choice == '1':
                # Website Scanner
                print(f"\n{Fore.CYAN}[*] Website Security Scanner{Style.RESET_ALL}")
                url = input(f"{Fore.YELLOW}Enter URL (e.g., https://example.com): {Style.RESET_ALL}").strip()
                
                if not url:
                    print(f"{Fore.RED}[!] URL cannot be empty{Style.RESET_ALL}\n")
                    continue
                
                save_report = input(f"{Fore.YELLOW}Save report? (y/n): {Style.RESET_ALL}").strip().lower() == 'y'
                
                # Simulate argparse object
                class Args:
                    target = url
                    report = save_report
                
                handle_web_scan(Args())
                input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
            
            elif choice == '2':
                # Port Scanner
                print(f"\n{Fore.CYAN}[*] Port Scanner{Style.RESET_ALL}")
                host = input(f"{Fore.YELLOW}Enter hostname or IP (e.g., example.com): {Style.RESET_ALL}").strip()
                
                if not host:
                    print(f"{Fore.RED}[!] Hostname cannot be empty{Style.RESET_ALL}\n")
                    continue
                
                save_report = input(f"{Fore.YELLOW}Save report? (y/n): {Style.RESET_ALL}").strip().lower() == 'y'
                
                class Args:
                    target = host
                    report = save_report
                
                handle_port_scan(Args())
                input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
            
            elif choice == '3':
                # Password Tester
                print(f"\n{Fore.CYAN}[*] Password Strength Tester{Style.RESET_ALL}")
                password = input(f"{Fore.YELLOW}Enter password to test: {Style.RESET_ALL}").strip()
                
                if not password:
                    print(f"{Fore.RED}[!] Password cannot be empty{Style.RESET_ALL}\n")
                    continue
                
                save_report = input(f"{Fore.YELLOW}Save report? (y/n): {Style.RESET_ALL}").strip().lower() == 'y'
                
                class Args:
                    password = password
                    report = save_report
                
                handle_password_test(Args())
                input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
            
            elif choice == '4':
                # Help
                print_help_menu()
                input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
            
            elif choice == '5':
                # Exit
                print(f"\n{Fore.GREEN}[+] Thank you for using SimSecure!{Style.RESET_ALL}\n")
                sys.exit(0)
            
            else:
                print(f"{Fore.RED}[!] Invalid choice. Please select 1-5{Style.RESET_ALL}\n")
        
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}[!] Interrupted by user{Style.RESET_ALL}\n")
            sys.exit(130)
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {str(e)}{Style.RESET_ALL}\n")


def print_help_menu():
    """
    Print detailed help information.
    """
    help_text = f"""
{Fore.CYAN}
=== SIMSECURE HELP ===
{Style.RESET_ALL}

COMMAND LINE USAGE:
  simsecure [COMMAND] [TARGET] [OPTIONS]

COMMANDS:
  web [URL]              Scan website security headers
  port [HOST]            Scan open ports on target
  password [PASS]        Test password strength
  -ls, --list            List all available commands
  -h, --help             Show this help message
  version                Show version information
  disclaimer             Show legal disclaimer

EXAMPLES:
  simsecure web https://example.com
  simsecure web example.com --report
  simsecure port example.com --report
  simsecure password "MyPass#123" --report
  simsecure -ls
  simsecure -h

INTERACTIVE MODE:
  Run 'simsecure' with no arguments to enter interactive menu

OPTIONS:
  --report               Generate and save a security report

SECURITY SCORING:
  Password (0-10):       0-5=Weak, 6-8=Strong, 9-10=Excellent
  Port Scan (0-10):      10=No risks, 4=Many open ports
  Web Scan (0-10):       10=Secure, 0=Multiple vulnerabilities

REPORTS:
  Reports are saved in: reports/ folder with timestamps
  View reports with: cat reports/scan_report_*.txt

For more info: simsecure disclaimer
"""
    print(help_text)


def main():
    """
    Main entry point for SimSecure CLI tool.
    """
    # Print banner
    print_banner()
    
    # Create argument parser
    parser = argparse.ArgumentParser(
        description='SimSecure - Professional Cybersecurity Command-Line Tool',
        epilog="""
Examples:
  simsecure                          # Interactive menu mode
  simsecure -ls                      # List all commands
  simsecure web https://example.com  # Scan website
  simsecure port example.com         # Scan ports
  simsecure password "Pass#123"      # Test password
  simsecure password "Pass#123" --report  # Test with report
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Add list commands option
    parser.add_argument(
        '-ls', '--list',
        action='store_true',
        help='List all available security checks'
    )
    
    # Create subcommands
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # WEB sub-command
    web_parser = subparsers.add_parser('web', help='Scan website for security issues')
    web_parser.add_argument(
        'target',
        help='URL to scan (e.g., https://example.com or example.com)'
    )
    web_parser.add_argument(
        '--report',
        action='store_true',
        help='Generate and save a report file'
    )
    web_parser.set_defaults(func=handle_web_scan)
    
    # PORT sub-command
    port_parser = subparsers.add_parser('port', help='Scan ports on target host')
    port_parser.add_argument(
        'target',
        help='Hostname or IP address to scan (e.g., example.com or 192.168.1.1)'
    )
    port_parser.add_argument(
        '--report',
        action='store_true',
        help='Generate and save a report file'
    )
    port_parser.set_defaults(func=handle_port_scan)
    
    # PASSWORD sub-command
    password_parser = subparsers.add_parser('password', help='Test password strength')
    password_parser.add_argument(
        'password',
        help='Password to test (enclose in quotes if contains spaces)'
    )
    password_parser.add_argument(
        '--report',
        action='store_true',
        help='Generate and save a report file'
    )
    password_parser.set_defaults(func=handle_password_test)
    
    # VERSION sub-command
    version_parser = subparsers.add_parser('version', help='Show version information')
    version_parser.set_defaults(func=lambda args: print(f"{Fore.CYAN}SimSecure v1.0{Style.RESET_ALL}"))
    
    # DISCLAIMER sub-command
    disclaimer_parser = subparsers.add_parser('disclaimer', help='Show legal disclaimer')
    disclaimer_parser.set_defaults(func=lambda args: print_disclaimer())
    
    # Parse arguments
    args = parser.parse_args()
    
    # Handle --list flag
    if args.list:
        print(f"\n{Fore.CYAN}=== AVAILABLE SECURITY CHECKS ==={Style.RESET_ALL}\n")
        print(f"{Fore.GREEN}1. Website Security Scanner{Style.RESET_ALL}")
        print(f"   - Checks HTTPS, security headers, CSP, XSS protection")
        print(f"   - Usage: simsecure web https://example.com [--report]\n")
        
        print(f"{Fore.GREEN}2. Port Scanner{Style.RESET_ALL}")
        print(f"   - Scans 17 common ports for open services")
        print(f"   - Usage: simsecure port example.com [--report]\n")
        
        print(f"{Fore.GREEN}3. Password Strength Tester{Style.RESET_ALL}")
        print(f"   - Analyzes password security strength (0-10 score)")
        print(f"   - Usage: simsecure password \"YourPassword\" [--report]\n")
        
        print(f"{Fore.YELLOW}Add --report flag to generate security reports\n{Style.RESET_ALL}")
        return
    
    # Show interactive menu if no command provided
    if not args.command:
        interactive_mode()
        return
    
    # Execute the appropriate function
    try:
        if hasattr(args, 'func'):
            args.func(args)
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Operation cancelled by user{Style.RESET_ALL}")
        sys.exit(130)
    except Exception as e:
        print(f"{Fore.RED}[!] Unexpected error: {str(e)}{Style.RESET_ALL}")
        sys.exit(1)


if __name__ == '__main__':
    main()
