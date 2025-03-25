import re

def detect_vulnerabilities(file_path):
    """Scans the file for common security vulnerabilities."""
    vulnerabilities = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        # Scan each line for security issues
        for i, line in enumerate(lines, start=1):
            if re.search(r'gets\s*\(', line):  # Unsafe input function in C
                vulnerabilities.append(("Buffer Overflow", "High", f"Line {i}"))
            if re.search(r'(SELECT|INSERT|DELETE|UPDATE)\s+.*\s+FROM\s+.*\s*WHERE\s+.*=.*"', line, re.IGNORECASE):
                vulnerabilities.append(("SQL Injection", "Medium", f"Line {i}"))
            if re.search(r'system\s*\(.*\)', line):  # Potential command injection
                vulnerabilities.append(("Command Injection", "Critical", f"Line {i}"))
            if re.search(r'("root"|\'root\')\s*[,;]', line):  # Hardcoded credentials
                vulnerabilities.append(("Hardcoded Credentials", "High", f"Line {i}"))

    except Exception as e:
        print(f"Error scanning file: {e}")

    return vulnerabilities
