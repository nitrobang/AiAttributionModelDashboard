from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
from dash.dependencies import Input, Output, State



# Example data
data_eng = [
    {"title": "Emails", "value": 2458, "change_percentage": 26},
    {"title": "Webinars", "value": 575, "change_percentage": 22},
    {"title": "White Papers", "value": 1672, "change_percentage": -16},
    {"title": "Tradeshows", "value": 452, "change_percentage": -20},
    {"title": "Newsletters", "value": 1123, "change_percentage": 65},
    {"title": "Email Flow", "value": 1454, "change_percentage": 5},
    {"title": "Digital Printing", "value": 765, "change_percentage": -6},
]

# Function to create HTML div for each data point
def create_data_div(entry):
    title = entry['title']
    value = entry['value']
    change_percentage = entry['change_percentage']

    # Determine font color based on change direction
    font_color = 'green' if change_percentage >= 0 else 'red'
    arrow = '↑' if change_percentage >= 0 else '↓'

    # Create HTML div with custom styling
    div = html.Div([
        html.Div(title, style={'font-weight': 'bold','color':'#222222',"margin-bottom": "30px","margin-left": "50px"}),
        html.Div(f"{value} ({arrow} {abs(change_percentage)}%)", style={'color': font_color,"margin-right": "100px"})
    ],style={'display':'flex','justify-content':'space-between','gap':'50px'})
    return div




data = dict(
    number=[39, 27.4, 20.6, 11],
    stage=["Website visit", "Downloads", "Potential customers", "Requested price"]
)




# Custom function to generate color gradient based on percentage rank
def get_color_gradient(values):
    # Define color range (light blue to dark blue)
    colors = ["#e6faff", "#ccf5ff", "#b3f0ff", "#66e0ff", "#33d6ff", "#00ccff", "#00b8e6", "#00a3cc", "#008fb3", "#007a99"]
    # Calculate the max value
    max_value = max(values)
    if max_value == 0:
        return [colors[0] for _ in values]
    # Assign color based on percentage rank
    return [colors[min(int(value / max_value * (len(colors)-1)), len(colors)-1)] for value in values]

labels = ['Emails', 'Webinars', 'White Papers', 'Newsletters']
values = [4500, 2500, 1053, 500]

df = px.data.gapminder().query("continent == 'Oceania'")

# Text field
def drawText(text,value):
    return dbc.Card([
            dbc.CardBody([
                
                    html.H2(value, style={'color': 'black', 'textAlign': 'center','font-size':'20px' })  # Set text color to black
                
            ]),dbc.CardFooter(text, style={ 'textAlign': 'center','color': 'black','backgroundColor': '#b3f0ff','font-weight':'bold'})],
            style={'backgroundColor': 'white','width':'270px',}  # Change card background color
    )
    

# Build App
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP,dbc.themes.SLATE,dbc.icons.FONT_AWESOME,{
        "href": "assets/custom.css",
        "rel": "stylesheet",
        "type": "text/css",
    }])
plus_icon=html.I(className='fa-solid fa-bars')
up_icon = html.I(className="fa-solid fa-arrow-trend-up", style={"margin-right": "6px", "margin-left": "2px"})
layer_icon = html.I(className="fas fa-layer-group", style={"margin-right": "5px"})
data_icon = html.I(className="fas fa-database", style={"margin-right": "6px", "margin-left": "2px"})
idea_icon = html.I(className="fas fa-lightbulb", style={"margin-right": "6px", "margin-left": "3px"})


