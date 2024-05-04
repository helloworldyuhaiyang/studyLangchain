from langchain.memory import ChatMessageHistory
from langchain.memory import ConversationBufferMemory

history = ChatMessageHistory()

history.add_user_message("hi!")

history.add_ai_message("whats up?")

print(history)

memory = ConversationBufferMemory()
memory.chat_memory.add_user_message("hi!")
memory.chat_memory.add_ai_message("whats up?")
print(memory.chat_memory)

