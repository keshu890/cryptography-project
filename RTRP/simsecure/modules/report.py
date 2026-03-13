"""
Report Module - Generates security scan reports
"""

import os
from datetime import datetime


def generate_report(scan_type, target, findings, security_score):
    """
    Generate a security scan report and save it to the reports folder.
    
    Args:
        scan_type (str): Type of scan performed (web, port, password)
        target (str): Target of the scan
        findings (list): List of findings from the scan
        security_score (float): Final security score out of 10
    
    Returns:
        str: Path to the generated report file
    """
    try:
        # Create reports directory if it doesn't exist
        reports_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'reports')
        os.makedirs(reports_dir, exist_ok=True)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_filename = f"scan_report_{scan_type}_{timestamp}.txt"
        report_path = os.path.join(reports_dir, report_filename)
        
        # Generate report content
        report_content = generate_report_content(scan_type, target, findings, security_score, timestamp)
        
        # Write report to file
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        return report_path
    
    except Exception as e:
        print(f"Error generating report: {e}")
        return None


def generate_report_content(scan_type, target, findings, security_score, timestamp):
    """
    Generate the formatted content of the security report.
    
    Args:
        scan_type (str): Type of scan
        target (str): Target of the scan
        findings (list): List of findings
        security_score (float): Security score
        timestamp (str): Timestamp of report generation
    
    Returns:
        str: Formatted report content
    """
    report = f"""
================================================================================
                         SIMSECURE SECURITY REPORT
================================================================================

Report Generated: {timestamp}
Tool Version: 1.0
Purpose: Ethical Security Testing for Authorized Targets Only

================================================================================

SCAN DETAILS:
  Scan Type:           {scan_type.upper()}
  Target:              {target}
  Scan Date:           {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

================================================================================

FINDINGS:
"""
    
    if findings:
        for i, finding in enumerate(findings, 1):
            report += f"\n  [{i}] {finding}"
    else:
        report += "\n  No findings detected during this scan."
    
    report += f"""

================================================================================

SECURITY SCORE: {security_score}/10

"""
    
    if security_score >= 8:
        rating = "EXCELLENT - Highly Secure"
    elif security_score >= 6:
        rating = "GOOD - Reasonably Secure"
    elif security_score >= 4:
        rating = "FAIR - Needs Improvement"
    else:
        rating = "POOR - Critical Issues Found"
    
    report += f"Rating: {rating}\n"
    
    report += f"""
================================================================================

DISCLAIMER & LEGAL NOTICE:
  This tool is designed for EDUCATIONAL and AUTHORIZED testing purposes only.
  Unauthorized access to computer networks is illegal.
  The user assumes full responsibility for compliance with applicable laws.
  
================================================================================

For more information and documentation, visit: https://simsecure.example.com

================================================================================
"""
    
    return report
