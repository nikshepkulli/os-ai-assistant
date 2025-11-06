# Security Policy

## Supported Versions

We take security seriously. The following versions of OS AI Assistant are currently supported with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

We greatly appreciate security researchers and users who report vulnerabilities to the OS AI Assistant community. All reports are thoroughly investigated.

### How to Report a Security Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via one of the following methods:

1. **GitHub Security Advisories** (Preferred)
   - Go to https://github.com/nikshepkulli/os-ai-assistant/security/advisories
   - Click "Report a vulnerability"
   - Provide detailed information about the vulnerability

2. **Email** (Alternative)
   - Open a GitHub issue with the title "Security: Contact Request"
   - A maintainer will provide a secure contact method

### What to Include in Your Report

Please include the following information:

- Type of vulnerability (e.g., command injection, privilege escalation, etc.)
- Full paths of source file(s) related to the vulnerability
- Location of the affected source code (tag/branch/commit or direct URL)
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the vulnerability, including how an attacker might exploit it

### Response Timeline

- **Initial Response**: Within 48 hours
- **Status Update**: Within 7 days
- **Fix Timeline**: Depends on severity
  - Critical: Within 7 days
  - High: Within 30 days
  - Medium: Within 90 days
  - Low: Next release cycle

## Security Best Practices

When using OS AI Assistant:

### For Users

1. **Keep Software Updated**: Always use the latest version
2. **Review Permissions**: Only grant necessary system permissions
3. **API Keys**: Store API keys securely, never commit them to version control
4. **Command Confirmation**: Enable confirmation for dangerous operations in config
5. **Audit Logs**: Regularly review command history logs

### For Developers

1. **Input Validation**: All user inputs must be validated and sanitized
2. **Command Execution**: Use safe subprocess execution methods
3. **Path Traversal**: Prevent path traversal attacks in file operations
4. **API Keys**: Use environment variables or secure key storage
5. **Dependencies**: Regularly update dependencies and scan for vulnerabilities

## Known Security Considerations

### System Access
- The assistant requires accessibility permissions to control your system
- Only grant permissions you're comfortable with
- Review the permission system in `src/utils/security.py`

### Voice Commands
- Voice commands are processed by AI (GPT-4/Claude)
- Be aware that transcripts may be sent to OpenAI/Anthropic APIs
- Use local Whisper STT for privacy-sensitive environments

### File Operations
- Deletion operations move files to trash (not permanent delete)
- Dangerous operations require user confirmation by default
- Customize security rules in `config/config.yaml`

### API Keys
- Never commit API keys to version control
- Use environment variables: `OPENAI_API_KEY`
- Rotate keys if accidentally exposed

## Security Features

### Built-in Protections

1. **Permission System**
   - Whitelist/blacklist for commands
   - Confirmation required for dangerous operations
   - Configurable security rules

2. **Safe Defaults**
   - Files moved to trash, not permanently deleted
   - Command history logged for auditing
   - Sensitive data sanitized from logs

3. **Input Validation**
   - Path sanitization to prevent traversal attacks
   - Command validation before execution
   - Rate limiting for API calls

## Vulnerability Disclosure Policy

- We follow responsible disclosure practices
- Security researchers will be credited (unless they prefer to remain anonymous)
- We'll coordinate disclosure timeline with the reporter
- CVEs will be requested for significant vulnerabilities

## Security Hall of Fame

We'll recognize security researchers who help improve OS AI Assistant security:

_No vulnerabilities reported yet - be the first!_

## Additional Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE Top 25](https://cwe.mitre.org/top25/)
- [GitHub Security Best Practices](https://docs.github.com/en/code-security)

## Contact

For general security questions (not vulnerabilities), please open a GitHub Discussion.

---

Thank you for helping keep OS AI Assistant and its users safe!
