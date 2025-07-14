# Hello World Agent

Welcome to the **"Hello World Agent"**! This project demonstrates a basic implementation of an AI agent using the **Agents SDK** with the **Gemini API**, integrated via an **OpenAI-compatible interface**.
The agent responds to a simple question about the fundamental pillars of Object-Oriented Programming (OOP) in Python.

### Features

- Utilizes the Agents SDK for agent creation and execution.
- Integrates the Gemini API with an OpenAI-style interface.
- Configures a basic agent with custom instructions.
- Demonstrates asynchronous execution with asyncio.

### Prerequisites

- Python 3.x
- agents library (install via **uv add openai-agents**)
- python-dotenv library (install via **uv add python-dotenv**)
- A .env file with your Gemini API key (e.g., **GEMINI_API_KEY=your_api_key_here**)

### Installation

- Make sure UV is installed in your system, if not read this: **[What is UV?)](https://github.com/Mutahir-15/codecommons/tree/main/01_agentic_ai/02_uv)**
- Clone the repository:
```
git clone https://github.com/Mutahir-15/codecommons/tree/main/01_agentic_ai/03_hello_world_agent.git
```
- Create a .env file in the root directory and add your Gemini API key here
```
GEMINI_API_KEY=your_api_key_here
```
- Install the required dependencies:
```
uv add openai-agents
uv add python-dotenv
```


### Usage
**Running the Script**

- Ensure all prerequisites are met.
- Execute the script:
```
uv run main.py
```
**This will run the agent and print the response to the question "What are fundamental pillars of OOP in Python?".**

--- 

### Code Explanation
**Imports**
```
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI
from agents.run import RunConfig
import os
import asyncio
from dotenv import load_dotenv
```

- **Key Concept: Module Imports** - Imports essential modules from the Agents SDK **(Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig)** and standard libraries **(os, asyncio, dotenv)** for environment handling and asynchronous operations.

### Environment Setup
```
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not set. Please add the API key to your .env file.")
```
- **Key Concept: Secure Configuration** - Loads environment variables from a .env file and validates the presence of the Gemini API key, ensuring secure and flexible key management.

### Client Initialization
```
external_client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
```
- **Key Concept: API Integration** - Initializes an asynchronous OpenAI client with the Gemini API key and base URL, enabling compatibility with Gemini's endpoint.

### Model Configuration
```
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)
```
- **Key Concept: Model Selection** - Creates an instance of OpenAIChatCompletionsModel using the gemini-2.0-flash model, showcasing how to specify a model for the agent.

### Run Configuration
```
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)
```
- **Key Concept: Run Settings** - Defines the configuration for agent execution, including the model, provider, and an option to disable tracing for performance optimization.

### Agent Definition and Execution
```
async def main():
    agent = Agent(
        name="Assistant Agent",
        instructions="You are a helpful assistant.",
        model=model
    )
    result = await Runner.run(agent, "What are fundamental pillars of OOP in Python?", run_config=config)
    print(result.final_output)
```
- **Key Concept: Agent Creation and Async Execution** - Defines an agent with a name, instructions, and model, then uses Runner.run to execute it asynchronously with a specific query. The result is printed to the console.
- **Key Concept: OOP Pillars** - The query targets fundamental OOP principles (Encapsulation, Inheritance, Polymorphism, Abstraction), highlighting the agent's capability to handle domain-specific questions.

# Script Entry Point
```
if __name__ == "__main__":
    asyncio.run(main())
```
- **Key Concept: Script Execution**- Ensures the main function runs only when the script is executed directly, adhering to Python best practices for modular code.

### Customization
- **Change Model:** Update model="gemini-2.0-flash" to other Gemini models (e.g., gemini-1.0-pro).
- **Modify Question:** Adjust the query in Runner.run to explore different topics.

### Contributing
Feel free to fork this repository, submit issues, or create pull requests to enhance the project.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
