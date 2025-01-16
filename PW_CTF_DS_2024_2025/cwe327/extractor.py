import email
from email.policy import default

# Load the email file
with open("container/download.eml", "r") as f:
    msg = email.message_from_file(f, policy=default)

# Extract the attachment
for part in msg.iter_attachments():
    filename = part.get_filename()
    if filename:
        with open(f"encrypted/{filename}", "wb") as file:
            file.write(part.get_payload(decode=True))
