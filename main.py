from models import ChatGPT, GPT3
from memory import MemoryManager


agent = GPT3()
memoryManager = MemoryManager(agent)
while True:
    prompt = input("User:")
    decision = memoryManager.decideMemoryNeed(prompt)
    print("decision:",decision)
