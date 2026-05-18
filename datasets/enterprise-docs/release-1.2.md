# Enterprise Platform Release 1.2

## Release Overview

Version 1.2 introduces major security,
authentication, and workflow improvements.

The release focuses on improving enterprise security,
auditability, and user management performance.

---

## New Features

### Multi-Factor Authentication

Added optional multi-factor authentication support
for enterprise users.

### Enhanced Audit Logging

The platform now tracks:
- login attempts
- approval actions
- password reset events
- administrative changes

### Registration Retry Protection

Duplicate registration attempts are now automatically detected.

### Improved Organization Search

Optimized organization lookup queries
for large enterprise datasets.

---

## Security Improvements

- Improved token expiration handling.
- Added stricter password validation rules.
- Added enhanced session timeout controls.
- Improved CORS validation logic.

---

## API Changes

### Updated Endpoints

- POST /api/auth/login
- POST /api/auth/register
- POST /api/auth/refresh

### New Endpoints

- POST /api/auth/mfa/verify
- GET /api/audit/logs

---

## Known Issues

### Session Expiration Delay

Some users may experience delayed session invalidation.

### Audit Log Performance

Audit queries may be slower on large datasets.

---

## Migration Notes

- Existing sessions must be re-authenticated.
- MFA configuration is optional.
- Audit logging is enabled by default.

---

## Deployment Notes

- Restart authentication services after deployment.
- Validate CORS configuration.
- Clear expired session caches.