from collections import defaultdict
from typing import List


class AccountsMerge:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        def dfs(idx, emails):
            if idx not in seen:
                seen.add(idx)
                for j in range(1, len(accounts[idx])):
                    email = accounts[idx][j]
                    emails.add(email)
                    for i in emailAccountMap[email]:
                        dfs(i, emails)

        emailAccountMap = defaultdict(list)

        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                emailAccountMap[account[j]].append(i)

        seen = set()
        result = []
        for i, account in enumerate(accounts):
            name, emails = account[0], set()
            if i not in seen:
                dfs(i, emails)
                result.append([name] + sorted(emails))

        return result


if __name__ == '__main__':
    init = AccountsMerge()
    print(init.accountsMerge(
        accounts=[["John", "johnsmith@mail.com", "john00@mail.com"],
                  ["John", "johnnybravo@mail.com"],
                  ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                  ["Mary", "mary@mail.com"]]))
