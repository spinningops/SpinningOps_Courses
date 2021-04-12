# THIS WILL GET THE CURRENT BILLING FROM AWS FOR THE CURRENT MONTH
# pip3 install boto3
# pip3 install termcolor

import boto3
import pprint
from datetime import date
from termcolor import colored


# get today's date
today = date.today()
# get current month
month = today.strftime("%Y-%m-01")
client = boto3.client('ce', region_name='us-east-1')


def costExplorerAmount():
    '''
        Get the current billing amount. 
    '''
    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': str(month),
            'End': str(today)
        },
        Granularity='MONTHLY',
        Metrics=[
            'NetUnblendedCost',
        ]
    )

    pretty_dict_str = pprint.pformat(response['ResultsByTime'][0]['Total']['NetUnblendedCost']['Amount'])

    # This removes the ' at the start of the string amount and removes after the float .
    amount_output = pretty_dict_str[1:pretty_dict_str.index('.')]
    return 'The current billing amount is: $' + colored(amount_output, 'red')

    
print(costExplorerAmount())