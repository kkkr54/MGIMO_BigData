import random
import json
from datetime import datetime

def generate_message():
    users = ["Alice", "Bob", "Charlie", "Diana"]
    languages = ["English", "Spanish", "French", "German"]
    lessons = ["Grammar Basics", "Vocabulary 101", "Conversational Phrases"]
    exercises = ["Fill-in-the-blank", "Multiple Choice", "Listening Comprehension"]
    
    message = {
        "user": random.choice(users),
        "language": random.choice(languages),
        "lesson": random.choice(lessons),
        "exercise": random.choice(exercises),
        "progress_percent": random.randint(-100, 100),
        "timestamp": datetime.utcnow().isoformat()
    }
    return json.dumps(message)