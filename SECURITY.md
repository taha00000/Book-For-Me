# Security Guidelines

## Environment Variables

This project uses environment variables to store sensitive information like API keys, secrets, and credentials. **NEVER commit actual .env files to version control.**

### Setting Up Environment Variables

1. **Backend**: Copy `backend/env.example` to `backend/.env` and fill in your actual values
2. **Frontend**: Copy `frontend/env.example` to `frontend/.env` and fill in your actual values  
3. **Mobile App**: Copy `App/env.example` to `App/.env` and fill in your actual values

### Required Environment Variables

#### Backend (.env)
- `GEMINI_API_KEY` - Google Gemini API key for AI/NLU
- `WHATSAPP_ACCESS_TOKEN` - Meta WhatsApp Business API access token
- `WHATSAPP_PHONE_NUMBER_ID` - Meta WhatsApp phone number ID
- `WHATSAPP_VERIFY_TOKEN` - Random token for webhook verification
- `FIRESTORE_PROJECT_ID` - Google Cloud Firestore project ID
- `FIRESTORE_CREDENTIALS_FILE` - Path to Firestore service account JSON file
- `JWT_SECRET_KEY` - Secret key for JWT token signing (minimum 32 characters)

#### Frontend (.env)
- `VITE_API_BASE_URL` - Backend API base URL
- `VITE_FIREBASE_*` - Firebase configuration (if using Firebase directly)

#### Mobile App (.env)
- `EXPO_PUBLIC_API_BASE_URL` - Backend API base URL
- `EXPO_PUBLIC_FIREBASE_*` - Firebase configuration

### Files Never to Commit

The following files and directories are automatically excluded via `.gitignore`:

- `.env` and `.env.*` files
- `credentials/` directory
- `*.json` credential files (except package.json, tsconfig.json, etc.)
- `*-service-account.json` files
- `*.pem`, `*.key`, `*.p12`, `*.pfx` files
- `secrets/` directory

### Security Best Practices

1. **Never hardcode API keys or secrets** in source code
2. **Use environment variables** for all sensitive configuration
3. **Rotate credentials regularly**, especially if they may have been exposed
4. **Use strong, random values** for JWT_SECRET_KEY (minimum 32 characters)
5. **Restrict API keys** to only necessary permissions and domains
6. **Review access logs** regularly for suspicious activity

### If Credentials Are Exposed

If you accidentally commit credentials to the repository:

1. **Immediately rotate/revoke** the exposed credentials
2. **Remove the credentials** from git history (contact repository admin)
3. **Update all environments** with new credentials
4. **Review access logs** for unauthorized usage

### Getting API Keys

- **Google Gemini**: https://makersuite.google.com/app/apikey
- **Meta WhatsApp Business API**: https://developers.facebook.com/docs/whatsapp/cloud-api/get-started
- **Firestore**: https://console.cloud.google.com/
- **Firebase**: https://console.firebase.google.com/

