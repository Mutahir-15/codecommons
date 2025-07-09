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

### Gemini AI Chat Completion Integration
This file contains a Python script that demonstrates how to integrate the Gemini API (via Google Generative Language) with the Agents SDK using an OpenAI-compatible interface. The script sets up a basic configuration to execute agents with Gemini models.


### Features

- Utilizes the Agents SDK for modular agent development.
- Implements an OpenAI-style interface for compatibility with Gemini models.
- Securely fetches API keys from environment variables.
- Supports multiple Gemini models with configurable options.

### Prerequisites

- Python 3.x 
- agents library (install via pip: pip install agents or uv: uv add openai_agents)
- python-dotenv library (install via pip: pip install python-dotenv)
- A .env file with your Gemini API key (e.g., GEMINI_API_KEY=your_api_key_here)
- Install the required dependencies:pip install agents python-dotenv


### Usage
**Code Overview**


The script performs the following steps:

- Imports Required Modules: Loads necessary modules from the Agents SDK and environment loader.
- Loads Environment Variables: Retrieves the Gemini API key from a .env file.
- Configures the Client: Sets up an OpenAI-compatible client using Gemini's endpoint.
- Defines the Model: Initializes a chat completion model with a specific Gemini model (e.g., gemini-2.0-flash).
- Creates Run Configuration: Prepares a configuration for executing agents with the defined model and client.


### Running the Script

Ensure all prerequisites are met.
Run the script:
```
python your_script_name.py
```
**If using UV (Recommended): [Introduction to UV (Universal Virtualenv)](https://github.com/Mutahir-15/codecommons/tree/main/01_agentic_ai/02_uv)**
```
uv run your_script_name.py
```

---


### Code Explanation
**Imports**
```
from agents import OpenAIChatCompletionsModel, AsyncOpenAI
from agents.run import RunConfig
import os  # Needed for os.getenv to work
```

- **OpenAIChatCompletionsModel** and *AsyncOpenAI** are used to create an OpenAI-compatible interface.
- **RunConfig** is used to configure agent execution.
- **os** is used to load environment variables.

**Environment Setup**
```
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
```

- **load_dotenv()** loads variables from the .env file.
- **API_KEY** securely retrieves the Gemini API key.

**Client Configuration**
```
external_client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
```

- Configures an external client compatible with Gemini's endpoint.

**Model Definition**
```
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",  # You can change it to other Gemini models
    openai_client=external_client,
)
```

- Defines the chat completion model using the Gemini **gemini-2.0-flash** model (configurable to other Gemini models).

**Run Configuration**
```
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,  # its optional, disables SDK trace logging
)
```

- Sets up the run configuration with the model, client, and optional tracing disabled.

**Customization**
- **Change Models:** Modify the **model** parameter in **OpenAIChatCompletionsModel** to use other Gemini models (e.g., gemini-1.0-pro).
- **Update API Key:** Ensure the **.env** file contains the correct **GEMINI_API_KEY**.
- **Enable Tracing:** Set **tracing_disabled=False** in **RunConfig** for SDK trace logging.

---


**Contributing**

Feel free to fork this repository, submit issues, or create pull requests to improve the project.


**License**

This project is licensed under the MIT License - see the LICENSE file for details.
