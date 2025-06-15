# Security Policy

## Supported Versions

We release security updates for the latest version of the Health Microservice API. Please ensure you are running the latest version for the best security.

## Reporting a Vulnerability

If you discover a security vulnerability, please follow these steps:

1. **Do not open a public issue.**
2. **Report it privately** by emailing the maintainer at [sany2k8@gmail.com](mailto:sany2k8@gmail.com).
3. Include as much detail as possible to help us quickly resolve the issue.
4. We will acknowledge receipt of your report and keep you updated on the status.

## Security Best Practices

- Always keep your dependencies up to date (`uv sync` regularly).
- Protect your `.env` file and never commit sensitive credentials.
- Use strong, unique passwords for your database and JWT secret.
- Limit access to your deployment environment.
- Regularly review and update permissions for database and API users.

## Disclosure Policy

We will investigate all reported vulnerabilities and address them promptly. Once a fix is available, we will disclose the issue and mitigation steps in the release notes.

Thank you for helping keep this project and its users secure!
