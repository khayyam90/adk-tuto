from google.adk.agents.llm_agent import Agent
from ip_location import get_current_city
from weather import get_weather

def getCurrentCity() -> str:
    """Returns the user's city"""
    return get_current_city()

def getCityWeather(city: str) -> str:
    """Returns the weather in a given city"""
    return get_weather(city)['condition']

root_agent = Agent(
    model='gemini-3.1-flash-lite-preview',
    name='root_agent',
    description="Gets the best outfit for the weather",
    instruction="You are a helpful assistant that tells what is the best pertinent outfit according to the weather. Use the 'getCurrentCity' tool to know the user's city and use 'getCityWeather' to get the weather in a given city.",
    tools=[getCurrentCity, getCityWeather],
)