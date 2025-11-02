class Book:
    def init(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"عنوان: {self.title}, نویسنده: {self.author}, قیمت: {self.price} تومان")

    def apply_discount(self, discount_percent):
        discount_amount = (self.price * discount_percent) / 100
        self.price -= discount_amount



book1 = Book("ملت عشق", "الیف شافاک", 200000)
book2 = Book("قلعه حیوانات", "جورج اورول", 150000)

print("اطلاعات قبل از تخفیف:")
book1.display_details()
book2.display_details()

book1.apply_discount(10)  
book2.apply_discount(20)  

print("\nاطلاعات بعد از تخفیف:")
book1.display_details()
book2.display_details()