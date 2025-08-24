import os
import openreview
from pathlib import Path

EMAIL = ""  # Set your OpenReview email
PASSWORD = ""  # Set your OpenReview password

# This is the id encoded as an "id" variable in the URL of your venue on OpenReview
VENUE_ID = ""  # Your venue id

OUTPUT_DIR = ""  # Set the output directory

# API V2
client = openreview.api.OpenReviewClient(
    baseurl="https://api2.openreview.net", username=EMAIL, password=PASSWORD
)

venue_group = client.get_group(VENUE_ID)
submission_name = venue_group.content["submission_name"]["value"]
submissions = client.get_all_notes(invitation=f"{VENUE_ID}/-/{submission_name}")

os.makedirs(OUTPUT_DIR, exist_ok=True)

for note in submissions:
    if note.content.get("pdf"):
        f = client.get_attachment(note.id, "pdf")
        with open(str(Path(OUTPUT_DIR, f"paper{note.number}.pdf")), "wb") as op:
            op.write(f)
