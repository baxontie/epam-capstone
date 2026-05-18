# User Management API

## Overview

The User Management API provides endpoints
for creating, updating, retrieving,
and deleting enterprise user accounts.

The API supports role-based authorization
and audit logging.

---

## Authentication

All API requests require bearer token authentication.

Example:

```http
Authorization: Bearer <access_token>
```

---

## Endpoints

### Create User

```http
POST /api/users
```

Creates a new enterprise user.

#### Request Body

```json
{
  "email": "user@example.com",
  "firstName": "John",
  "lastName": "Doe",
  "role": "Administrator"
}
```

---

### Get User

```http
GET /api/users/{id}
```

Returns user profile information.

---

### Update User

```http
PUT /api/users/{id}
```

Updates user information.

---

### Delete User

```http
DELETE /api/users/{id}
```

Soft deletes a user account.

---

## Validation Rules

- Email addresses must be unique.
- Roles must exist in the authorization system.
- Deleted users cannot authenticate.
- Required fields cannot be empty.

---

## Common Errors

### 401 Unauthorized

Occurs when the access token is invalid or expired.

### 403 Forbidden

Occurs when the user lacks required permissions.

### 404 User Not Found

Occurs when the specified user does not exist.

### 409 Duplicate Email

Occurs when a duplicate email address is detected.

---

## Security Recommendations

- Use HTTPS for all requests.
- Rotate access tokens regularly.
- Restrict administrator permissions.
- Enable audit logging.

---

## Related APIs

- POST /api/auth/login
- POST /api/auth/refresh
- GET /api/audit/logs

---

## Release Changes

### Version 1.2

- Added audit logging support.
- Improved duplicate email validation.
- Added role validation checks.