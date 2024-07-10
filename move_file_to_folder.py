from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Caminho para o arquivo JSON da conta de serviço
SERVICE_ACCOUNT_FILE = 'credentials2.json'

# Escopo necessário para acessar o Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive']


def move_file_to_folder(file_id, folder_id):
    """Move specified file to the specified folder.
    Args:
        file_id: Id of the file to move.
        folder_id: Id of the folder
    Print: An object containing the new parent folder and other meta data
    Returns : Parent Ids for the file

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    # Autenticação com a conta de serviço
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    try:
        # call drive api client
        service = build("drive", "v3", credentials=credentials)

        # pylint: disable=maybe-no-member
        # Retrieve the existing parents to remove
        file = service.files().get(fileId=file_id, fields="parents").execute()
        previous_parents = ",".join(file.get("parents"))
        # Move the file to the new folder
        file = (
            service.files()
            .update(
                fileId=file_id,
                addParents=folder_id,
                removeParents=previous_parents,
                fields="id, parents",
            )
            .execute()
        )
        return file.get("parents")

    except HttpError as error:
        print(f"An error occurred: {error}")
        return None


if __name__ == "__main__":
    move_file_to_folder(
        file_id="1qh6A7Zp3MOFc50QQDTJ1J8fb0doH0QPq",
        folder_id="1Bc7EhUrUzZte7HxwMytvuOozDeOgnDR9",
    )
