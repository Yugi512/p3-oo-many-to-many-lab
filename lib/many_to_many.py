class Author:
        
    def __init__(self,name):
        self.name = name

    def contracts(self):
        lists_of_contracts = []
        for contract in Contract.all:
            if contract.author == self:
                lists_of_contracts.append(contract)

        return lists_of_contracts
        
    def books(self):
        list_of_books = []
        contracts = self.contracts()
        for contract in contracts:
            list_of_books.append(contract.book)
        return list_of_books
    
    def sign_contract(self,book,date,royalties):
        contract = Contract(self,book,date,royalties)
        return contract
    
    def total_royalties(self):
        total_sum = 0
        contracts = self.contracts()
        for contract in contracts:
            total_sum += contract.royalties
        return total_sum

class Book:
    def __init__(self,title):
        self.title = title 

    def contracts(self):
        list_of_contracts = []
        for contract in Contract.all:
            if contract.book == self:
                list_of_contracts.append(contract)

        return list_of_contracts
        
    def authors(self):
        list_of_authors =[]
        contracts = self.contracts()
        for contract in contracts:
            list_of_authors.append(contract.author)
        
        return list_of_authors

class Contract:
    all = []
    
    def __init__(self,author,book,date,royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    
    def contracts_by_date(date):
        list_of_dates = []
        for contract in Contract.all:
            if contract.date == date:
                list_of_dates.append(contract)
        return list_of_dates
          


    @property 
    def author(self):
        return self._author
    
    @author.setter
    def author(self,author):
        if isinstance(author,Author):
            self._author = author
        else:
            raise Exception("not author")

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self,book):
        if isinstance(book,Book):
            self._book = book
        else:
            raise Exception("not book")
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self,date):
        if isinstance(date,str):
            self._date = date
        else:
            raise Exception("not date")
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self,royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception("not royalties")
        
    

