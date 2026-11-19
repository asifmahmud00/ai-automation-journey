
print("===== MESSAGE CLASSIFIER =====")

message = input("Enter a customer message: ")

message = message.lower()

if "refund" in message:
    print("Category: Refund Request")

elif "price" in message or "cost" in message:
    print("Category: Pricing Inquiry")

elif "delivery" in message or "shipping" in message:
    print("Category: Delivery Inquiry")

else:
    print("Category: General Inquiry")
