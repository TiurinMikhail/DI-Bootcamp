
class Pagination():
    def __init__(self,items=None, pageSize=10):
        self.items = items
        self.pageSize = pageSize
        self.currentPage = 1
        self.list_of_pages = [self.items[i:i+self.pageSize] for i in range(0,len(self.items),self.pageSize)]
        self.total_pages = len(self.list_of_pages)

    def getVisibleItems(self):
        print(self.list_of_pages[self.currentPage-1])
        return self

    def nextPage(self):
        if self.currentPage + 1 > self.total_pages:
            self.currentPage = self.total_pages
        else:
            self.currentPage = self.currentPage + 1
        return self

    def prevPage(self):
        if self.currentPage - 1 <= 0:
            self.currentPage = 1
        else:
            self.currentPage = self.currentPage - 1
        return self

    def firstPage(self):
        self.currentPage = 1
        return self

    def lastPage(self):
        self.currentPage = self.total_pages
        return self

    def goToPage(self,pageNum):
        if pageNum > self.total_pages:
            self.currentPage = self.total_pages
        elif pageNum <= 0:
            self.currentPage = 1
        else:
            self.currentPage = pageNum
        return self


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

p.getVisibleItems()

p.nextPage().nextPage().getVisibleItems()
p.nextPage().prevPage().getVisibleItems()
p.nextPage().prevPage().getVisibleItems()
p.goToPage(3)
p.getVisibleItems()

p.nextPage().nextPage().nextPage().nextPage().getVisibleItems().nextPage().getVisibleItems()

p.goToPage(1).prevPage().getVisibleItems()

p1 = Pagination(alphabetList, 5)
p1.getVisibleItems()