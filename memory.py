from embeddings import Embeddings
from utils import MEMORY_NEED_PROMPT, SUMMARY_ENOUGH_CHECK_PROMPT, SUMMARIZATION_PROMPT, HISTORY_BASED_PROMPT

class MemoryManager:
    def __init__(self, model) -> None:
        self.embeddings_model = Embeddings()
        self.model = model
        self.history = []
        self.history_embeddings = []
    
    def getEmbeddings(self, text):
        return self.embedding_model.get([text])

    def isMemoryNeeded(self,content):
        prompt = MEMORY_NEED_PROMPT.format(user_input = content)
        completion = self.model.get_completion_without_history(prompt)
        return "(A)" in completion
    
    def isSummaryEnough(self,content):
        prompt = SUMMARY_ENOUGH_CHECK_PROMPT.format(user_input = content)
        completion = self.model.get_completion_without_history(prompt)
        return "(A)" in completion
    
    def summarize(self, user_prompt, completion):
        prompt = SUMMARIZATION_PROMPT.format(user_input = user_prompt, system_response= completion)
        return self.model.get_completion_without_history(prompt)

    def completionWithHistory(self,history_of_related_turn, previous_user_input, previous_system_response, current_user_input):
        prompt = HISTORY_BASED_PROMPT.format(history_of_related_turn = history_of_related_turn, 
                                             previous_user_input= previous_user_input,
                                             previous_system_response= previous_system_response,
                                             current_user_input= current_user_input)
        return self.model.get_completion_without_history(prompt)

    






        