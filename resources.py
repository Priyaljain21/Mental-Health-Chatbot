class MentalHealthResources:
    @staticmethod
    def get_crisis_resources():
        return {
            "emergency": "911",
            "suicide_prevention": "988",
            "crisis_text": "Text HOME to 741741",
            "samhsa": "1-800-662-4357"
        }

    @staticmethod
    def get_mental_health_information():
        return [
            {
                "topic": "Depression",
                "description": "Depression is a common but serious mood disorder that affects how you feel, think, and handle daily activities.",
                "symptoms": [
                    "Persistent sad, anxious, or empty mood",
                    "Loss of interest in activities",
                    "Difficulty sleeping or oversleeping",
                    "Changes in appetite",
                    "Difficulty concentrating"
                ]
            },
            {
                "topic": "Anxiety",
                "description": "Anxiety disorders involve more than temporary worry or fear. The anxiety does not go away and can get worse over time.",
                "symptoms": [
                    "Excessive worry",
                    "Restlessness",
                    "Difficulty concentrating",
                    "Sleep problems",
                    "Physical symptoms like rapid heartbeat"
        ]
    }
]   