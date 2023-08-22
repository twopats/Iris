import json
from semantic_kernel import Kernel
from semantic_kernel.skill_definition import sk_function
from semantic_kernel.core_skills.file_io_skill import FileIOSkill
from semantic_kernel.orchestration.sk_context import SKContext


class OrchestratorPlugin:
    def __init__(self, kernel: Kernel):
        self._kernel = kernel

    @sk_function(
        description="Routes the request to the appropriate function",
        name="route_request",
    )
    async def RouteRequest(self, context: SKContext) -> str:
        print("###RouteRequest")

        # Save the original user request
        request = context["input"]

        GetIntent = self._kernel.skills.get_function("OrchestratorPlugin", "GetIntent")

        CreateResponse = self._kernel.skills.get_function(
            "OrchestratorPlugin", "CreateResponse"
        )
        await GetIntent.invoke_async(context=context)
        intent = context["input"].strip()
        print("Intent: ", intent)

        file_skill = self._kernel.import_skill(FileIOSkill(), skill_name="file_skill")

        # Call the appropriate function
        if intent == "Read":
            mainFunction = file_skill["readAsync"]
        elif intent == "Write":
            mainFunction = file_skill["writeAsync"]
        else:
            return "I'm sorry, I don't understand."

        # Create a new context object with the original request
        pipelineContext = self._kernel.create_new_context()
        pipelineContext["original_request"] = request
        pipelineContext["input"] = request

        # Run the functions in a pipeline
        output = await self._kernel.run_async(
            mainFunction,
            input_context=pipelineContext,
        )
        return output["input"]
