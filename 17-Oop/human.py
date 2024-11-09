class Human:
    human = "Homo sapiens"
    def __init__(self, head, hands, legs, body):
        self.head = head
        self.hands = hands
        self.legs = legs
        self.body = body

    def about_head(self):
        print(f"Human have only one head, {self.head} is the scientific name for the human head")
    def about_hands(self):
        print(f"Human have two hands, {self.hands} is the scientific name for the human hands")
    def about_legs(self):
         print(f"Human have two legs, {self.legs} is the scientific name for the human legs")
    def about_body(self):
        print(f"Human have one body, {self.body} is the scientific name for the human body")

print(f"The {Human.human}")
print(f"..............................\n")
human_objects = Human("The cranium","ossa metacarpalia", "membrum inferius", "Homo sapiens")
human_objects.about_head()
human_objects.about_hands()
human_objects.about_legs()
human_objects.about_body()


    
        