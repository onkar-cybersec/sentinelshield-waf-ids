# Final Report

## SentinelShield: Advanced Intrusion Detection & Web Protection System

## 1. Project Overview

SentinelShield is a simplified Intrusion Detection and Web Protection System developed using Python Flask. The system simulates the working behavior of a lightweight Web Application Firewall by inspecting incoming HTTP requests, detecting malicious payloads, applying rate limiting, generating logs, and displaying security events through a dashboard.

The project was built and tested in a Parrot OS virtual lab environment and documented on Windows for final submission and GitHub presentation.

## 2. Project Objectives

The main objectives of this project were:

* To understand how Web Application Firewalls inspect HTTP requests.
* To detect common web attack patterns using predefined rules.
* To block malicious or abusive requests.
* To monitor traffic behavior using rate limiting.
* To generate security logs for analysis.
* To display detected activity through a dashboard.
* To document practical testing, observations, and improvements.

## 3. System Components

| Component                   | Description                               |
| --------------------------- | ----------------------------------------- |
| Flask Web Application       | Handles incoming web requests             |
| Request Inspector           | Extracts and analyzes user input          |
| Rule-Based Detection Engine | Matches input against attack signatures   |
| Rate Limiter                | Tracks repeated requests from the same IP |
| Decision Engine             | Allows or blocks requests                 |
| Logging System              | Stores security events                    |
| Dashboard                   | Displays request summary and logs         |

## 4. Attack Categories Tested

The following attack categories were tested during practical work:

| Attack Category           | Example Payload                    | Result  |
| ------------------------- | ---------------------------------- | ------- |
| SQL Injection             | `' OR '1'='1`                      | Blocked |
| XSS                       | `<script>alert(1)</script>`        | Blocked |
| Directory Traversal / LFI | `../../../../etc/passwd`           | Blocked |
| Command Injection         | `test; whoami`                     | Blocked |
| Rate Limit Abuse          | More than 5 requests in 60 seconds | Blocked |
| Normal Request            | `hello`                            | Allowed |

## 5. Detection Results

| Test Type                         | Expected Result       | Actual Result | Status |
| --------------------------------- | --------------------- | ------------- | ------ |
| Normal input                      | Allowed               | Allowed       | Pass   |
| SQL Injection payload             | Blocked               | Blocked       | Pass   |
| XSS payload                       | Blocked               | Blocked       | Pass   |
| Directory Traversal / LFI payload | Blocked               | Blocked       | Pass   |
| Command Injection payload         | Blocked               | Blocked       | Pass   |
| Repeated requests                 | Blocked by rate limit | Blocked       | Pass   |

## 6. Total Attacks Performed

During testing, the following attack attempts were performed:

| Category                  | Number of Main Tests |
| ------------------------- | -------------------: |
| SQL Injection             |                    1 |
| XSS                       |                    1 |
| Directory Traversal / LFI |                    1 |
| Command Injection         |                    1 |
| Rate Limit Abuse          |                    1 |
| Normal Request Test       |                    1 |

Additional payloads were also documented inside the `test-payloads` folder for repeatable testing.

## 7. Detection Accuracy

For the tested payloads, SentinelShield correctly identified and blocked all malicious requests.

```text
Detection Accuracy = Correct Detections / Total Malicious Test Cases
Detection Accuracy = 5 / 5
Detection Accuracy = 100%
```

This result applies only to the tested payload set. In a real-world environment, detection accuracy would depend on rule quality, payload variation, encoding, evasion techniques, and traffic behavior.

## 8. False Positives and False Negatives

### False Positives

A false positive occurs when normal traffic is incorrectly blocked.

During testing, the normal request `hello` was allowed successfully. No false positive was observed in the basic test.

However, because the current detection engine uses simple pattern matching, some legitimate inputs containing special characters such as `'`, `;`, or `SELECT` could be incorrectly blocked.

### False Negatives

A false negative occurs when malicious traffic is not detected.

No false negative was observed for the tested payloads. However, advanced encoded payloads, obfuscated JavaScript, or complex SQL Injection techniques may bypass the current simple rule engine.

## 9. Log Analysis

The logging system recorded each request with the following details:

* Timestamp
* IP address
* Input value
* Request result
* Detection category

Example log format:

```text
[YYYY-MM-DD HH:MM:SS] IP=127.0.0.1 INPUT=<payload> RESULT=BLOCKED DETECTION=XSS
```

The logs helped verify that:

* Normal requests were allowed.
* Malicious requests were blocked.
* Detection categories were recorded correctly.
* Rate-limited requests were logged.
* Dashboard data was generated from log entries.

## 10. Dashboard Analysis

The dashboard displayed a summary of:

* Total requests
* Allowed requests
* Blocked requests
* Security log entries

During testing, a stored XSS issue was discovered when raw log entries were displayed directly in the browser. This was fixed by escaping HTML output before rendering log data.

This improvement showed that security dashboards must also be protected from malicious content stored in logs.

## 11. Limitations

SentinelShield is a practical learning project and has some limitations:

* Detection is based on simple string pattern matching.
* Advanced payload encoding may bypass detection.
* Rules are manually defined and not automatically updated.
* Rate limiting is stored in memory and resets when the server restarts.
* It does not use a database for long-term alert storage.
* It does not include authentication for dashboard access.
* It is not designed for production deployment.

## 12. Suggested Improvements

Future improvements may include:

* Use regular expressions for stronger rule matching.
* Add payload normalization and URL decoding before inspection.
* Store logs in a database.
* Add authentication for the dashboard.
* Add severity levels for alerts.
* Add IP blocking duration.
* Add charts for attack distribution.
* Add exportable reports.
* Integrate with SIEM-style alerting.
* Add automated test scripts.

## 13. Conclusion

SentinelShield successfully demonstrates the core workflow of a lightweight Web Application Firewall and Intrusion Detection System. The project inspects HTTP requests, detects common web attack signatures, applies IP-based rate limiting, logs all activity, and displays security events through a dashboard.

The practical work helped demonstrate important cybersecurity concepts such as request inspection, signature-based detection, traffic behavior monitoring, alert generation, log analysis, dashboard interpretation, and secure output rendering.
