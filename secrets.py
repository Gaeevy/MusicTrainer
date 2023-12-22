from google.cloud import secretmanager
import google_crc32c

PROJECT_ID = "music-trainer-42"
SECRET_ID = "BOT_TOKEN"


def get_bot_token() -> str:
    """
    Get information about the given secret. This only returns metadata about
    the secret container, not any secret material.
    """

    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    name = f"projects/{PROJECT_ID}/secrets/{SECRET_ID}/versions/1"

    response = client.access_secret_version(request={"name": name})

    # Verify payload checksum.
    crc32c = google_crc32c.Checksum()
    crc32c.update(response.payload.data)
    if response.payload.data_crc32c != int(crc32c.hexdigest(), 16):
        print("Data corruption detected.")

    # Print the secret payload.
    token = response.payload.data.decode("UTF-8")
    return token