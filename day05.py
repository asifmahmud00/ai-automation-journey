

def is_urgent(message):
    if "urgent" in message.lower():
        return True
    else:
        return False

value = is_urgent("not Urgent message")
print(value)

def count_messages(messages):
    count = 0

    for message in messages:
        count = count + 1

    return count

messages = [
    "Hello, I need help",
    "Where is my order?",
    "I want a refund",
    "My payment failed"
]

total = count_messages(messages)

print("Total messages:", total)