app.layout = html.Div([
    html.Div([
        html.Div(
            [
                dbc.Button(
                    children= plus_icon,
                    id="open-offcanvas-scrollable",
                    n_clicks=0,style={'margin-left': '17px', 'margin-top': '5px','background': '#222222'}
                ),
                dbc.Offcanvas(
    [
        
        html.Div(
            [
                
                html.Div(
                    html.Img(src="/assets/logo.png", style={"width": "100px", "height": "auto","margin-left": "0px"}),
                    style={"margin-bottom": "20px","margin-left": "0",'display':'flex', 'align-items': 'flex-start'}
                ),
                # Links
                
                html.Div(
                    [
                html.A(
                    html.Span([up_icon, "Lead Gen"], style={"margin-bottom": "10px", "display": "block", 'text-decoration' : 'none'}),
                    href="/page2.py"
                ),
                html.A(
                    html.Span([layer_icon, "Lead Nurturing"], style={"margin-bottom": "10px", "display": "block", 'text-decoration' : 'none'}),
                    href="/page3.py"
                ),
                html.A(
                    html.Span([data_icon, "Data"], style={"margin-bottom": "10px", "display": "block", 'text-decoration' : 'none'}),
                    href="#"
                ),
                html.A(
                    html.Span([idea_icon, "Optimize Media Mix"], style={"display": "block", 'text-decoration' : 'none'}),
                    href="#"
                ),

                    ],
                    style={"margin-bottom": "20px",'font-size': '120%',},
                ),

                # Title
                html.H5("Budget", style={"margin-bottom": "5px"}),

                # Text input boxes
                dbc.Input(placeholder="Enter Budget", style={"margin-bottom": "20px"}),

                html.H5("Reach", style={"margin-bottom": "5px"}),

                # Text input boxes
                dbc.Input(placeholder="Enter Reach", style={"margin-bottom": "20px"}),

                html.H5("Topic Area", style={"margin-bottom": "5px"}),

                # Text input boxes
                dbc.Input(placeholder="Enter Topic Area", style={"margin-bottom": "20px"}),

                # Button
                html.Div(dbc.Button("Go", color="primary", className="mr-1",),style={'display':'flex', 'justify-content': 'center',}),
            ],
            style={"backgroundColor": "#222222", "text-align": "left"}
        ),
    ],
    id="offcanvas-scrollable",
    scrollable=True,
    title="",
    is_open=False,
    style={"backgroundColor": "#222222", "padding-left": "0"},
)



            ]
        ),
        html.H3("AI Attribution Model and Optimization Tool", style={"margin-left": "30px", 'color': '#222222', 'text-align':'center', 'line-height': '2'}),
    ],style={'backgroundColor': 'white','display':'flex',}),
        
    html.Div([
        html.Div([
        dbc.Row([
            dbc.Col([
                drawText("Marketing Leads","9634")  # Pass text as an argument to the drawText function
            ], width=3),
            dbc.Col([
                drawText("MQLs","1170")  # Pass text as an argument to the drawText function
            ], width=3),
            dbc.Col([
                drawText("Opportunities","1000")  # Pass text as an argument to the drawText function
            ], width=3),
            dbc.Col([
                drawText("Conversions","500")  # Pass text as an argument to the drawText function
            ], width=3),
        ]),
    ],style={'margin-left':'100px'}),
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Row([
            dbc.Col([
    html.Div([
        html.H3("Cohort Performance", style={ 'color': 'black', 'text-align': 'center',"margin-left": "40px"}),
        dcc.Graph(
            figure=px.bar(data, y='number', x='stage', orientation='v',).update_traces(
                marker_color=get_color_gradient(values)
            ).update_layout(
                plot_bgcolor='rgba(0,0,0,0)',  # Set plot background color to transparent
                paper_bgcolor='rgba(0,0,0,0)',  # Set paper background color to transparent
                xaxis_title="Stage",
                yaxis_title="Number",
            )
        ),
    ], style={'backgroundColor': 'white', 'padding-right': '0', 'z-index': ' 0'})
], width=3),


            dbc.Col([
                html.Div([
                    html.H3("Activity Importance", style={ 'color': 'black', 'text-align': 'center',"margin-left": "130px",'position':'relative'}),
                    dcc.Graph(
                        figure=px.pie(labels=labels, values=values, hole=0.5,
                                    color_discrete_sequence=get_color_gradient(values),width= 450,height=450).update_layout(
    plot_bgcolor='rgba(0,0,0,0)',  # Set plot background color to transparent
    paper_bgcolor='rgba(0,0,0,0)'  # Set paper background color to transparent
)
                    ),
                ],style={'backgroundColor': 'white','padding-right':'0','z-index':' 0'}) 
            ], width=3),
            dbc.Col(
                html.Div(
                html.Div([
                    html.Div([
                        html.Strong(label),
                        html.Br(),
                        html.Span(str(round(value / sum(values) * 100, 2)) + "%", style={'font-size': '180%','color': get_color_gradient(values)[i]})
                    ], style={'color': get_color_gradient(values)[i]}) for i, (label, value) in enumerate(zip(labels, values))
                ]),
                style={'textAlign': 'center','backgroundColor': 'white','height': '526px','padding': '70px 0','font-size': '160%','z-index':' 1'}
                )
                , width=2),
            dbc.Col(
                html.Div([
                    html.H3("Engagements", style={ 'color': '#222222', 'text-align': 'center','top':'0',"margin-bottom": "70px"}),
                    html.Div([
        create_data_div(entry) for entry in data_eng
    ])],
                    style={'backgroundColor': 'white'}  # Change card background color
                
        ), width=4),
        ], align='center'), 
        html.Br(),   
    ],
    style={'backgroundColor': 'white'}  # Change main card background color
    )
])

@app.callback(
    Output("offcanvas-scrollable", "is_open"),
    Input("open-offcanvas-scrollable", "n_clicks"),
    State("offcanvas-scrollable", "is_open"),
)
def toggle_offcanvas_scrollable(n1, is_open):
    if n1:
        return not is_open
    return is_open

# Run app and display result inline in the notebook
app.run_server(debug=True)
