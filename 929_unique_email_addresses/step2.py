# local + domain, @で分かれる
# localにある.は無視
# localの、+以降は無視

from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        for email in emails:
            local, domain = email.split("@")
            local = local.replace(".", "")
            local = local.split("+")[0]

            normalized_email = f"{local}@{domain}"
            unique_emails.add(normalized_email)

        return len(unique_emails)
