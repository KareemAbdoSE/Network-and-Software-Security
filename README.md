# Comprehensive Network Security Implementation

A Python-based secure access control system for Finvest Holdings using RBAC and ACLs to protect financial data.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup](#setup)
5. [Usage](#usage)

## Introduction
This project is a secure access control system implemented in Python for Finvest Holdings. It safeguards sensitive financial data by employing Role-Based Access Control (RBAC) and Access Control Lists (ACLs). The system ensures users have permissions appropriate to their roles, enhancing security through the principle of least privilege.

## Features
- **Role-Based Access Control (RBAC):** Aligns permissions with specific roles to ensure users have necessary access.
- **Access Control Lists (ACLs):** Provides fine-grained control over resources.
- **Secure Password Management:** Utilizes PBKDF2 HMAC SHA-256 hashing with salts for robust password security.
- **Proactive Password Checker:** Enforces strong password policies and prevents the use of weak passwords.
- **User Enrollment Interface:** Allows new users to register securely with real-time password validation.
- **Login Mechanism:** Authenticates users and displays their access permissions based on roles.
- **Comprehensive Testing:** Includes automated tests for access control and authentication mechanisms.

## Technologies Used
- **Programming Language:** Python 3.x
- **Cryptography Modules:** hashlib, os
- **Password Hashing Algorithm:** PBKDF2 HMAC SHA-256
- **User Interface:** Command-line interfaces for enrollment and login

## Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/KareemAbdoSE/Network-and-Software-Security.git
   cd Network-and-Software-Security
   
2. **Install Dependencies:**
- No external dependencies are required beyond Python's standard library.

3. **Run the Enrollment Script:**
   ```bash
   python enrollment.py
- Follow the prompts to enter your User ID, Password, Password Confirmation, and Role.

4. **Run the Login Script:**
   ```bash
   python login.py
- Enter your User ID and Password to authenticate.

## Usage
- **User Enrollment:** Register new users with secure password policies.
- **User Authentication:** Log in to access resources based on your role.
- **Access Control Enforcement:** Permissions are granted according to RBAC and ACL policies.
