# hr questions insertion in mongo db script
'''
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.hr_recruitment  # Database name
questions_collection = db.questions  # Collection name

# HR Questions Data
hr_questions = [
    {
        "question": "Tell me about yourself.",
        "keywords": ["Background", "Skills", "Experience", "Achievements", "Goals", "Fit"],
        "answers": [
            "I hold a Business Administration degree and have excelled in customer service over the past two years, achieving a 95% customer satisfaction rate. I'm keen to leverage my expertise in a forward-thinking company that values innovation and customer-centric solutions."
        ]
    },
    {
        "question": "Why do you want to work here?",
        "keywords": ["Company Values", "Culture", "Growth Opportunities", "Alignment", "Contribution", "Passion"],
        "answers": [
            "I am impressed by your company's dedication to sustainability and community engagement. My background in project management and passion for environmental initiatives align perfectly with your mission, and I am excited about the opportunity to contribute to your ongoing success."
        ]
    },
    {
        "question": "What are your greatest strengths?",
        "keywords": ["Skills", "Qualities", "Examples", "Impact", "Relevance", "Confidence"],
        "answers": [
            "My greatest strengths are strategic thinking and leadership. In my previous role, I led a team to implement a new marketing strategy that increased sales by 25% over six months."
        ]
    },
    {
        "question": "What are your weaknesses?",
        "keywords": ["Self-awareness", "Improvement", "Honesty", "Reflection", "Adaptability", "Growth"],
        "answers": [
            "In the past, I struggled with delegating tasks, fearing loss of control. However, by building trust in my team's capabilities and focusing on mentorship, I've transformed this into a strength, leading to more efficient project completions."
        ]
    },
    {
        "question": "Where do you see yourself in five years?",
        "keywords": ["Career Goals", "Growth", "Ambition", "Alignment", "Development", "Vision"],
        "answers": [
            "I envision myself as a senior leader in the organization, driving innovative projects that align with company goals, mentoring emerging talent, and continuously seeking opportunities for personal and professional growth."
        ]
    },
    {
        "question": "Describe a challenging situation you faced and how you handled it.",
        "keywords": ["Problem-solving", "Initiative", "Outcome", "Resilience", "Learning", "Adaptability"],
        "answers": [
            "Faced with a critical system failure that halted operations, I led a task force to diagnose the issue, implemented a temporary solution within hours, and developed a long-term fix that prevented future occurrences, ensuring business continuity."
        ]
    },
    {
        "question": "How do you handle stress and pressure?",
        "keywords": ["Coping Mechanisms", "Resilience", "Time Management", "Prioritization", "Calmness", "Performance"],
        "answers": [
            "I thrive under pressure by employing strategic planning and mindfulness techniques. For instance, during peak season, I implemented a workload distribution plan that reduced stress levels and increased team productivity by 30%."
        ]
    },
    {
        "question": "Why should we hire you?",
        "keywords": ["Fit", "Value Addition", "Skills", "Experience", "Contribution", "Uniqueness"],
        "answers": [
            "With over five years of experience in digital marketing, a data-driven approach, and a passion for storytelling, I have consistently delivered campaigns that exceeded expectations. I am confident that my innovative strategies and commitment to excellence will drive significant growth for your company."
        ]
    },
    {
        "question": "How do you prioritize your work?",
        "keywords": ["Time Management", "Organization", "Decision-Making", "Efficiency", "Planning", "Focus"],
        "answers": [
            "Utilizing the Eisenhower Matrix, I categorize tasks based on urgency and importance, delegate when appropriate, and employ project management tools to track progress, ensuring optimal productivity and alignment with organizational objectives."
        ]
    },
    {
        "question": "How do you handle conflict in the workplace?",
        "keywords": ["Communication", "Resolution", "Empathy", "Professionalism", "Collaboration", "Diplomacy"],
        "answers": [
            "I approach workplace conflicts as opportunities for growth. By facilitating transparent discussions, actively listening, and mediating fair solutions, I have successfully resolved disputes that led to stronger team cohesion and improved performance."
        ]
    }
]

# Insert into MongoDB
questions_collection.insert_many(hr_questions)

print("HR questions inserted successfully!")
'''

#  evaluation criteria script 
'''
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.hr_recruitment  # Database name
criteria_collection = db.evaluation_criteria  # Collection name

# Evaluation Criteria Data
evaluation_criteria = [
    {"name": "Correctness", "description": "Is the response factually accurate?"},
    {"name": "Relevance", "description": "Does the response directly address the question and stay on topic?"},
    {"name": "Completeness", "description": "Does the response cover all key aspects without missing critical details?"},
    {"name": "Conciseness", "description": "Is the response clear and to the point, avoiding unnecessary details?"},
    {"name": "Depth of Understanding", "description": "Does the response demonstrate a strong grasp of the concept and an insightful explanation?"},
    {"name": "Accuracy", "description": "Does the answer correctly match the predefined one?"},
    {"name": "Clarity", "description": "Is it well-structured and understandable?"},
    {"name": "Length", "description": "Is it too lengthy compared to the predefined one?"},
    {"name": "Language Clarity & Grammar", "description": "Is the response well-written, with proper grammar and sentence structure?"},
    {"name": "Creativity", "description": "Does the response showcase originality and insightful thinking?"}
]

# Insert into MongoDB
criteria_collection.insert_many(evaluation_criteria)

print("Evaluation criteria inserted successfully!")
'''

