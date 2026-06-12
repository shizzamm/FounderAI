import json

from agents import idea_agent
from agents import market_agent
from agents import business_agent
from agents import pm_agent
from agents import cto_agent
from agents import investor_agent
from agents import critic_agent
from agents import improvement_agent
from agents import comparison_agent


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

print("\nRunning Improvement Agent...")
improved_idea = improvement_agent.run(
    idea,
    critic
)

print("\nRunning Comparison Agent...")
comparison = comparison_agent.run(
    idea,
    improved_idea,
    critic
)

report = {
    "idea": idea,
    "market": market,
    "business": business,
    "product": product,
    "cto": cto,
    "investor": investor,
    "critic": critic,
    "improved_idea": improved_idea,
    "comparison": comparison
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