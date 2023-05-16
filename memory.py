import faiss
from embeddings import Embeddings
from utils import MEMORY_NEED_PROMPT, SUMMARY_ENOUGH_CHECK_PROMPT, SUMMARIZATION_PROMPT, HISTORY_BASED_PROMPT

class MemoryManager:
    def __init__(self, model) -> None:
        self.embeddings_model = Embeddings()
        self.model = model
        self.history = []
        self.history_embeddings = []
        self.similarity_thr = 0.4
        self.relevance_coef = 1
        self.recency_coef = 1
        self.history_limit = 3
        self.index = faiss.IndexFlatIP(384)
    
    def getPrompt(self, prompt):
        embeddings = self.embeddings_model.get(prompt).reshape((1,-1))
        _, D, I = self.index.range_search(x=embeddings, thresh=self.similarity_thr)
        scores = []
        for index in I:
            score = self.relevance_coef * D[index] + self.recency_coef * index
            scores.append((index, score))
        
        scores = sorted(scores, key=lambda x: x[1],reverse=True)
        limit = min(self.history_limit,len(scores))
        indices = [score[0] for score in scores[:limit]]
        resulting_prompt = ""
        for index in indices:
            resulting_prompt += self.history[index] + "\n"
        
        return resulting_prompt
    
    def addPrompt(self,prompt):
        embeddings = self.getEmbeddings(prompt).reshape((1,-1))
        self.history.append(prompt)
        self.index.add(embeddings)
    
    def getCloseHistory(self, prompt):


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

    def getCompletion(self, prompt):
        self.addPrompt(prompt)


    






        