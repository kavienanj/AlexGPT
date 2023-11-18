import argparse
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SECRETS_PATH ="src/gmail/"
TOKEN_FILE = SECRETS_PATH + "token.json"
CLIENT_SECRET_FILE = SECRETS_PATH + "client_secret.json"

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def main(count):
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists(TOKEN_FILE):
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRET_FILE, SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open(TOKEN_FILE, "w") as token:
      token.write(creds.to_json())

  try:
    # Call the Gmail API
    service = build("gmail", "v1", credentials=creds)

    # Get last 5 important mails
    results = service.users().messages().list(userId="me", labelIds=["IMPORTANT"]).execute()
    messages = results.get("messages", [])[:count]

    if not messages:
      print("Unable to read mails, retry later.")
      return
    print("Reading last", len(messages), "important mails.")
    for message in messages:
      msg = service.users().messages().get(userId='me', id=message['id']).execute()
      from_mail, subject = "", ""
      for header in msg['payload']['headers']:
        if header['name'] == 'Subject':
          subject = header['value']
        if header['name'] == 'From':
          from_mail = header['value']
      if from_mail and subject:
        print(f"Mail received from: {from_mail}, with subject: {subject}")

  except HttpError as error:
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Run shell commands")
  parser.add_argument(
      "--count",
      type=int,
      required=False,
      default=5,
      help="Number of mails to read",
  )
  args = parser.parse_args()
  count = args.count
  main(count)