#  recuiter and candidate login script
'''
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.hr_recruitment  # Database name
hr_collection = db.hr_users  # HR Collection
user_collection = db.user_accounts  # User Collection

# HR (Recruiter) Login Data
hr_accounts = [
    {"email": "hr1@example.com", "password": "hrpassword1"},
    {"email": "hr2@example.com", "password": "hrpassword2"},
    {"email": "hr3@example.com", "password": "hrpassword3"}
]

# User (Candidate) Login Data
user_accounts = [
    {"email": "user1@example.com", "password": "userpassword1"},
    {"email": "user2@example.com", "password": "userpassword2"},
    {"email": "user3@example.com", "password": "userpassword3"}
]

# Insert into MongoDB
hr_collection.insert_many(hr_accounts)
user_collection.insert_many(user_accounts)

print("HR and User accounts inserted successfully!")
'''
'''
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.hr_recruitment  # Database name
questions3_collection = db.questions3_collection  # Updated collection name

# HR Questions Data (with Keywords & 3 Predefined Answers)
hr_questions = [
    {
        "question": "Tell me about yourself.",
        "keywords": ["Background", "Skills", "Experience", "Achievements", "Goals", "Fit"],
        "answers": [
            "I have a degree in Business Administration and have worked in customer service for two years.",
            "With a Business Administration degree and two years in customer service, I've developed strong communication skills.",
            "I hold a Business Administration degree and have excelled in customer service over the past two years, achieving a 95% customer satisfaction rate."
        ]
    },
    {
        "question": "Why do you want to work here?",
        "keywords": ["Company Values", "Culture", "Growth Opportunities", "Alignment", "Contribution", "Passion"],
        "answers": [
            "I heard good things about your company and think it would be a good place to work.",
            "Your company's commitment to innovation and employee development aligns with my career aspirations.",
            "I am impressed by your company's dedication to sustainability and community engagement."
        ]
    },
    {
        "question": "What are your greatest strengths?",
        "keywords": ["Skills", "Qualities", "Examples", "Impact", "Relevance", "Confidence"],
        "answers": [
            "I'm a hard worker and get along with people.",
            "I possess strong analytical skills and excel in team collaboration.",
            "My greatest strengths are strategic thinking and leadership."
        ]
    },
    {
        "question": "What are your weaknesses?",
        "keywords": ["Self-awareness", "Improvement", "Honesty", "Reflection", "Adaptability", "Growth"],
        "answers": [
            "I can be a perfectionist sometimes.",
            "I tend to be overly critical of my work, but I've been working on balancing attention to detail with productivity.",
            "In the past, I struggled with delegating tasks, fearing loss of control. However, I have improved by mentoring and trusting my team."
        ]
    },
    {
        "question": "Where do you see yourself in five years?",
        "keywords": ["Career Goals", "Growth", "Ambition", "Alignment", "Development", "Vision"],
        "answers": [
            "I see myself in a stable job, doing well.",
            "In five years, I aim to advance into a managerial role and lead a team.",
            "I envision myself as a senior leader, driving innovation and mentoring future talents."
        ]
    },
    {
        "question": "Describe a challenging situation you faced and how you handled it.",
        "keywords": ["Problem-solving", "Initiative", "Outcome", "Resilience", "Learning", "Adaptability"],
        "answers": [
            "I had a tough project once but managed to complete it on time.",
            "I coordinated with my team under tight deadlines to deliver results successfully.",
            "I led a crisis response team to solve a critical issue, ensuring future preventive measures."
        ]
    },
    {
        "question": "How do you handle stress and pressure?",
        "keywords": ["Coping Mechanisms", "Resilience", "Time Management", "Prioritization", "Calmness", "Performance"],
        "answers": [
            "I try to stay calm and get the work done.",
            "I prioritize tasks and maintain open communication with my team.",
            "I thrive under pressure by employing strategic planning and mindfulness techniques."
        ]
    },
    {
        "question": "Why should we hire you?",
        "keywords": ["Fit", "Value Addition", "Skills", "Experience", "Contribution", "Uniqueness"],
        "answers": [
            "I have the skills and experience required for the job.",
            "My background and skills align well with the role's expectations.",
            "I bring unique expertise and a passion for innovation that would contribute to company growth."
        ]
    },
    {
        "question": "How do you prioritize your work?",
        "keywords": ["Time Management", "Organization", "Decision-Making", "Efficiency", "Planning", "Focus"],
        "answers": [
            "I make a list of tasks and try to complete them.",
            "I assess urgency, structure my plan, and allocate time effectively.",
            "I use the Eisenhower Matrix and project management tools to track and complete tasks efficiently."
        ]
    },
    {
        "question": "How do you handle conflict in the workplace?",
        "keywords": ["Communication", "Resolution", "Empathy", "Professionalism", "Collaboration", "Diplomacy"],
        "answers": [
            "I try to avoid conflicts and focus on my work.",
            "I address conflicts by engaging in open dialogue and understanding different perspectives.",
            "I see conflicts as opportunities to foster teamwork, communication, and growth."
        ]
    }
]

# Insert into MongoDB
questions3_collection.insert_many(hr_questions)

print("HR questions inserted successfully into 'questions3_collection'!")

'''
