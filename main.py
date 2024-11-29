import os

POSITIVE_FEEDBACK_FILES_PATH = 'data\\aclImdb\\train\\pos'
NEGATIVE_FEEDBACK_FILES_PATH = 'data\\aclImdb\\train\\neg'
SOURCES = [POSITIVE_FEEDBACK_FILES_PATH, NEGATIVE_FEEDBACK_FILES_PATH]
SPECIAL_CHARACTERS = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/\\  "

all_reviews = []

for source in SOURCES:
    reviews = []
    files = os.listdir(source)
    for file in files:
        if file.endswith('.txt'):
            file_path = os.path.join(source, file)
            with open (file_path, encoding='utf-8') as stream:
                content = stream.read().lower()
                content = content.replace('<br />', ' ')
                for char in SPECIAL_CHARACTERS:
                    content = content.replace(char, ' ')
                content = content.split()
                reviews.append(content)
    all_reviews.append(reviews) 

# Unpacking into two separate lists
positive_reviews, negative_reviews = all_reviews

user_review = input('Put down a comment to find out his sentiment: ').lower()
user_review = user_review.replace('<br />', ' ')
for char in SPECIAL_CHARACTERS:
    user_review = user_review.replace(char, ' ')
user_reviews = user_review.split()

results = []
for item in user_reviews:
    count_positive = 0
    count_negative = 0
    for review in positive_reviews:
        if item in review:
            count_positive +=1
    for review in negative_reviews:
        if item in review:
            count_negative += 1
    total = count_positive + count_negative
    if total > 0:
        majority = count_positive - count_negative
        final_score = majority/total
    else:
        final_score = 0
    results.append((item, count_positive, count_negative, final_score))

phrase_sentiment = 0
items_sum = 0
for item in results:
    print(item[0], item[3])
    items_sum += 1
    phrase_sentiment += item[3]
phrase_sentiment_score = phrase_sentiment/ items_sum
if phrase_sentiment_score >= 0:
    print('--\nThe sentiment of your comment is positive and amounts to:', phrase_sentiment_score)
else:
    print('--\nThe sentiment of your comment is negative and amounts to::', phrase_sentiment_score)
