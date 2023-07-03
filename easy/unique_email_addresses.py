from typing import List


def numUniqueEmails(emails: List[str]) -> int:
    unique_email = set()
    for email in emails:
        local_name, domain_name = email.split('@')

        unique_email.add(f"{local_name.split('+')[0].replace('.', '')}@{domain_name}")
    return len(unique_email)


if __name__ == '__main__':
    print(numUniqueEmails(
        ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]))
    print(numUniqueEmails(
        ["testemail@leetcode.com", "testemail1@leetcode.com", "testemail+david@lee.tcode.com"]))
    print(numUniqueEmails(
        ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))
