import requests

class LLMIntegration:
    def __init__(self, api_key, personality):
        self.api_key = api_key
        self.personality = personality

    def generate_prompt(self, messages, personality):
        conversation = "\n\n".join(messages)
        prompt = f"{personality}: {conversation}"
        return prompt

    def get_response(self, prompt):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7,
            "n": 1,
            "stop": None
        }
        response = requests.post("https://api.openai.com/v1/engines/davinci-codex/completions", headers=headers, json=data)
        response_json = response.json()
        return response_json["choices"][0]["text"].strip()

    def generate_response(self, messages):
        prompt = self.generate_prompt(messages, self.personality)
        response = self.get_response(prompt)
        return response