# Training data
messages = [
    ('Win money now free prize', 'spam'),
    ('Congratulations you won lottery', 'spam'),
    ('Free entry to win cash', 'spam'),
    ('Urgent claim your prize now', 'spam'),
    ('You have won 10000 dollars', 'spam'),
    ('Hi how are you doing today', 'ham'),
    ('Lets meet for lunch tomorrow', 'ham'),
    ('Are you coming to college', 'ham'),
    ('Please send the assignment', 'ham'),
    ('Good morning have a nice day', 'ham'),
]

# Word count for spam and ham
spam_words = {}
ham_words = {}
spam_count = 0
ham_count = 0

for msg, label in messages:
    words = msg.lower().split()
    for w in words:
        if label == 'spam':
            spam_words[w] = spam_words.get(w, 0) + 1
            spam_count += 1
        else:
            ham_words[w] = ham_words.get(w, 0) + 1
            ham_count += 1

print("Model Trained Successfully")
print(f"Spam words: {len(spam_words)}, Ham words: {len(ham_words)}")
print("\n--- Spam/Ham Prediction ---")
print("Type 'exit' to stop")

# detection loop
while True:
    test = input("\nEnter message: ")
    if test.lower() == 'exit':
        break
    
    words = test.lower().split()
    spam_score = 0
    ham_score = 0
    
    for w in words:
        # Agar word spam me zyada hai to spam score badhao
        if w in spam_words:
            spam_score += spam_words[w]
        if w in ham_words:
            ham_score += ham_words[w]
        # Special spam keywords
        if w in ['win','free','prize','lottery','urgent','money','won','claim','cash','dollars']:
            spam_score += 2
    
    print(f"Spam Score: {spam_score}, Ham Score: {ham_score}")
    if spam_score > ham_score:
        print(f"Result: SPAM -> {test}")
    else:
        print(f"Result: HAM -> {test}")
