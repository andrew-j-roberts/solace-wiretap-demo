#  This is example training data for classifying user messages into 
#  - Store pictures in S3
#  - Save the chat history

train_array = [
    # STORE PICTURE IN S3
    ('Can you store this in S3?', 'save-file'),
    ('Can you save this file in S3?', 'save-file'),
    ('Can you store this in S3?', 'save-file'),
    ('store this in S3', 'save-file'),
    ('store this file in s3', 'save-file'),
    ('put this in s3', 'save-file'),
    ('save file', 'save-file'),
    ('put file', 'save-file'),
    ('save this', 'save-file'),
    ('can you save this', 'save-file'),
    ('copy this to s3', 'save-file'),
    ('place in s3', 'save-file'),
    ('copy to s3', 'save-file'),
    # SAVE OUR CONVERSATION 
    ('save this convo', 'save-convo'),
    ('save this conversation', 'save-convo'),
    ('save this chat', 'save-convo'),
    ('save chat history', 'save-convo'),
    ('put chat in s3', 'save-convo'),
    ('save chat', 'save-convo'),
    ('save convo', 'save-convo'),
    ('save conversation', 'save-convo')
]

test_array = [
    ('The beer was good.', 'pos'),
    ('I do not enjoy my job', 'neg'),
    ("I ain't feeling dandy today.", 'neg'),
    ("I feel amazing!", 'pos'),
    ('Gary is a friend of mine.', 'pos'),
    ("I can't believe I'm doing this.", 'neg')
]

def get_training_data():
    return train_array

def get_test_data():
    return test_array