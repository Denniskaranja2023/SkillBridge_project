# Railway Deployment Fix - TODO List

## Issues Identified:
1. Duplicate Flask app creation in app.py breaking all routes
2. Incorrect Procfile path for gunicorn
3. Missing Railway domain in CORS configuration
4. SocketIO CORS missing Railway domains
5. Hardcoded SESSION_COOKIE_DOMAIN breaking sessions

## Fixes Completed:

### Step 1: Fix app.py Structure ✅
- [x] Removed duplicate Flask app initialization at the bottom
- [x] Kept routes registered on the imported app from config
- [x] Fixed SocketIO CORS to include Railway domains

### Step 2: Fix Procfile ✅
- [x] Corrected the gunicorn module path with quotes: `"server.config:app"`

### Step 3: Fix CORS Configuration in config.py ✅
- [x] Added Railway domains to Flask-CORS origins
- [x] Made SESSION_COOKIE_DOMAIN configurable via environment variable

## Railway Environment Variables to Set:

In your Railway dashboard, add these environment variables:

```
DATABASE_URL=<your-postgresql-connection-string>
SESSION_COOKIE_DOMAIN=<your-railway-domain>.up.railway.app
```

Example:
```
DATABASE_URL=postgres://user:pass@containers-us-west-123.railway.app:5432/railway
SESSION_COOKIE_DOMAIN=skillbridge-production.up.railway.app
```

## Testing After Deployment:
1. Deploy to Railway
2. Test API endpoints are accessible (e.g., `https://your-domain.railway.app/api/login`)
3. Verify CORS requests work from Railway domain
4. Test authentication/session cookies work properly

## Client Configuration Update (if needed):
Ensure your Client/src/config.js uses Railway URL:
```javascript
export const BASE_URL = import.meta.env.VITE_API_URL || 'https://your-railway-domain.up.railway.app';
```

## Common Railway Issues:
- **Routes not accessible**: Check Railway logs for startup errors
- **CORS errors**: Ensure SESSION_COOKIE_DOMAIN is set correctly
- **Database connection**: Verify DATABASE_URL is set and using PostgreSQL
- **Static files**: Railway may need extra configuration for file uploads

