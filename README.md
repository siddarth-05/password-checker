# Password Strength & Breach Checker

Welcome to the Password Strength & Breach Checker! This project is a Python tool that helps you create strong, secure passwords and checks if your password has ever been exposed in a known data breach. It works from the command line, and also includes an optional web demo built with Flask.

---

## Features

- **Password Strength Analysis:**  
  Checks your password for minimum length (14+ characters), uppercase and lowercase letters, digits, and special characters. Gives you clear feedback on what’s missing.

- **Breach Detection:**  
  Uses the Have I Been Pwned (HIBP) API to see if your password has appeared in public data breaches. Your password is never sent directly—only a small part of its hash is checked.

- **Web Demo:**  
  Includes a simple Flask web app for checking passwords in your browser. Ready to deploy on Render or similar platforms.

---

## Installation

1. **Clone this repository:**

2. **Install dependencies:**
(For the web demo, Flask is required.)

---

## Usage

### Command-Line

To check a password from the command line, run: 
`python password_checker.py`


You’ll be prompted to enter a password. The tool will analyze its strength and check if it has been found in any known data breaches.

#### Example Output

Enter your password: My$ecureP@ssw0rd2025
 Strong password!
 Password not found in known breaches.

 
---

### Web Demo

A simple Flask web interface is included.

**To run locally:**
`cd web_demo
flask run`

Then open your browser and go to `http://127.0.0.1:5000`.

**To deploy online:**  
You can deploy the `web_demo` folder to [Render](https://render.com/) or any platform that supports Flask apps.

---

## How It Works

**Password Strength:**  
- Minimum length: 14 characters  
- At least one uppercase letter  
- At least one lowercase letter  
- At least one digit  
- At least one special character (from `~!@#$%^&*()_+=;:,.?`)  
If your password is missing any of these, the tool will tell you exactly what to improve.

**Breach Detection:**  
- Your password is hashed with SHA-1.
- Only the first 5 characters of the hash are sent to the Have I Been Pwned API (this is called the k-anonymity model).
- If your password is found in a breach, you’ll see how many times it’s appeared.

---

## Repository Structure

password-checker/
├── password_checker.py
├── README.md
├── demo_screenshot.png
└── web_demo/
├── app.py
└── templates/
└── index.html


---

## Screenshots

![image](https://github.com/user-attachments/assets/82d6a9f0-fab5-432a-92ee-e7b20d5e8fcc)
(Testing the password "admin123")
![image](https://github.com/user-attachments/assets/44aeaf04-bbd4-44a8-b273-fe451e40774a)
(Testing the password "password")




---

## Contributing

Contributions are welcome! If you have suggestions, find a bug, or want to add a feature, please open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License.

---

## FAQ

**Is my password sent to a third party?**  
No. Only a partial hash is sent to the Have I Been Pwned API, so your actual password never leaves your computer.

**Can I use this in production?**  
This tool is intended for personal or educational use. For production use, review the code and adapt it to your security requirements.

---

Thanks for checking out this project. Stay safe online!


