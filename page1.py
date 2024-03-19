from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
from dash.dependencies import Input, Output, State
import numpy as np
import plotly.graph_objects as go

import numpy as np
import calendar

data_lastClick = [
    {"channel": "Direct/None", "Percent": 49},
    {"channel": "Google Ads", "Percent": 30},
    {"channel": "Facebook Ads", "Percent": 10},
    {"channel": "LinkedIn", "Percent": 3}
]

data_eng = [
    {"channel": "Facebook Ads", "Percent": 38},
    {"channel": "Google Ads", "Percent": 17},
    {"channel": "LinkedIn", "Percent": 10},
    {"channel": "Direct/None", "Percent": 10}
]

# Function to create HTML div for each data point
# def create_data_div(entry):
#     channel = entry['channel']
#     percent = entry['Percent']

#     # Customizing font color based on the percentage value
#     font_color = 'green' if percent > 20 else 'red'

#     # Create HTML div with custom styling
#     div = html.Div([
#     html.Div(channel, style={'font-weight': 'bold', 'color': '#222222', "margin": "5px", "margin-left": "10px","margin-top": "10px","margin-bottom": "10px"}),
#     html.Div(f"{percent} %", style={'color': font_color, "margin": "5px","margin-right": "10px","margin-top": "10px","margin-bottom": "10px"})
#     ], style={'display': 'flex', 'justify-content': 'space-between', 'gap': '50px', 'border-radius': '10px', 'box-shadow': '2px 2px 5px 2px rgba(0, 0, 0, 0.1)','backgroundColor': 'white', 'width': '370px', 'margin': '10px',"margin-bottom": "25px" })
#     return div

def create_data_div(entry, icon):
    channel = entry['channel']
    percent = entry['Percent']

    # Define icon classes based on channel name
    icon_classes = {
        "Direct/None": "fas fa-globe",
        "Google Ads": "fab fa-google",
        "Facebook Ads": "fab fa-facebook",
        "LinkedIn": "fab fa-linkedin"
    }

    # Get icon class based on channel name
    icon_class = icon_classes.get(channel, "fas fa-question")

    # Create HTML div with custom styling and icon
    div = html.Div([
        html.Div([html.I(className=icon_class, style={'margin-right': '5px'}), html.Span(channel)], style={'font-weight': 'bold', 'color': '#222222', "margin": "5px", "margin-left": "10px","margin-top": "10px","margin-bottom": "10px","margin-bottom": "10px",}),
        html.Div(f"{percent} %", style={'color': '#222222', "margin": "5px","margin-right": "10px","margin-top": "10px","margin-bottom": "10px"})
    ], style={'display': 'flex', 'justify-content': 'space-between', 'gap': '50px', 'border-radius': '10px', 'box-shadow': '2px 2px 5px 2px rgba(0, 0, 0, 0.1)','backgroundColor': 'white', 'width': '370px', 'margin': '10px',"margin-bottom": "25px" })
    return div

# Usage
for entry in data_lastClick:
    create_data_div(entry, icon="far fa-clock")

for entry in data_eng:
    create_data_div(entry, icon="far fa-flag")









# List of channel names
channels = ['Direct', 'Facebook']
# List of month names
month = [calendar.month_name[i][:3] for i in range(1, 13)]
# Generate percentage data for Direct channel
direct_percentages = [20, 22, 25, 24, 28, 30, 32, 33, 34, 35, 36, 38]
direct_percentages = [x + 50 for x in direct_percentages]

# Generate more volatile data for Facebook channel

facebook_percentages = [
    20,23,21,50,19,25,20,22,60,30,70,42
]  # Generating random data with mean 20 and standard deviation 2


# Ensure percentages are within the range of 0 to 100
direct= np.clip(direct_percentages, 0, 100)
facebook= np.clip(facebook_percentages, 0, 100)

# Create dictionary with data for each channel
areadata = {
    "month": month,
    
    "Direct": direct,
    "Facebook": facebook
}



# Add traces for Direct and Facebook channels with curved lines
area = go.Figure()
area.add_trace(go.Scatter(x=areadata['month'], y=areadata['Direct'], mode='lines+markers', fill='tozeroy', name='Facebook', line_shape='spline', line=dict(color='#f2e9ae')))
area.add_trace(go.Scatter(x=areadata['month'], y=areadata['Facebook'], mode='lines+markers', fill='tonexty', name='Direct', line_shape='spline', line=dict(color='#838df7')))
area.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',  # Set plot background color to transparent
    paper_bgcolor='rgba(0,0,0,0)'  # Set paper background color to transparent
)





