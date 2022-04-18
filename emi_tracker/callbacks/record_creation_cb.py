
# coding=utf-8
"""
==============================================================================
Purpose:   This module serves as a callback for new emi record creation

Author:    Shashank Gupta.
Created:   5/30/2021.
==============================================================================
"""


import dash
from dash.dependencies import Input, Output
from datetime import datetime
import pandas as pd
from pathlib import Path

from emi_tracker.server import app

print("record creation callback registered...")


@app.callback(
    [Output('id-alert-record-creation', 'is_open'),
     Output('id-alert-record-creation', 'children'),
     Output('id-alert-record-creation', 'color')],
    [Input(component_id='submit-values', component_property='n_clicks'),
     # Input(component_id='bank_name', component_property='value'),
     Input(component_id='id-lender-dropdown', component_property='value'),
     Input(component_id='total_amount', component_property='value'),
     Input(component_id='emi_tenure', component_property='value'),
     Input(component_id='id-emi-per-month', component_property='value'),
     Input(component_id='merchant_info', component_property='value'),
     Input(component_id='description', component_property='value'),
     Input(component_id='transact_date', component_property='value'),
     Input(component_id='id-emi-start-radioitems', component_property='value')]
)
def create_new_record(n_clicks, bank, amount, tenure, emi_pm, merchant, description, tdate, emi_month):

    if n_clicks == 0:
        return False, '', ''
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'submit-values' in changed_id:
        print("tdate is: ", tdate)
        if _check_tdate_validity(tdate):
            print("starting process")
            try:
                csv_file = Path("emi_records.csv")
                if csv_file.is_file():
                    # append
                    print("file exists, so appending..")
                    df = pd.DataFrame({'Bank': [bank], 'Amount': [amount], 'Transact Date': [tdate], 'Tenure': [tenure],
                                       'Emi Per Month': [emi_pm], 'Merchant': [merchant], 'Description': [description],
                                       "EMI Start": [emi_month]})
                    df.to_csv("emi_records.csv", mode='a', header=False, index=False)
                else:
                    # create new
                    print("creating new file..")
                    df = pd.DataFrame({'Bank': [bank], 'Amount': [amount], 'Transact Date': [tdate], 'Tenure': [tenure],
                                       'Emi Per Month': [emi_pm], 'Merchant': [merchant], 'Description': [description],
                                       "EMI Start": [emi_month]})
                    df.to_csv("emi_records.csv", index=False)
                return True, 'Record Created', 'success'
            except Exception as e:
                print("exception: ", e)
                return False
        else:
            print("Not creating record...")
            return True, 'Wrong date entered', 'danger'
    else:
        print("Button is not clicked, something else is changed.")
        return False, '', ''


def _check_tdate_validity(t_date):
    try:
        _date = datetime.strptime(t_date, '%d/%m/%Y')
        return True
    except (ValueError, TypeError) as ex:
        print("date validity exception: ", ex)
        return False
