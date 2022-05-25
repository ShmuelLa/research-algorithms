import gspread
import pandas as pd
from fairpy.agents import AdditiveAgent
from fairpy.items.allocations_fractional import FractionalAllocation
from fairpy.items.pareto_improvement import ParetoImprovement


class GSpreadParetoImprovement:

    def __init__(self):
        """
        Initializes the pareto improvement Google spreadsheet solver
        sets the service account and test worksheet we previously configured
        """
        self.account = account = gspread.service_account("creds.json")
        self.spreadsheet = account.open_by_key('1BdSeJ0uOmnJijWa460BmgyjAKBpVFiQ-6QONHN3Ip4U')

    def solve(self, sheet_name):
        """
        Solved the problem presented on the input sheet
        by using all the relevant class methods


        >>> gpi = GSpreadParetoImprovement()
        >>> gpi.solve('Input2')
        Received and uploaded result:
        agent1's bundle: {item 1,item 2,item 3 ,item 4},  value: 28.0
        <BLANKLINE>

        >>> gpi = GSpreadParetoImprovement()
        >>> gpi.solve('Input3')
        Received and uploaded result:
        agent1's bundle: {item 1,item 2,item 3 ,item 4},  value: -90.0
        <BLANKLINE>
        """
        fr_allocation, items = self.get_input(sheet_name)
        result_str = str(ParetoImprovement(fr_allocation, items).find_pareto_improvement())
        print("Received and uploaded result:")
        print(result_str)
        self.post_output(result_str)

    def get_input(self, sheet_name) -> tuple[FractionalAllocation, set]:
        """
        Fetches the input sheet from the spreadsheet, converts it to a Pandas
        dataframe and iterates over the data in order to create all
        the different object for the ParetoImprovement and FractionalAlLocation
        settings

        :return: FractionalAllocation of the input sheet content and an item set
        """
        i_sheet = self.spreadsheet.worksheet(sheet_name)
        df = pd.DataFrame(i_sheet.get_all_records())
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

    def post_output(self, output: str):
        """
        Posts the resulting output as string in the output sheet

        :param output: The pareto improvement algorithm output for the relevant input
        """
        o_sheet = self.spreadsheet.worksheet("Output")
        o_sheet.update('A1', str(output))


if __name__ == "__main__":
    gpi = GSpreadParetoImprovement()
    gpi.solve('Input')
    import doctest
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))

