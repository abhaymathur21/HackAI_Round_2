from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low
import requests

class Message(Model):
    value: str
    
local_agent = Agent(
    name="local_agent",
    seed="local_agent_seed",
    port=8001,
    endpoint=["http://127.0.0.1:8001/submit"],
)
# print(local_agent.address)

@local_agent.on_interval(period=100000)
async def message_handler(ctx:Context):
    query_message = input("Enter a message: ")
    # query_message = "iPhone 9"
    print(query_message)
    await ctx.send("agent1qw76h6w8ns93rqa6ye5hyd4xj0k97nl2fk9xepes0dayqhr8c57qw45nye0", Message(value=query_message))
    
if __name__ == "__main__":
    fund_agent_if_low(local_agent.wallet.address())
    local_agent.run()
