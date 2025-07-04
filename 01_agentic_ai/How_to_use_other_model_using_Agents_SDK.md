# Do you know the importance of this code?

```
# Imports required modules from the Agents SDK and environment loader
from agents import OpenAIChatCompletionsModel, AsyncOpenAI
from agents.run import RunConfig
from dotenv import load_dotenv
import os	# Needed for os.getenv to work

# It loads environment variable from .env file
load_dotenv()

# Fetch your Gemini API Key securely
API_KEY = os.getenv("GEMINI_API_KEY")

# This configure OpenAI compatible client using Gemini's endpoint
external_client = AsyncOpenAI (
    api_key= API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Define the model using Gemini via OpenAI style interface
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",	# You can change it to other Gemini models
    openai_client= external_client,
)

# Create a run configuration for executing agents
config = RunConfig(
    model=model
    model_provider= external_client,
    tracing_disabled=True,	# its optional, disables SDK trace logging
)
```
---

This small snippet is a bridge between two giants:
Google's Gemini model and OpenAI's Agentic AI SDK.

✅ OpenAI-style interaction using Gemini
✅ Use any OpenAI-compatible tool (tool calling, planning, etc.)
✅ Great for building real AI agents — not just chatbots

If you’re working on Agentic AI, this is your starting point to mix OpenAI SDKs with Gemini’s power.

Let’s build agents that think, decide, and act. 🚀
