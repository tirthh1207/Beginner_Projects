from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Load model
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generator",
    temperature=0.5
)

model = ChatHuggingFace(llm=llm)

# Memory string
memory = ""

# -------- Memory summarizer prompt --------

memory_prompt = PromptTemplate(
    template="""
You are a memory summarizer.

Old memory:
{old_memory}

New user message:
{new_message}

Update the memory in short form (keep important facts only):
""",
    input_variables=["old_memory", "new_message"]
)

# -------- Chat prompt --------

chat_prompt = PromptTemplate(
    template="""
You are a helpful chatbot assistant.

Chat memory:
{memory}

User:
{user_input}

Reply naturally:
""",
    input_variables=["memory", "user_input"]
)

# -------- Main loop --------

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    # Update memory
    memory_result = model.invoke(
        memory_prompt.format(
            old_memory=memory,
            new_message=user_input
        )
    )

    memory = memory_result.content

    # Get chatbot reply
    chat_result = model.invoke(
        chat_prompt.format(
            memory=memory,
            user_input=user_input
        )
    )

    print("Bot:", chat_result.content)
