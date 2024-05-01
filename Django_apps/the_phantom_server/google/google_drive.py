import os
#from googleapiclient.discovery import build
#from oauth2client.service_account import ServiceAccountCredentials
#from django.conf import settings
#import google_auth_oauthlib.flow

class GoogleDriveService:
    def __init__(self):
        self._SCOPES=['https://www.googleapis.com/auth/drive']
        _base_path = os.path.dirname(__file__)
        _credential_path=settings.BASE_DIR+'/double-carport-379805-3c8d861c5f86.json'
        self.cred = _credential_path

    def build(self):
        creds = ServiceAccountCredentials.from_json_keyfile_name(self.cred, self._SCOPES)
        service = build('drive', 'v3', credentials=creds)

        return service
    
    
class GoogleDriveAPI:
    
    def __init__(self):
        self.GOOGLE_DRIVE_CLIENT_ID = f"{settings.GOOGLE_DRIVE_CLIENT_ID}"
        self.GOOGLE_DRIVE_CLIENT_SECRET = f"{settings.GOOGLE_DRIVE_CLIENT_SECRET}"
        self.GOOGLE_DRIVE_REDIRECT_URI = f"{settings.GOOGLE_DRIVE_REDIRECT_URI}"
        self.GOOGLE_DRIVE_AUTH_URL = f"{settings.GOOGLE_DRIVE_AUTH_URL}"
        self.GOOGLE_DRIVE_TOKEN_URL = f"{settings.GOOGLE_DRIVE_TOKEN_URL}"
        self.client_secret = settings.BASE_DIR+f'/{settings.GOOGLE_DRIVE_CLIENT_SECRET_JSON_FILE}'
        self.SCOPES = settings.SCOPES
        
    def authenticate(self):
        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(self.client_secret, scopes=self.SCOPES)
        flow.redirect_uri = f"{settings.GOOGLE_DRIVE_REDIRECT_URI}"
        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true',
            login_hint='hint@gmail.com',
            prompt='consent')
        return {'authorization_url':authorization_url, 'state':state}
    
    def credentials_to_dict( self, credentials):
        data = {
            "token": credentials.token,
            "refresh_token": credentials.refresh_token,
            "token_uri": credentials.token_uri,
            "client_id": credentials.client_id,
            "client_secret": credentials.client_secret,
            "scopes": credentials.scopes,
        }
        return data
