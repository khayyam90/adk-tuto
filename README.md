[![Python](https://img.shields.io/badge/python-3.10%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Google ADK](https://img.shields.io/badge/Google%20ADK-latest-4285F4?style=flat-square&logo=google)](https://google.github.io/adk-docs/)

# Installation

```
python -m venv .env
source .env/bin/activate
python3 -m pip install -r requirements.txt
```


# Run

`adk run OutfitAgent`

# Discovering Google ADK - Agent Development Kit

ADK is an open source development framework to build and run your AI agents. I will present here an introduction to ADK illustrated in Python.

## What is an AI agent ?

An AI agent is an autonomous program that can understand its environment and use tools to achieve a specific goal.
An AI agent must be dedicated to a specific basic role that needs LLM capabilities. The common example is the customer client multi-agent system that runs multiple specific agents : 
* an agent to understand a textual customer query
* an agent to explore the internal company FAQ
* an agent to explore the CRM and query the customer informations
* an agent to trigger an individual marketing action

All these agents can be mutualized between several departments and a combination of them will create the customer service.
An agent will run as an infinite loop waiting for incoming prompts. 

## What is an AI tool ?

An AI agent can reason through a LLM but it cannot know your internal and private data (customer data, banking data, industrial knowledge…) But you can indicate to the LLM what parts of the answer depend on your private data and how to collect them. 
By describing the capabilities and the input/output, the LLM will be able to formulate an execution plan with sequential (or parallel) queries based on incremental results. 
Describing an AI tool is giving to your LLM the capability to think on your internal data while keeping your data protected. Each tool is auto-described so the LLM can decide by itself when to use it and with which inputs. 
Describing AI tools can also give capabilities to your agent to act on thinkgs outside of your program : 
* send mails, SMS
* call third part APIs
* start an external workflow 
…

ADK installation (on Python environment)
pip install google-adk
Create a new Python project and define the APIkeys

## Example : Outfit agent

Let's try to create a basic agent : I would like to have every morning an outfit proposition focused on the weather in my location. 

![/assets/images/san-juan-mountains.jpg](https://cdn-images-1.medium.com/max/1200/1*c-vDY0uU29lAxADceX7roA.png "Execution plan")

Execution flowThe execution plan will produce a graph of multiple calls to end up by the production of a textual proposition. The agent execution will implement the LangGraph paradigm.

Google ADK proposes an easy way to define agents : 

```
from google.adk.agents.llm_agent import Agent
from ip_location import get_current_city
from weather import get_weather

def getCurrentCity() -> str:
    """Returns the user's city"""
    return get_current_city()

def getCityWeather(city: str) -> str:
    """Returns the weather in a given city"""
    return get_weather(city)

root_agent = Agent(
    model='gemini-3.1-flash-lite-preview',
    name='root_agent',
    description="Gets the best outfit for the weather",
    instruction="You are a helpful assistant that tells what is the best pertinent outfit according to the weather. Use the 'getCurrentCity' tool to know the user's city and use 'getCityWeather' to get the weather in a given city.",
    tools=[getCurrentCity, getCityWeather],
)
```

You can notice the declaration of 2 tools : getCurrentCity and getCityWeather. The LLM will decide by itself how to use them even if we can guess the ideal execution : getCurrentCity then getCityWeather then LLM based on weather conditions. 
## Execution

In console mode 
`adk run OutfitAgent`
in Web mode
`adk web --port 8000`

Execution result 
Input : "how should I wear ?"
Output : Since it's sunny in Paris, you should definitely opt for a light and comfortable outfit! Think breathable fabrics like cotton or linen. A t-shirt paired with shorts or a breezy skirt would be perfect. Don't forget your sunglasses, a hat for extra protection, and comfortable walking shoes if you're heading out!