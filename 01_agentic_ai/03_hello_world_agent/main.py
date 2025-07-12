# Import necessary modules
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI
from agents.run import RunConfig
import os
import asyncio
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up the Gemini API key
API_KEY = os.getenv("GEMINI_API_KEY")

# Check if the API key is set otherwise raise an error
if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not set. Please add the API key to your .env file.")

# Initialize the OpenAI client with the API key and base URL
external_client = AsyncOpenAI (
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Create an instance of the OpenAIChatCompletionsModel with the external client
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# Configure the run settings for the agent
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Define the main function to run the agent
async def main():
    
    # Create an instance of the Agent with the specified model and instructions
    agent = Agent(
        name="Assistant Agent",
        instructions="You are a helpful assistant.",
        model=model
    )

    # Run the agent with a specific question
    result = await Runner.run(agent, "What are fundamental pillars of OOP in Python?", run_config=config)

    # Print the final output of the agent
    print(result.final_output)

# Entry point for the script
# This will execute the main function when the script is run
if __name__ == "__main__":
    asyncio.run(main())