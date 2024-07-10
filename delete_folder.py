from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Caminho para o arquivo JSON da conta de serviço
SERVICE_ACCOUNT_FILE = 'credentials2.json'

# Escopo necessário para acessar o Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive']


def delete_file_folder(file_id):
    # Autenticação com a conta de serviço
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    try:
        # call drive api client
        service = build("drive", "v3", credentials=credentials)

        response = service.files().delete(fileId=file_id).execute()

        results = (
            service.files()
            .list(pageSize=10, fields="nextPageToken, files(id, name)")
            .execute()
        )
        items = results.get("files", [])

        print("Files:")
        for item in items:
            print(f"{item['name']} ({item['id']})")

    except HttpError as error:
        print(f"An error occurred: {error}")
        return None


if __name__ == "__main__":
    delete_file_folder(
        file_id="10NiH44R2BHUQPNoFpMqe6q7rqiaByOHK",
    )
