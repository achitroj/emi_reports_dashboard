# Author: Shashank Gupta

# This is the first layout of the application

from time import sleep
from dash.dependencies import Output
from dash.dependencies import Input

import dash_core_components as dcc
import dash_html_components as html

# register callbacks
from callbacks import record_creation_cb
from callbacks import report_view_cb

from emi_tracker.layouts.navigation import get_navbar_layout
from emi_tracker.layouts.record_dashboard_layout import RecordDashboardLayout
from emi_tracker.layouts.report_view_dashboard_layout import ReportViewDashboardLayout
from emi_tracker.server import app


app.layout = html.Div([dcc.Location(id='url', refresh=False), html.Div(id='page-content')], style={'width': '100%'})
view_report = ReportViewDashboardLayout()
add_new = RecordDashboardLayout()


@app.callback(Output('page-content', 'children'),
               #Output('nav-link-view', 'classname'),
               #Output('nav-link-add', 'classname')],

              [Input('url', 'pathname')])
def get_page_layout(path):
    if path == '/view':
        print("path is: ", path)
        # sleep(5)
        return html.Div([
            get_navbar_layout(),
            html.Div([view_report.get_view_dashboard_layout()])

        ]) # , 'selected_dashboard_style', ''
    elif path == '/add':
        print("path is: ", path)
        # sleep(5)
        return html.Div([
            get_navbar_layout(),
            html.Div([add_new.get_add_new_dashboard_layout()])
        ])  # , '', 'selected_dashboard_style'
    else:
        print("path is nothing..", path)
        # sleep(5)
        return html.Div([
            get_navbar_layout(),
            html.Div([view_report.get_view_dashboard_layout()])
        ])  # , 'selected_dashboard_style', ''
