import os
from dotenv import load_dotenv
import openai
import utils
import copy

load_dotenv()

OPENAI_KEY = os.getenv('OPENAI_KEY')
openai.api_key = OPENAI_KEY


class OpenAIModel:
    def __init__(self, model):
        self.model = model
        self.next_roles = {
            "user":"assistant",
            "assistant":"user"
            }
        self.messages = []

    def getRole(self, messages):
        if len(messages) % 2 == 0:
            return "user"
        return "assistant"

    def get_completion(self,content):
        self.addMessage(content)
        completion = self.get_output()
        self.addMessage(completion)
        return completion
    
    def get_completion_without_history(self,content):
        completion = self.get_output(content)
        return completion


class ChatGPT(OpenAIModel):
    def __init__(self, model = "gpt-3.5-turbo", system_message=""):
        super().__init__(model)
        if system_message:
            self.messages = [{"role": "system", "content" :system_message}]
        else:
            c_time = utils.get_current_date()
            self.messages = [{"role": "system", "content" : f"You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible.\nKnowledge cutoff: 2021-09-01\nCurrent date: {c_time}"}]
        
        self.start_messages = copy.deepcopy(self.messages)

    def addMessage(self,content):
        role = self.getRole(self.messages)
        message = {"role": role, "content":content}
        self.messages.append(message)
    
    def get_output(self, prompt=None):
        if prompt:
            result = openai.ChatCompletion.create(
                model=self.model,
                messages = self.start_messages.extend([{"role":"user","content":prompt}])
                )
        else:
            result = openai.ChatCompletion.create(
                model=self.model,
                messages = self.messages
            )
        completion = result["choices"][0]["message"]["content"]
        return completion

class GPT3(OpenAIModel):
    def __init__(self, model = "text-davinci-003"):
        super().__init__(model)
        self.prompt = "user: "
        self.seperator = "\n#####\n"
        self.role=""
    
    def addMessage(self,content):
        messages = self.prompt.split(self.seperator)
        role = self.getRole(messages)
        next_role = self.next_roles[role]
        self.prompt = self.prompt + content + self.seperator + next_role +": "
    
    def get_output(self, prompt=None):
        if prompt:
            completion = openai.Completion.create(model=self.model, prompt=prompt)
        else:
            completion = openai.Completion.create(model=self.model, prompt=self.prompt)
        return completion.choices[0].text




