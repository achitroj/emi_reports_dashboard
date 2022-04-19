import dash_bootstrap_components as dbc


def get_navbar_layout():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink(id='nav-link-view', children="View Report", href="/view")),
            dbc.NavItem(dbc.NavLink(id='nav-link-add', children="Add New EMI", href='/add')),

            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("More Options", header=True),
                    dbc.DropdownMenuItem("Send reports", href="#"),
                    dbc.DropdownMenuItem("View Expense", href="#"),
                ],
                nav=True,
                in_navbar=True,
                label="More",
            ),
        ],
        brand="EMI Tracker",
        brand_href="#",
        color="primary",
        dark=True,
        sticky='top'

    )
    return navbar
