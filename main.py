import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAITextCompletion

kernel = sk.Kernel()


api_key = sk.openai_settings_from_dot_env()

kernel = sk.Kernel()

kernel.add_text_completion_service(               # We are adding a text service
    "OpenAI_davinci",                         # The alias we can use in prompt templates' config.json
    OpenAITextCompletion(
        "text-davinci-003",                   # OpenAI Model Name
        api_key
    )
)

