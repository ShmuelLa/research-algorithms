import gspread
import networkx as nx
import pandas as pd
from fairpy.agents import AdditiveAgent
from fairpy.items.allocations_fractional import FractionalAllocation
from fairpy.items.pareto_improvement import ParetoImprovement


def get_input():
    account = gspread.service_account("creds.json")
    spreadsheet = account.open_by_key('1BdSeJ0uOmnJijWa460BmgyjAKBpVFiQ-6QONHN3Ip4U')

    sheet = spreadsheet.worksheet("Input")
    df = pd.DataFrame(sheet.get_all_records())

    items_list = [col.split('-')[0] for col in df if 'valuation' in col]
    items = set(items_list)
    agent_names = df['name'].tolist()

    agents_list = []
    agents_allocation_list = []
    for agent_name in agent_names:
        agent_valuation_dict = {}
        agent_allocation_dict = {}
        for x in df.itertuples():
            if x[1] == agent_name:
                for item_i in range(len(items)):
                    agent_valuation_dict[items_list[item_i]] = x[item_i + 2]
                    agent_allocation_dict[items_list[item_i]] = float(x[item_i + 2 + 1 + len(items)])
        agents_list.append(AdditiveAgent(agent_valuation_dict, name=agent_name))
        agents_allocation_list.append(agent_allocation_dict)

    fr_allocation = FractionalAllocation(agents_list, agents_allocation_list)
    return fr_allocation, items


def post_output(output: str):
    account = gspread.service_account("creds.json")
    spreadsheet = account.open_by_key('1BdSeJ0uOmnJijWa460BmgyjAKBpVFiQ-6QONHN3Ip4U')

    sheet = spreadsheet.worksheet("Output")
    sheet.update('A1', str(output))


if __name__ == "__main__":
    initial_allocation, all_items = get_input()
    pi = ParetoImprovement(initial_allocation, all_items)
    post_output(pi.find_pareto_improvement())

