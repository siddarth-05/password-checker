# Password Strength & Breach Checker

A Python tool to check password strength and verify if your password has been exposed in public data breaches.

## Features

- Password Strength Analysis

  -Checks for minimum length (default: 14 characters)

  -Requires uppercase, lowercase, digits, and special characters

  -Provides clear, actionable feedback on missing criteria

- Breach Detection

  -Uses the Have I Been Pwned (HIBP) API to check if the password has appeared in public data breaches

  -Privacy-preserving: only a partial hash of the password is sent to the API

- Web Demo (Optional)

  -Flask-based web interface for interactive password checking

  -Ready for deployment on Render or similar platforms

## Usage

- liter
