from random import randint

class IRCTC:
    def __init__(self,train_name):
        self.train_name = train_name

    def book_ticket(self,fro,to):
        print(f"Booked ticket in {self.train_name} from {fro} to {to}")
    
    def get_status(self):
        print(f"{self.train_name} is running on time")
    
    def price_info(self,fro,to):
        print(f"Ticket Price for {self.train_name} from {fro} to {to}: Rs. {randint(200,500)}")


shan_e_punjab = IRCTC("Shan-e-Punjab")
shan_e_punjab.get_status()
shan_e_punjab.price_info("Khanna","Delhi")
shan_e_punjab.book_ticket("Khanna","Punjab")