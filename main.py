import json

from agents import idea_agent
from agents import market_agent
from agents import business_agent
from agents import pm_agent
from agents import cto_agent
from agents import investor_agent
from agents import critic_agent


startup_idea = input(
    "Enter startup idea: "
)

print("\nRunning Idea Agent...")
idea = idea_agent.run(
    startup_idea
)

print("\nRunning Market Agent...")
market = market_agent.run(
    idea
)

print("\nRunning Business Agent...")
business = business_agent.run(
    idea,
    market
)

print("\nRunning PM Agent...")
product = pm_agent.run(
    idea,
    market,
    business
)

print("\nRunning CTO Agent...")
cto = cto_agent.run(
    product
)

print("\nRunning Investor Agent...")
investor = investor_agent.run(
    idea,
    market,
    business,
    product,
    cto
)

print("\nRunning Critic Agent...")
critic = critic_agent.run(
    idea,
    market,
    business,
    product,
    cto,
    investor
)

report = {
    "idea": idea,
    "market": market,
    "business": business,
    "product": product,
    "cto": cto,
    "investor": investor,
    "critic": critic
}

with open(
    "outputs/startup_report.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        report,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nFounderAI Report Generated!")

print("\n====================")

print(
    json.dumps(
        report,
        indent=4,
        ensure_ascii=False
    )
)