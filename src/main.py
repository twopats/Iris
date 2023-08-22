import semantic_kernel as sk
import os
from semantic_kernel.connectors.ai.open_ai import OpenAITextCompletion
from semantic_kernel.core_skills.file_io_skill import FileIOSkill
from dotenv import dotenv_values

from plugins.OrchestratorPlugin.OrchestratorPlugin import OrchestratorPlugin
from semantic_kernel.planning.basic_planner import BasicPlanner


async def main():
    skills_dir = "./src/skills"
    API_KEY = dotenv_values(".env")["OPENAI_API_KEY"]

    # Create a new kernel
    kernel = sk.Kernel()
    kernel.add_text_completion_service(
        "OpenAI_davinci", OpenAITextCompletion("text-davinci-003", API_KEY)
    )
    pluginsDirectory = "./src/plugins"
    kernel.import_semantic_skill_from_directory(pluginsDirectory, "OrchestratorPlugin")
    kernel.import_semantic_skill_from_directory(pluginsDirectory, "AssistantPlugin")

    orchestratorPlugin = kernel.import_skill(
        OrchestratorPlugin(kernel), "OrchestratorPlugin"
    )

    # Create new planner
    planner = BasicPlanner()

    ask = "hi"
    plan = await planner.create_plan_async(ask, kernel)
    print(plan)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
