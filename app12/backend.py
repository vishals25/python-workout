import os
from langchain_huggingface import HuggingFaceEndpoint

class Chatbot:
    def __init__(self):
        self.HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
        self.llm = HuggingFaceEndpoint(
            repo_id="huggingfaceh4/zephyr-7b-alpha", 
            huggingfacehub_api_token=self.HUGGINGFACEHUB_API_TOKEN,
            temperature= 0.3,  
            top_k=10,  
            top_p=0.95,
            return_full_text=False
        ) # type: ignore

    def get_response(self, question):
            response = self.llm.invoke(question)
            return response


if __name__ == "__main__":
    chatbot = Chatbot()
    print(chatbot.get_response("Write a joke on birds?"))
