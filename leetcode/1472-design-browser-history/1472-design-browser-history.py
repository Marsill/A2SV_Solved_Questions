class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        homepage = Node(homepage)
        self.home = homepage

    def visit(self, url: str) -> None:
        url = Node(url)

        self.home.next = url
        url.prev = self.home
        self.home = self.home.next
            

    def back(self, steps: int) -> str:
        while steps and self.home.prev:
            self.home = self.home.prev
            steps -= 1
        return self.home.value

    def forward(self, steps: int) -> str:
        while steps and self.home.next: 
            self.home = self.home.next
            steps -= 1
        return self.home.value
    



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)