from flask import Flask, request
from html import escape
from datetime import datetime, timedelta

app = Flask(__name__)

attack_patterns = {
    "SQL Injection": ["'", "\"", " OR ", " AND ", "--", "UNION", "SELECT", "DROP"],
    "XSS": ["<script>", "</script>", "alert(", "onerror=", "onload="],
    "Directory Traversal / LFI": ["../", "..\\", "/etc/passwd", "boot.ini"],
    "Command Injection": [";", "&&", "||", "|", "whoami", "cat ", "ls "]
}

request_tracker = {}

RATE_LIMIT = 5
TIME_WINDOW = 60
LOG_FILE = "../logs/sentinelshield.log"

def inspect_request(user_input):
    detected_attacks = []

    for attack_type, patterns in attack_patterns.items():
        for pattern in patterns:
            if pattern.lower() in user_input.lower():
                detected_attacks.append(attack_type)
                break

    return detected_attacks

def check_rate_limit(ip_address):
    current_time = datetime.now()

    if ip_address not in request_tracker:
        request_tracker[ip_address] = []

    request_tracker[ip_address].append(current_time)

    valid_requests = []
    for request_time in request_tracker[ip_address]:
        if current_time - request_time <= timedelta(seconds=TIME_WINDOW):
            valid_requests.append(request_time)

    request_tracker[ip_address] = valid_requests

    if len(request_tracker[ip_address]) > RATE_LIMIT:
        return True

    return False

def write_log(ip_address, user_input, result, attacks):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = (
        f"[{timestamp}] IP={ip_address} "
        f"INPUT={user_input} RESULT={result} "
        f"DETECTION={','.join(attacks) if attacks else 'None'}\n"
    )

    with open(LOG_FILE, "a") as log_file:
        log_file.write(log_entry)

def read_logs():
    try:
        with open(LOG_FILE, "r") as log_file:
            return log_file.readlines()
    except FileNotFoundError:
        return []

@app.route("/")
def home():
    return """
    <h1>SentinelShield</h1>
    <p>Advanced Intrusion Detection & Web Protection System</p>

    <form action="/search" method="GET">
        <input type="text" name="q" placeholder="Enter search query">
        <button type="submit">Submit</button>
    </form>

    <br>
    <a href="/dashboard">View Security Dashboard</a>
    """

@app.route("/search")
def search():
    user_input = request.args.get("q", "")
    ip_address = request.remote_addr

    detected_attacks = inspect_request(user_input)
    rate_limited = check_rate_limit(ip_address)

    if rate_limited:
        write_log(ip_address, user_input, "BLOCKED", ["Rate Limit Exceeded"])
        return """
        <h2>Request Blocked</h2>
        <p><b>Reason:</b> Too many requests from same IP address</p>
        <p><b>Detection:</b> Rate Limit Exceeded</p>
        <br>
        <a href="/">Back</a>
        """

    if detected_attacks:
        write_log(ip_address, user_input, "BLOCKED", detected_attacks)
        return f"""
        <h2>Request Blocked</h2>
        <p><b>Reason:</b> Suspicious payload detected</p>
        <p><b>Detection:</b> {', '.join(detected_attacks)}</p>
        <br>
        <a href="/">Back</a>
        """

    write_log(ip_address, user_input, "ALLOWED", detected_attacks)
    return f"""
    <h2>Request Allowed</h2>
    <p>Your input: {user_input}</p>
    <br>
    <a href="/">Back</a>
    """

@app.route("/dashboard")
def dashboard():
    logs = read_logs()
    safe_logs = [escape(log) for log in logs]

    total_requests = len(logs)
    blocked_requests = len([log for log in logs if "RESULT=BLOCKED" in log])
    allowed_requests = len([log for log in logs if "RESULT=ALLOWED" in log])

    dashboard_html = f"""
    <h1>SentinelShield Security Dashboard</h1>

    <h3>Summary</h3>
    <p>Total Requests: {total_requests}</p>
    <p>Allowed Requests: {allowed_requests}</p>
    <p>Blocked Requests: {blocked_requests}</p>

    <h3>Security Logs</h3>
    <pre>
    {''.join(safe_logs)}
    </pre>

    <br>
    <a href="/">Back to Home</a>
    """

    return dashboard_html

if __name__ == "__main__":
    app.run(debug=True)
