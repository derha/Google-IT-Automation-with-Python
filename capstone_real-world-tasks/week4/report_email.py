#!/usr/bin/env python3

import os
from datetime import datetime
import reports
import emails


def make_paragraph():
    paragraph = []
    working_dir = "supplier-data/descriptions"
    for file in os.listdir(working_dir):
        with open(os.path.join(working_dir, file), 'r+', encoding="utf-8") as f:
            paragraph.append("name: {}".format(f.readline().strip()))
            paragraph.append("weight: {}<br />".format(f.readline().strip()))
    return paragraph


def main():
    # make a PDF file
    attachment = "/tmp/processed.pdf"
    now = datetime.now()
    title = "Processed Update on " + "{} {}, {}".format(now.strftime('%B'), now.strftime('%d'), now.strftime('%Y'))
    paragraph = "<br />".join(make_paragraph())
    reports.generate_report(attachment, title, paragraph)
    # send an email
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send_email(message)


if __name__ == "__main__":
    main()
