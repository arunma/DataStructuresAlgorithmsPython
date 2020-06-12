class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = []
        self.popped = []
        self.history.append(homepage)

    def visit(self, url: str) -> None:
        self.history.append(url)
        self.popped=[]

    def back(self, steps: int) -> str:
        while steps > 0 and len(self.history) > 1:
            self.popped.append(self.history.pop())
            steps=steps-1
        return self.history[-1]

    def forward(self, steps: int) -> str:
        while steps > 0 and len(self.popped) > 0:
            self.history.append(self.popped.pop())
            steps = steps - 1
        return self.history[-1]


if __name__ == '__main__':
    browserHistory = BrowserHistory("leetcode.com")
    browserHistory.visit("google.com")  # You are in "leetcode.com". Visit "google.com"
    browserHistory.visit("facebook.com")  # You are in "google.com". Visit "facebook.com"
    browserHistory.visit("youtube.com")  # You are in "facebook.com". Visit "youtube.com"
    print(browserHistory.back(1))  # You are in "youtube.com", move back to "facebook.com" return "facebook.com"
    print(browserHistory.back(1))  # You are in "facebook.com", move back to "google.com" return "google.com"
    print("forward " + browserHistory.forward(1))  # You are in "google.com", move forward to "facebook.com" return "facebook.com"
    browserHistory.visit("linkedin.com")  # You are in "facebook.com". Visit "linkedin.com"
    print("forward " + browserHistory.forward(2))  # You are in "linkedin.com", you cannot move forward any steps.
    print(browserHistory.back(2))  # You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
    print(browserHistory.back(7))  # You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"


    # browserHistory = BrowserHistory("zav.com")
    # browserHistory.visit("kni.com")  # You are in "leetcode.com". Visit "google.com"
    # print(browserHistory.back(7))  #zav
    # print(browserHistory.back(7))  # zav
    # print("forward " + browserHistory.forward(5))  # kni
    # print("forward " + browserHistory.forward(1))  # kni
    # browserHistory.visit("pwrrbnw.com")
    # browserHistory.visit("mosohif.com")
    # print(browserHistory.back(9))  #zav.com
