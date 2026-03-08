from smolagents import ToolCallingAgent, WebSearchTool, InferenceClientModel
import gradio as gr
import os

model = InferenceClientModel(
    api_key=os.environ["HFToken"],
    model_id="moonshotai/Kimi-K2.5",
    provider="together",
    max_tokens=300
)

agent = ToolCallingAgent(
    tools=[WebSearchTool()],
    model=model,
    instructions="""
    You are an intelligent AI research assistant.
    Search the web when needed.
    Provide clear answers with sources.
    Keep responses short and helpful.
    """
)

def run_agent(message, history):
    return agent.run(message)

gr.ChatInterface(
    fn=run_agent,
    title="Sashank's AI Web Search Agent",
    description="Ask any question — I can search the web for answers.",
    theme=gr.themes.Soft()
).launch()