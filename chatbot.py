from transformers import AutoTokenizer, AutoModelForCausalLM
import random

class MentalHealthBot:
    def __init__(self):
        model_name = "gpt2"  
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.emotional_responses = {
            "sad": [
                "I'm really sorry you're feeling down. It's okay to not be okay, and talking about it can help.",
                "It's completely normal to feel sad sometimes. Would you like to share what's going on?"
            ],
            "happy": [
                "I'm so glad to hear you're feeling happy! What's been making you feel this way?",
                "That's great! Positive feelings are so important. What's been bringing you joy lately?"
            ],
            "anxious": [
                "I can understand how anxiety can feel overwhelming. Would you like to talk about what's on your mind?",
                "It's okay to feel anxious. You're not alone in this, and I'm here to listen if you'd like to share."
            ],
            "angry": [
                "I'm sorry you're feeling angry. Sometimes it helps to express what's making you feel this way.",
                "Anger is a powerful emotion. If you'd like, we can talk about what's been frustrating you."
            ],
            "upset": [
                "I'm really sorry you're feeling upset. It's tough when emotions feel overwhelming. Want to talk about what's bothering you?",
                "It’s okay to feel upset, and it’s important to express those emotions. I’m here to listen if you want to share."
            ],
            "negative": [
                "I'm sorry you're feeling this way. It's okay to have tough days, and I'm here to listen if you'd like to share.",
                "It sounds like you're going through a hard time. Remember, you don’t have to go through it alone. Would you like to talk about it?"
            ],
            "I got rejected again today.": [
                "I'm sorry you're feeling this way. It's okay to have tough days, and I'm here to listen if you'd like to share.",
                "It sounds like you're going through a hard time. Remember, you don’t have to go through it alone. There are some bad days here and there but that doesn't mean good days are around thr corner and plus you know you always haveme to talk to."
            ],
            "I nailed my interview": [
                "I'm so glad to hear that. You are definately going to get that job!",
                "That's great! What an incredible news. This calls for a celebration innit?"
            ]
        }

    def get_response(self, prompt):
        clean_prompt = prompt.lower().strip()

        # Detect emotion from prompt using keywords and negation
        emotion = self.detect_emotion(clean_prompt)

        if emotion:
            return self.get_emotional_response(emotion)

        # If no specific emotion is detected, use model to generate a general response
        return self.get_model_response(clean_prompt)

    def detect_emotion(self, prompt):
        # Handle negation like "not happy", "not good"
        if "not happy" in prompt or "not good" in prompt or "feeling down" in prompt or "feeling bad" in prompt:
            return "negative"  # Assign to negative emotion if negation is detected

        # Simple emotion detection using positive keywords
        emotions = {
            "sad": ["sad", "down", "blue", "unhappy", "depressed"],
            "happy": ["happy", "good", "great", "joy", "feeling good"],
            "anxious": ["anxious", "nervous", "worried", "stressed"],
            "angry": ["angry", "frustrated", "mad", "irritated"],
            "upset": ["upset", "distressed", "disappointed", "bothered"]
        }

        # Check for matching emotions in the prompt
        for emotion, keywords in emotions.items():
            if any(keyword in prompt for keyword in keywords):
                return emotion
        
        return None

    def get_emotional_response(self, emotion):
        # Return a predefined response based on the detected emotion
        return random.choice(self.emotional_responses[emotion])

    def get_model_response(self, prompt):
        # Generate a response from the model for general conversation
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(
            **inputs,
            max_length=100,  # Limit response length to avoid excessive output
            temperature=0.7,  # Moderate creativity
            top_p=0.9,  # Nucleus sampling
            repetition_penalty=1.5,  # Penalize repeated text
            no_repeat_ngram_size=3,  # Prevent repeated n-grams
            top_k=50  # Top-k sampling
        )

        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        response = self.filter_repetitions(response)
        return response

    def filter_repetitions(self, response):
        # Break the response into sentences and remove duplicates
        sentences = response.split(". ")
        unique_sentences = []
        for sentence in sentences:
            if sentence not in unique_sentences:
                unique_sentences.append(sentence)
        return ". ".join(unique_sentences)