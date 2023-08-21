import semantic_kernel as sk
import os
from semantic_kernel.connectors.ai.open_ai import OpenAITextCompletion
from dotenv import dotenv_values 

skills_dir = "./src/skills"

API_KEY = dotenv_values(".env")["OPENAI_API_KEY"]

kernel = sk.Kernel()



kernel = sk.Kernel()

kernel.add_text_completion_service(               # We are adding a text service
    "OpenAI_davinci",                         # The alias we can use in prompt templates' config.json
    OpenAITextCompletion(
        "text-davinci-003",                   # OpenAI Model Name
        API_KEY
    )
)



jokeFunction = kernel.import_semantic_skill_from_directory(skills_dir, "FunSkill")["Joke"]

result = jokeFunction("the weather in new york city")
print(result)