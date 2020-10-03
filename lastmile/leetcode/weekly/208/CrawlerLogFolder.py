from typing import List


class CrawlerLogFolder:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log == '../' :
                if stack:
                    stack.pop()
            elif log == './':
                pass
            else:
                stack.append(log)
        return len(stack)

if __name__ == '__main__':
    init = CrawlerLogFolder()
    print(init.minOperations(["d1/", "d2/", "./", "d3/", "../", "d31/"]))
    print(init.minOperations(["d1/", "../", "../", "../"]))
    print(init.minOperations(["./","../","./"]))
