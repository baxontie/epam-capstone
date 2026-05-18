# CORS Troubleshooting Guide

## Overview

Cross-Origin Resource Sharing (CORS) errors occur
when frontend applications attempt to access backend APIs
from different origins without proper configuration.

This guide describes common causes and troubleshooting steps.

---

## Common Symptoms

- Browser blocks API requests.
- "Access-Control-Allow-Origin" header missing.
- Authentication requests fail.
- Preflight OPTIONS requests return errors.

---

## Common Causes

### Missing CORS Headers

The backend does not return required CORS headers.

### Invalid Allowed Origins

The frontend origin is not included in the allowed origins list.

### Credential Configuration Issues

Requests using cookies or authorization headers
require additional CORS configuration.

### OPTIONS Request Failure

The backend does not correctly handle preflight requests.

---

## Recommended Configuration

### ASP.NET Core Example

```csharp
builder.Services.AddCors(options =>
{
    options.AddPolicy("DefaultPolicy", policy =>
    {
        policy
            .AllowAnyHeader()
            .AllowAnyMethod()
            .AllowCredentials()
            .WithOrigins("http://localhost:4200");
    });
});

app.UseCors("DefaultPolicy");
```

---

## Security Recommendations

- Avoid using AllowAnyOrigin with credentials.
- Restrict allowed origins in production.
- Log blocked requests for audit purposes.
- Validate authorization headers.

---

## Related APIs

- POST /api/auth/login
- POST /api/auth/register
- GET /api/users/profile

---

## Release Notes

### Version 1.3

- Added stricter origin validation.
- Improved preflight request handling.
- Added CORS audit logging.