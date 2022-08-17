# Mail Manager
- Automated cleanup for gmail.

## Prerequisites
- `npm run install`
- (Should still be valid) `credentials.json` generated from GCP. (download from GCP API & Services Credentials)

## Refresh token:
- note: if you change scope you need to delete token.json to regenerate a new one. also 
reset secret in GCP.
- note: has some issues if there is an active token elsewhere.


GCP console:
https://console.cloud.google.com/apis/dashboard?project=

## To run
```bash
npm run start
```
