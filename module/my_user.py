class User:
    def __init__(self,name):
        self.keyword_list = []
        self.name = name

    def get_user_name(self):
        self.name = input("이름을 입력하세요:")
        return self.name
    
    def add_keyword(self,keyword):
        self.keyword_list.append(keyword)
    
    def show_keyword(self):
        for i in self.keyword_list:
            print(i)
    
    

