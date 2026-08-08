# Security Policy

## 🛡️ Overview

The **Affiliate Links Generator** project takes security and user privacy seriously. As a tool designed to construct and handle URLs containing affiliate tracking IDs and publisher tokens, maintaining clean, secure, and injection-safe URL generation is a core priority.

---

## 📋 Supported Versions

We actively provide security updates and patches for the following versions:

| Version / Branch | Supported          |
| ---------------- | ------------------ |
| `main` (Latest)  | :white_check_mark: |
| < 1.0.0          | :x:                |

---

## 🔒 Reporting a Vulnerability

If you discover a security vulnerability, flaw in URL sanitization, credential exposure issue, or potential injection vector in Affiliate Links Generator, please report it responsibly.

### How to Submit a Security Report

**Do NOT create a public GitHub Issue for security vulnerabilities.**

Instead, please report the security issue privately by:

1. Submitting a **Private Security Advisory** via GitHub's [Security Advisories page](https://github.com/rishibanota/Affiliate-Links-Generator/security/advisories/new).
2. Alternatively, emailing the project maintainer, **Rishi Banota**, directly via GitHub profile contact details.

### What to Include in Your Report

To help us investigate and resolve the issue quickly, please include:

* A description of the vulnerability and its potential impact.
* Step-by-step instructions or proof-of-concept (PoC) script to reproduce the behavior.
* Affected provider module(s) or CLI options.
* Suggested fix or mitigation steps (if known).

---

## ⏱️ Response Timeline

* **Acknowledgment**: Within 48 hours of receipt.
* **Assessment**: Preliminary assessment within 5 business days.
* **Fix & Patch Release**: Critical vulnerabilities will be patched promptly on the `main` branch.

---

## 💡 Best Practices for Users

When using Affiliate Links Generator:

1. **Avoid Hardcoding Secrets**: Never commit affiliate API keys, publisher secrets, or sensitive credentials into public version control. Use environment variables or local configuration files.
2. **Validate Input URLs**: When exposing this package in web applications or API endpoints, ensure input URLs are validated against allowed schemes (`http://`, `https://`).
