class ListOperation:
    def __init__(self, list) -> None:
        self.list = list

    def get(self, index):
        return self.list.index(index)

    def sort(self):
        self.list.sort(reverse=False)
        return self.list

