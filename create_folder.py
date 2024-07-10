from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Caminho para o arquivo JSON da conta de serviço
SERVICE_ACCOUNT_FILE = 'credentials2.json'

# Escopo necessário para acessar o Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive']


def create_folder():
    """Create a folder and prints the folder ID
    Returns : Folder Id

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """

    # Autenticação com a conta de serviço
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    try:
        # create drive api client
        service = build("drive", "v3", credentials=credentials)
        file_metadata = {
            "name": "Invoices",
            "mimeType": "application/vnd.google-apps.folder",
        }

        # pylint: disable=maybe-no-member
        file = service.files().create(body=file_metadata, fields="id").execute()
        print('file', file)
        print(f'Folder ID: "{file.get("id")}".')
        return file.get("id")

    except HttpError as error:
        print(f"An error occurred: {error}")
        return None


if __name__ == "__main__":
    create_folder()
