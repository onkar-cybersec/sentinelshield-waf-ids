# SentinelShield: Advanced Intrusion Detection & Web Protection System

## Project Overview

SentinelShield is a lightweight Intrusion Detection and Web Protection System built using Python Flask. The project simulates the behavior of a basic Web Application Firewall by inspecting incoming HTTP requests, detecting malicious payloads, applying rate limiting, logging security events, and displaying results through a dashboard.

This project was developed as a practical cybersecurity internship project to understand how request inspection, attack detection, logging, alert generation, and dashboard monitoring work in real-world security systems.

## Architecture Diagram

![SentinelShield Architecture Diagram](architecture/architecture-diagram.jpg)

## Objectives

* Inspect HTTP request parameters for suspicious input.
* Detect common web attack patterns using rule-based signatures.
* Block malicious requests before they are processed further.
* Monitor repeated requests using IP-based rate limiting.
* Generate logs containing timestamp, IP address, input, result, and detection category.
* Display allowed and blocked requests through a simple security dashboard.
* Demonstrate the workflow of detection, decision, logging, and dashboard visibility.

## Features

* HTTP request inspection
* SQL Injection detection
* Cross-Site Scripting detection
* Directory Traversal / LFI detection
* Command Injection detection
* IP-based rate limiting
* Security event logging
* Dashboard summary
* Output encoding fix for dashboard log safety

## Tools and Technologies Used

* Python 3
* Flask
* HTML
* Parrot OS
* VirtualBox
* Browser-based testing
* Linux terminal
* GitHub documentation

## Project Structure

```text
SentinelShield/
├── architecture/
│   └── architecture-notes.txt
├── logs/
│   └── sentinelshield.log
├── screenshots/
├── src/
│   └── app.py
├── test-payloads/
│   ├── command-injection.txt
│   ├── lfi-directory-traversal.txt
│   ├── normal-requests.txt
│   ├── sql-injection.txt
│   └── xss.txt
├── requirements.txt
└── README.md
```

## How the System Works

1. A user submits input through the web form.
2. The Flask application receives the HTTP request.
3. The request inspector extracts the input parameter.
4. The detection engine compares the input against predefined attack signatures.
5. The rate limiter checks whether the same IP address has exceeded the allowed request threshold.
6. The decision engine allows, blocks, or flags the request.
7. The event is written into the log file.
8. The dashboard displays total requests, allowed requests, blocked requests, and security logs.

## Detection Categories

| Attack Type               | Example Payload                        |
| ------------------------- | -------------------------------------- |
| SQL Injection             | `' OR '1'='1`                          |
| XSS                       | `<script>alert(1)</script>`            |
| Directory Traversal / LFI | `../../../../etc/passwd`               |
| Command Injection         | `test; whoami`                         |
| Rate Limit Abuse          | More than 5 requests within 60 seconds |

## Setup Instructions

Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
cd src
python app.py
```

Open the application in browser:

```text
http://127.0.0.1:5000
```

Open the dashboard:

```text
http://127.0.0.1:5000/dashboard
```

## Testing Summary

The system was tested using normal inputs and malicious payloads. Normal requests were allowed, while malicious requests were blocked and logged.

| Test Case                         | Result                  |
| --------------------------------- | ----------------------- |
| Normal request                    | Allowed                 |
| SQL Injection payload             | Blocked                 |
| XSS payload                       | Blocked                 |
| Directory Traversal / LFI payload | Blocked                 |
| Command Injection payload         | Blocked                 |
| Repeated requests                 | Blocked by rate limiter |

## Screenshots / Evidence

| Screenshot | Description |
|---|---|
| `01_basic_web_app.jpg` | Basic SentinelShield web application running |
| `02_sql_injection_blocked.jpg` | SQL Injection payload blocked |
| `03_xss_blocked.jpg` | XSS payload blocked |
| `04_lfi_blocked.jpg` | Directory Traversal / LFI payload blocked |
| `05_command_injection_blocked.jpg` | Command Injection payload blocked |
| `06_rate_limit_blocked.jpg` | Rate limiting triggered |
| `07_log_file.jpg` | Security log entries generated |
| `09_dashboard_xss_fixed.jpg` | Dashboard safely displays XSS payload as text |

## Security Improvement

During dashboard testing, a stored XSS issue was identified because raw log entries were displayed directly in the browser. This was fixed by applying HTML escaping before rendering log data.

This improvement ensures that malicious payloads appear as plain text in the dashboard instead of executing as JavaScript.

## Conclusion

SentinelShield successfully demonstrates a simplified but practical workflow of a Web Application Firewall and Intrusion Detection System. It inspects requests, detects malicious patterns, applies rate limiting, logs events, and displays security activity through a dashboard. The project helped build hands-on understanding of web request analysis, signature-based detection, traffic behavior monitoring, and secure dashboard rendering.
