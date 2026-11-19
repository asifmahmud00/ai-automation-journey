messages = [
    "Hello, I need help with my order",
    "What are your prices?",
    "My payment is not working",
    "Thank you for your service",
    "Where is my delivery?",
    "I want a refund",
    "I have a Complaint",
    "I want to complain",
    "Your service is bad"
]

print("CUSTOMER MESSAGE REPORT")
print("-----------------------")
count = 0

for message in messages:
    print("Message:", message)
    count = count + 1

    if "order" in message.lower():
        print("Category: Order")
    elif "price" in message.lower():
        print("Category: Pricing")
    elif "payment" in message.lower():
        print("Category: Payment")
    elif "delivery" in message.lower():
        print("Category: Delivery")
    elif "refund" in message.lower():
        print("Category: Refund")
    elif ("complain" in message.lower() 
        or "complaint" in message.lower()
        or "bad" in message.lower()):
        print("Category: Complain")
        
    else:
        print("Category: General")

    print("----- Count:", count)
    print("-----------------------")

print("Total Messages Processed:", count)

