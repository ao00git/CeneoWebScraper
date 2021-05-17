class Opinion:
    def __init__(self, opinion_id = None, author = None, reocmmendation = None, stars = None, content = None, pros = [], cons = [], purchased = None, submit_date = None, purchase_date = None, useful = None, useless = None):
        self.opinion_id = opinion_id
        self.author = author 
        self.reocmmendation = reocmmendation 
        self.stars = stars 
        self.content = content 
        self.pros = pros 
        self.cons = cons   
        self.purchased = purchased 
        self.submit_date = submit_date
        self.purchase_date = purchase_date
        self.opinion_id = opinion_id 
        self.opinion_id = opinion_id 

    def extract_product(self):