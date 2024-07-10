from google.oauth2 import service_account
from googleapiclient.discovery import build

# Caminho para o arquivo JSON da conta de serviço
SERVICE_ACCOUNT_FILE = 'credentials2.json'

# Escopo necessário para acessar o Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive']

# Autenticação com a conta de serviço
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Constrói o serviço de API do Google Drive
service = build('drive', 'v3', credentials=credentials)

# Exemplo de listagem dos arquivos no Google Drive
results = service.files().list(pageSize=10, fields="nextPageToken, files(id, name)").execute()
items = results.get('files', [])

if not items:
    print('No files found.')
else:
    print('Files:')
    for item in items:
        print(u'{0} ({1})'.format(item['name'], item['id']))
