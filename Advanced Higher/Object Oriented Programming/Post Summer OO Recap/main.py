class Ticket:
    def __init__(self, user, issue):
        self.user = user
        self.issue = issue
        self.next = None
    
class HelpDesk:
    def __init__(self):
        self.head = None

    def log_ticket(self, user, issue):
        new_ticket = Ticket(user, issue)
        new_ticket.next = self.head
        self.head = new_ticket

    def show_tickets(self):
        current = self.head
        while current is not None:
            print(f"{current.user} reported: {current.issue}")
            current = current.next

hd = HelpDesk()
hd.log_ticket("fayalw", "Laptop not working")
hd.log_ticket("deevij", "Phone glitching")
hd.log_ticket("lucgri", "Ipad not charging")
hd.show_tickets()