data = dict(
    number=[39, 27.4, 20.6, 11],
    _=["Website visit","Form Fills", "MQLs",  "Opportunities"]
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








labels = ['Linkedin', 'Google', 'Youtube', 'Organic']
values = [4500, 2500, 1053, 500]

dl = px.data.medals_long()


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
facebook_icon = html.I(className="fa-brands fa-facebook", style={"margin-right": "6px", "margin-left": "3px"})
twitter_icon = html.I(className="fa-brands fa-x-twitter", style={"margin-right": "6px", "margin-left": "3px"})
linkedin_icon = html.I(className="fa-brands fa-linkedin", style={"margin-right": "6px", "margin-left": "3px"})
google_icon = html.I(className="fa-brands fa-google", style={"margin-right": "6px", "margin-left": "3px"})


dropdown_options = [
    {"label": "Campaign 1", "value": "campaign1"},
    {"label": "Campaign 2", "value": "campaign2"},
    {"label": "Campaign 3", "value": "campaign3"},
    {"label": "Campaign 4", "value": "campaign4"}
]

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

                    ],
                    style={"margin-bottom": "20px",'font-size': '120%',},
                ),
                
                dcc.Dropdown(
            options=dropdown_options,
            placeholder="Select Campaign",
            style={"margin-bottom": "20px"}
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
        html.H3("Channel Attribution", style={"margin-left": "30px", 'color': '#222222', 'text-align':'center', 'line-height': '2'}),
    ],style={'backgroundColor': 'white','display':'flex',}),
        
    html.Div([
    #     html.Div([
    #     dbc.Row([
    #         dbc.Col([
    #             drawText("Facebook","100")  # Pass text as an argument to the drawText function
    #         ], width=3),
    #         dbc.Col([
    #             drawText("LinkedIn","300")  # Pass text as an argument to the drawText function
    #         ], width=3),
    #         dbc.Col([
    #             drawText("Instagram","160")  # Pass text as an argument to the drawText function
    #         ], width=3),
    #         dbc.Col([
    #             drawText("X","320")  # Pass text as an argument to the drawText function
    #         ], width=3),
    #     ]),
    # ],style={'margin-left':'100px'}),
        
        dbc.Row([
#             dbc.Col([
#                 html.Div([
#                     html.H3("Channel Importance", style={ 'color': 'black', 'text-align': 'center',"margin-left": "200px"}),
#                     dcc.Graph(
#                         figure=px.pie(labels=labels, values=values, hole=0.5,
#                                     color_discrete_sequence=get_color_gradient(values),width= 700,height=400).update_layout(
#     plot_bgcolor='rgba(0,0,0,0)',  # Set plot background color to transparent
#     paper_bgcolor='rgba(0,0,0,0)'  # Set paper background color to transparent
# )
#                     ),
#                 ],style={'backgroundColor': 'white','padding-right':'0','z-index':' 0'}) 
#             ], width=3),
            # dbc.Col(
            #     html.Div(
            #     html.Div([
            #         html.Div([
            #             html.Strong(label),
            #             html.Br(),
            #             html.Span(str(round(value / sum(values) * 100, 2)) + "%", style={'font-size': '180%','color': get_color_gradient(values)[i]})
            #         ], style={'color': get_color_gradient(values)[i]}) for i, (label, value) in enumerate(zip(labels, values))
            #     ]),
            #     style={'textAlign': 'center','backgroundColor': 'white','height': '526px','padding': '70px 0','font-size': '160%','z-index':' 1',"margin-left": "100px"}
            #     )
            #     , width=3),
        #     dbc.Col(
        #         html.Div([
        #             html.H3("Campaign Metrics", style={ 'color': 'black', 'text-align': 'center'}),
        #             dcc.Graph(
        #                  # Set the id prop as a string
        #                 figure = px.funnel(data, x='number', y='_', color_discrete_sequence=get_color_gradient(values),width= 600,height=400).update_traces(
        #                     marker_color=get_color_gradient(values)
        #                 ).update_layout(
        #                     plot_bgcolor='rgba(0,0,0,0)',  # Set plot background color to transparent
        #                     paper_bgcolor='rgba(0,0,0,0)',  # Set paper background color to transparent
        #                     yaxis={'visible': True, 'showticklabels': True}
        #                 )
        #             )],
        #             style={'backgroundColor': 'white',"margin-left": "100px" }  # Change card background color
                
        # ), width=12),
        ], align='center'), 
        
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H3("Form Fill by Channel", style={ 'color': 'black', 'text-align': 'center'}),
                    dcc.Graph(
                        id='area-plot',
                        figure=area
                        )],
                    style={'backgroundColor': 'white'}  # Change card background color
                ),
            ])
        ], align='center'), 
        html.Br(),
        dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Div([
            html.H4("Last Click", style={ 'color': '#222222', 'text-align': 'center', "margin-bottom": "30px", "margin-top": "10px"}),
            *[create_data_div(entry,icon="far fa-clock") for entry in data_lastClick]
            ], style={'backgroundColor': '#e8e6ed','padding':'10px','border-radius': '10px', "margin-top": "10px"})
        ], width=4),
        dbc.Col([
            html.Div([
            html.H4("Ai-Driven Attribution", style={ 'color': 'white', 'text-align': 'center', "margin-bottom": "30px", "margin-top": "10px"}),
            *[create_data_div(entry, icon="far fa-flag") for entry in data_eng]  # Place the list comprehension inside square brackets
            ], style={'backgroundColor': '#6939e3','padding':'10px','border-radius': '10px'})

        ], width=4),
        dbc.Col([
            html.Div([
                    html.H3("Campaign Metrics", style={ 'color': 'black', "margin-left": "150px",}),
                    dcc.Graph(
                        id='funnel-graph',  # Set the id prop as a string
                        figure = px.funnel(data, x='number', y='_', color_discrete_sequence=get_color_gradient(values),width= 600,height=400).update_traces(
                            marker_color=get_color_gradient(values)
                        ).update_layout(
                            plot_bgcolor='rgba(0,0,0,0)',  # Set plot background color to transparent
                            paper_bgcolor='rgba(0,0,0,0)',  # Set paper background color to transparent
                            yaxis={'visible': True, 'showticklabels': True}
                        )
                    )],
                    style={'backgroundColor': 'white',"margin-right": "0px",}  # Change card background color
                
        )
        ], width=4)
    ], align='center')
    ])

    ],
    style={'backgroundColor': 'white','padding':'30px',}  # Change main card background color
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
