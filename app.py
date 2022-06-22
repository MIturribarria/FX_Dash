# Se importan las librerias
import dash
from dash import Dash, html, dcc, Input, Output, dash_table, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
import base64
import dash_auth
from datetime import timedelta
from datetime import datetime



# Se crea la lista de usuarios
usuarios = [["Research","12345"],["Institucionales","12345"]]

# Se crea la aplicación
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Identificación de usuarios

auth =dash_auth.BasicAuth(app,usuarios)
#urllib.request.urlretrieve('https://github.com/MIturribarria/FX_Dash/blob/9e16df5417474a1a0f88407a04c55b004e6a16ed/BBVA2.jpg',
#                            "BBVA2.jpg")
#urllib.request.urlretrieve('https://github.com/MIturribarria/FX_Dash/blob/9e16df5417474a1a0f88407a04c55b004e6a16ed/BBVA.jpg',
#                            "BBVA.jpg")

                            #https://github.com/MIturribarria/FX_Dash/blob/9e16df5417474a1a0f88407a04c55b004e6a16ed/BBVA.jpg


#Las imagenes/Logos
#BBVA = Image.open('BBVA.jpg')
#BBVA2 = Image.open('BBVA2.jpg')

#BBVA = 'BBVA.jpg' # replace with your own image
#BBVA2 = 'BBVA2.jpg'

#encoded_image = base64.b64encode(open(BBVA, 'rb').read())
#encoded_image2 = base64.b64encode(open(BBVA2, 'rb').read())

# Se importan los datos en la carpeta
df_tabla_eco = pd.read_csv('https://raw.githubusercontent.com/MIturribarria/FX_Dash/main/Tabla_eco.csv')
df_last = pd.read_csv('https://raw.githubusercontent.com/MIturribarria/FX_Dash/main/Last.csv')
df_rsi = pd.read_csv('https://raw.githubusercontent.com/MIturribarria/FX_Dash/main/RSI.csv')
df_stocastic = pd.read_csv('https://raw.githubusercontent.com/MIturribarria/FX_Dash/main/Stocastic.csv')
df_dss = pd.read_csv('https://raw.githubusercontent.com/MIturribarria/FX_Dash/main/DSS.csv')
df_tabla_tec = pd.read_csv ('https://raw.githubusercontent.com/MIturribarria/FX_Dash/main/Tabla_tec.csv')
df_carry = pd.read_csv ('https://raw.githubusercontent.com/MIturribarria/FX_Dash/main/Carry.csv')
df_25rr = pd.read_csv ('https://raw.githubusercontent.com/MIturribarria/FX_Dash/main/25RR.csv')
df_iv3m = pd.read_csv ('https://raw.githubusercontent.com/MIturribarria/FX_Dash/main/Vol3M.csv')
df_tabla_vol = pd.read_csv ('https://raw.githubusercontent.com/MIturribarria/FX_Dash/main/Tabla_vol.csv')
df_bis = pd.read_csv ('https://raw.githubusercontent.com/MIturribarria/FX_Dash/main/BIS.csv')



df_last['Date'] =  pd.to_datetime(df_last['Date'], format = '%d/%m/%Y')



#Se hace la aplicación
app.layout = html.Div([

        dbc.Row([dbc.Col(html.Img(src=app.get_asset_url('BBVA.jpg')),
                         width=6,
                         ),
                 dbc.Col(html.Img(src=app.get_asset_url('BBVA2.jpg')),
                         width={'seize':3, 'offset': 3},
                         ),
        ]),

        dbc.Row(dbc.Col(html.H1('BBVA Global Strategy & Research FX Dashboard',
                                style={'fontSize':40, 'font-family':'sans-serif', 'color':'#004481', 'textAlign': 'center'},
                                ),

                        ),
                ),
        dbc.Row(dbc.Col(dbc.Label(''),width=12)),
        dbc.Row([dbc.Col(dbc.Label('Select a currency:'),
                        width=1,
                        ),
                dbc.Col(dcc.Dropdown(df_last.columns.values[1:], 'USDMXN (Mexico)',id='fx_value'),
                        width=2,
                        ),
                dbc.Col(dbc.Label('Select a period:'),
                                width=1,
                                ),
                dbc.Col(dcc.DatePickerRange(id='Fechas2',
                                             min_date_allowed=df_last['Date'].min(),
                                             max_date_allowed=df_last['Date'].max(),
                                             start_date= datetime(2018,1,1),
                                             end_date=df_last['Date'].max()),
                         width=2
                          ),
                dbc.Col(dbc.Label(''),
                        width=6,
                        ),
                ]),
        dbc.Row(dbc.Col(dbc.Label('Economic Summary',size="lg",color='#004481'),
                        width={'seize':6, 'offset': 6},
                                ),
                ),
        dbc.Row([dbc.Col(dcc.Graph(id='TCN_fig'),
                         width=6,
                        ),
                 dbc.Col(dash_table.DataTable(id="Tabla_macro",
                                                  style_data_conditional=[{
                                                    'if': {'row_index': 'odd'},
                                                    'backgroundColor': 'rgb(220, 220, 220)',
                                                                            }],
                                                   style_as_list_view=True,
                                                   style_cell={'fontSize':15, 'font-family':'sans-serif','textAlign': 'center'},
                                                   style_header={
                                                    'backgroundColor': 'rgb(210, 210, 210)',
                                                    'color': 'black',
                                                    'fontWeight': 'bold'
                                                                 }
                                             ),
                         width=6,
                        ),
                ]),
        dbc.Row(dbc.Col(html.H1('Technical Analysis Summary',
                                style={'fontSize':40, 'font-family':'sans-serif', 'color':'#2DCCCD','textAlign': 'center'},
                                ),

                        ),
                ),
        dbc.Row(dbc.Col(dbc.Label(''),width=12)),
        dbc.Row([dbc.Col(dash_table.DataTable(id="Tabla_tec1",
                                                  style_data_conditional=[{
                                                    'if': {'row_index': 'odd'},
                                                    'backgroundColor': 'rgb(220, 220, 220)',
                                                                            }],
                                                  style_as_list_view=True,
                                                  style_cell={'fontSize':15, 'font-family':'sans-serif','textAlign': 'center'},
                                                  style_header={
                                                   'backgroundColor': 'rgb(210, 210, 210)',
                                                   'color': 'black',
                                                   'fontWeight': 'bold'
                                                                }
                                              ),
                         width=4,
                            ),
                dbc.Col(dash_table.DataTable(id="Tabla_tec2",
                                                 style_data_conditional=[{
                                                   'if': {'row_index': 'odd'},
                                                   'backgroundColor': 'rgb(220, 220, 220)',
                                                                            }],
                                                 style_as_list_view=True,
                                                 style_cell={'fontSize':15, 'font-family':'sans-serif','textAlign': 'center'},
                                                 style_header={
                                                  'backgroundColor': 'rgb(210, 210, 210)',
                                                  'color': 'black',
                                                  'fontWeight': 'bold'
                                                                }
                                              ),
                        width=4,
                        ),
                dbc.Col(dash_table.DataTable(id="Tabla_tec3",
                                                 style_data_conditional=[{
                                                   'if': {'row_index': 'odd'},
                                                   'backgroundColor': 'rgb(220, 220, 220)',
                                                                            }],
                                                 style_as_list_view=True,
                                                 style_cell={'fontSize':15, 'font-family':'sans-serif','textAlign': 'center'},
                                                 style_header={
                                                  'backgroundColor': 'rgb(210, 210, 210)',
                                                  'color': 'black',
                                                  'fontWeight': 'bold'
                                                                }
                                                                ),
                        width=4,
                ),
        ]),
        dbc.Row([dbc.Col(dcc.Graph(id='Chart_tec1'),
                         width=6,
                                ),
                 dbc.Col(dcc.Graph(id='Chart_tec2'),
                         width=6,
                                ),
        ]),

        dbc.Row(dbc.Col(html.H1('FX Relative Peformance & Carry Total Return Indexes',
                                style={'fontSize':35, 'font-family':'sans-serif', 'color':'#D8BE75', 'textAlign': 'center'},
                                ),

                        ),
                ),
        dbc.Row(dbc.Col(dbc.Label(''),width=12)),
        dbc.Row([dbc.Col(dbc.Label('Select a period:'),width=2),
                 dbc.Col(dbc.Label('Select currencies to compare:'),width=10)]),

        dbc.Row([dbc.Col(dcc.DatePickerRange(id='Fechas1',
                                             min_date_allowed=df_last['Date'].min(),
                                             max_date_allowed=df_last['Date'].max(),
                                             start_date= datetime(2018,1,1),
                                             end_date=df_last['Date'].max()),
                         width=2,
                                ),
                 dbc.Col(dcc.Dropdown(df_last.columns.values[1:],
                         'USDBRL (Brazil)',id='multi_100_1', multi=False),
                         width=2,
                                ),
                 dbc.Col(dcc.Dropdown(df_last.columns.values[1:],
                         'EURUSD (Eurozone)',id='multi_100_2', multi=False),
                         width=2,
                                ),
                 dbc.Col(dcc.Dropdown(df_last.columns.values[1:],
                        'USDJPY (Japan)',id='multi_100_3', multi=False),
                         width=2,
                                ),
                 dbc.Col(dcc.Dropdown(df_last.columns.values[1:],
                        'USDCOP (Colombia)',id='multi_100_4', multi=False),
                         width=2,
                                ),
                 dbc.Col(dcc.Dropdown(df_last.columns.values[1:],
                        'USDZAR (South Africa)',id='multi_100_5', multi=False),
                         width=2,
                                ),

        ]),

        dbc.Row([dbc.Col(dcc.Graph(id='Chart_Base100'),
                         width=6,
                                ),
                 dbc.Col(dcc.Graph(id='Chart_Carry'),
                         width=6,
                                ),
        ]),
        dbc.Row(dbc.Col(html.H1('FX Volatility Analysis',
                                style={'fontSize':35, 'font-family':'sans-serif', 'color':'#F35E61', 'textAlign': 'center'},
                                ),

                        ),
                ),
        dbc.Row(dbc.Col(dbc.Label(''),width=12)),
        dbc.Row([dbc.Col(dbc.Label('Select a period:'),width={'seize':1, 'offset': 4}),
                dbc.Col(dcc.DatePickerRange(id='Fechas3',
                                                     min_date_allowed=df_last['Date'].min(),
                                                     max_date_allowed=df_last['Date'].max(),
                                                     start_date= datetime(2018,1,1),
                                                     end_date=df_last['Date'].max()),
                                 width=2,
                                        ),
                dbc.Col(dbc.Label(''),width=5),
                ]),
        dbc.Row([dbc.Col(dcc.Graph(id='Chart_TS'),
                         width=4,
                                ),
                 dbc.Col(dcc.Graph(id='Chart_IV3M'),
                         width=4,
                                ),
                 dbc.Col(dcc.Graph(id='Chart_RR'),
                         width=4,
                                ),
        ]),

        dbc.Row(dbc.Col(html.H1('FX Fundamental Analysis',
                                style={'fontSize':35, 'font-family':'sans-serif', 'color':'#48AE64', 'textAlign': 'center'},
                                ),

                        ),
                ),
        dbc.Row(dbc.Col(dbc.Label(''),width=12)),
        dbc.Row([dbc.Col(dbc.Label('Select a period:'),width=1),
                dbc.Col(dcc.DatePickerRange(id='Fechas4',
                                                     min_date_allowed=df_bis['Date'].min(),
                                                     max_date_allowed=df_bis['Date'].max(),
                                                     start_date= datetime(2018,1,1),
                                                     end_date=df_last['Date'].max()),
                                 width=2,
                                        ),
                dbc.Col(dbc.Label(''),width=9),
                ]),
        dbc.Row([dbc.Col(dcc.Graph(id='Chart_BIS'),
                         width=6,
                                ),
                 dbc.Col(dcc.Graph(id='Chart_Model'),
                         width=6,
                                ),
                ]),
])



#Se definen los callbacks

@app.callback(                 # Para la grafica 1 de tipo de cambio y prom moviles
    Output('TCN_fig', 'figure'),
    [Input('fx_value', 'value'),
     Input('Fechas2', 'start_date'),
     Input('Fechas2','end_date')])
def update_graph(filtro_fx,start_date,end_date):  # Para la grafica 1 de tipo de cambio y prom moviles

    start = datetime.strptime(start_date[:10],'%Y-%m-%d')
    end =  datetime.strptime(end_date[:10],'%Y-%m-%d')

    df_tcn =df_last[['Date', filtro_fx]]
    df_tcn['SMA10'] = df_tcn[filtro_fx].rolling(10).mean()
    df_tcn['SMA30'] = df_tcn[filtro_fx].rolling(30).mean()
    df_tcn['SMA90'] = df_tcn[filtro_fx].rolling(90).mean()
    df_tcn['SMA200'] = df_tcn[filtro_fx].rolling(200).mean()

    df_tcn['Date'] =  pd.to_datetime(df_tcn['Date'], format = '%d/%m/%Y')
    df_tcn = df_tcn[(df_tcn['Date'] > start) & (df_tcn['Date'] < end)]

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df_tcn['Date'], y=df_tcn[filtro_fx], name=filtro_fx,
                         line=dict(color='#004481', width=2)))
    fig.add_trace(go.Scatter(x=df_tcn['Date'], y=df_tcn['SMA10'], name='SMA10',
                         line=dict(color='#2DCCCD', width=1.5,
                              dash='dash')))
    fig.add_trace(go.Scatter(x=df_tcn['Date'], y=df_tcn['SMA30'], name='SMA30',
                         line=dict(color='#D8BE75', width=1.5,
                              dash='dash')))
    fig.add_trace(go.Scatter(x=df_tcn['Date'], y=df_tcn['SMA90'], name='SMA90',
                         line=dict(color='#F35E61', width=1.5,
                              dash='dash')))
    fig.add_trace(go.Scatter(x=df_tcn['Date'], y=df_tcn['SMA200'], name='SMA200',
                         line=dict(color='#48AE64', width=1.5,
                              dash='dash')))

    fig.update_layout(title='Nominal FX & Standard Moving Averages',
                       xaxis_title='Date',
                       yaxis_title='Level',
                       plot_bgcolor="white")

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#CCCCCC')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#CCCCCC')

    fig.update_xaxes(
        rangeslider_visible=False,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1M", step="month", stepmode="backward"),
                dict(count=6, label="6M", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1Y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    return fig

@app.callback(    # La tabla macro
    Output('Tabla_macro', 'data'),
    Input('fx_value', 'value'))
def update_table(fx_input):  # La tabla macro
    dff = df_tabla_eco[['Economic Indicator', fx_input]]
    dff2 = dff[fx_input].str.split(',',expand=True)
    dff2.columns = ['Data', 'As of:']
    dff3 = pd.concat([dff['Economic Indicator'],dff2],axis=1)
    data = dff3.to_dict('records')
    return data

##Las tablas del tecnico

@app.callback(
    Output('Tabla_tec1', 'data'),
    Input('fx_value', 'value'))
def update_table2(fx_input):
    dff = df_tabla_tec[['Indicator:', fx_input]]
    df3=dff.iloc[0:6]
    df3.columns =['Indicator:','Level']
    data = df3.to_dict('records')
    return data

@app.callback(
    Output('Tabla_tec2', 'data'),
    Input('fx_value', 'value'))
def update_table2(fx_input):
    dff = df_tabla_tec[['Indicator:', fx_input]]
    df4=dff.iloc[7:13]
    df4.columns =['Indicator:','Level']
    data = df4.to_dict('records')
    return data

@app.callback(
    Output('Tabla_tec3', 'data'),
    Input('fx_value', 'value'))
def update_table2(fx_input):
    dff = df_tabla_tec[['Indicator:', fx_input]]
    df5=dff.iloc[14:]
    dff5 = df5[fx_input].str.split(',',expand=True)
    dff5.columns = ['Last', 'Max', 'Min']
    df5 = pd.concat([df5['Indicator:'],dff5],axis=1)

    data = df5.to_dict('records')
    return data


@app.callback(                 # Para la grafica 1 de tecnico
    Output('Chart_tec1', 'figure'),
    Input('fx_value', 'value'))
def update_graph(filtro_tec):  # Para la grafica 1 de tecnico

    df_tec1 =df_rsi[['Date', filtro_tec]]
    df_tec1['SMA14'] = df_tec1[filtro_tec].rolling(14).mean()

    df_tec1['Date'] =  pd.to_datetime(df_tec1['Date'], format = '%d/%m/%Y')

    end_date = df_tec1['Date'].max()
    start_date = end_date - timedelta(days =728)
    df_tec1 = df_tec1[(df_tec1['Date'] > start_date) & (df_tec1['Date'] < end_date)]

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df_tec1['Date'], y=df_tec1[filtro_tec], name='RSI',
                         line=dict(color='#004481', width=2)))
    fig.add_trace(go.Scatter(x=df_tec1['Date'], y=df_tec1['SMA14'], name='RSI SMA14',
                         line=dict(color='#F35E61', width=2,
                              dash='dash')))

    fig.add_hline(y=75, line_color="#48AE64")
    fig.add_hline(y=25, line_color="#48AE64")


    fig.update_layout(title='RSI Levels',
                       xaxis_title='Date',
                       yaxis_title='Level',
                       plot_bgcolor="white")

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#CCCCCC')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#CCCCCC')

    fig.update_xaxes(
        rangeslider_visible=False,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1M", step="month", stepmode="backward"),
                dict(count=6, label="6M", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1Y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    return fig

@app.callback(                 # Para la grafica 2 de tecnico
        Output('Chart_tec2', 'figure'),
        Input('fx_value', 'value'))
def update_graph(filtro_tec2):  # Para la grafica 2 de tecnico
    df_tec2 =df_stocastic[['Date', filtro_tec2]]
    df_tec2['DSS'] = df_dss[filtro_tec2]

    df_tec2['Date'] =  pd.to_datetime(df_tec2['Date'], format = '%d/%m/%Y')

    end_date = df_tec2['Date'].max()
    start_date = end_date - timedelta(days =728)
    df_tec2 = df_tec2[(df_tec2['Date'] > start_date) & (df_tec2['Date'] < end_date)]

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df_tec2['Date'], y=df_tec2[filtro_tec2], name='Stocastic',
                         line=dict(color='#004481', width=2)))
    fig.add_trace(go.Scatter(x=df_tec2['Date'], y=df_tec2['DSS'], name='DSS',
                         line=dict(color='#F35E61', width=2,
                              dash='dash')))

    fig.add_hline(y=75, line_color="#48AE64")
    fig.add_hline(y=25, line_color="#48AE64")


    fig.update_layout(title='Stocastic Levels',
                       xaxis_title='Date',
                       yaxis_title='Level',
                       plot_bgcolor="white")

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#CCCCCC')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#CCCCCC')

    fig.update_xaxes(
        rangeslider_visible=False,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1M", step="month", stepmode="backward"),
                dict(count=6, label="6M", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1Y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    return fig

@app.callback(                 # Para la grafica 1 de tipo de cambio y prom moviles
    Output('Chart_Base100', 'figure'),
    [Input('fx_value','value'),
      Input('multi_100_1', 'value'),
      Input('multi_100_2','value'),
      Input('multi_100_3','value'),
      Input('multi_100_4','value'),
      Input('multi_100_5','value'),
            Input('Fechas1','start_date'),
            Input('Fechas1','end_date')])
def update_graph(fx_value,fx1,fx2,fx3,fx4,fx5,start_date,end_date):  # Para la grafica 1 de tipo de cambio y prom moviles

    start = datetime.strptime(start_date[:10],'%Y-%m-%d')
    end =  datetime.strptime(end_date[:10],'%Y-%m-%d')

    df_n =df_last[['Date', fx_value]]
    df_n['Date'] =  pd.to_datetime(df_n['Date'], format = '%d/%m/%Y')
    df_n = df_n[(df_n['Date'] > start) & (df_n['Date'] < end)]
    df_n = df_n.set_index('Date').pct_change().fillna(0).add(1).cumprod().mul(100).reset_index()

    df_1 =df_last[['Date', fx1]]
    df_1['Date'] =  pd.to_datetime(df_1['Date'], format = '%d/%m/%Y')
    df_1 = df_1[(df_1['Date'] > start) & (df_1['Date'] < end)]
    df_1 = df_1.set_index('Date').pct_change().fillna(0).add(1).cumprod().mul(100).reset_index()

    df_2 =df_last[['Date', fx2]]
    df_2['Date'] =  pd.to_datetime(df_2['Date'], format = '%d/%m/%Y')
    df_2 = df_2[(df_2['Date'] > start) & (df_2['Date'] < end)]
    df_2 = df_2.set_index('Date').pct_change().fillna(0).add(1).cumprod().mul(100).reset_index()

    df_3 =df_last[['Date', fx3]]
    df_3['Date'] =  pd.to_datetime(df_3['Date'], format = '%d/%m/%Y')
    df_3 = df_3[(df_3['Date'] > start) & (df_3['Date'] < end)]
    df_3 = df_3.set_index('Date').pct_change().fillna(0).add(1).cumprod().mul(100).reset_index()

    df_4 =df_last[['Date', fx4]]
    df_4['Date'] =  pd.to_datetime(df_4['Date'], format = '%d/%m/%Y')
    df_4 = df_4[(df_4['Date'] > start) & (df_4['Date'] < end)]
    df_4 = df_4.set_index('Date').pct_change().fillna(0).add(1).cumprod().mul(100).reset_index()

    df_5 =df_last[['Date', fx5]]
    df_5['Date'] =  pd.to_datetime(df_5['Date'], format = '%d/%m/%Y')
    df_5 = df_5[(df_5['Date'] > start) & (df_5['Date'] < end)]
    df_5 = df_5.set_index('Date').pct_change().fillna(0).add(1).cumprod().mul(100).reset_index()
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df_n['Date'], y=df_n[fx_value], name=fx_value,
                         line=dict(color='#004481', width=2)))
    fig.add_trace(go.Scatter(x=df_1['Date'], y=df_1[fx1], name=fx1,
                         line=dict(color='#2DCCCD', width=2)))
    fig.add_trace(go.Scatter(x=df_2['Date'], y=df_2[fx2], name=fx2,
                         line=dict(color='#D8BE75', width=2)))
    fig.add_trace(go.Scatter(x=df_3['Date'], y=df_3[fx3], name=fx3,
                         line=dict(color='#F7893B', width=2)))
    fig.add_trace(go.Scatter(x=df_4['Date'], y=df_4[fx4], name=fx4,
                         line=dict(color='#48AE64', width=2)))
    fig.add_trace(go.Scatter(x=df_5['Date'], y=df_5[fx5], name=fx5,
                         line=dict(color='#F8CD51', width=2)))

    fig.update_layout(title='FX Relative performance',
                       xaxis_title='Date',
                       yaxis_title='Level',
                       plot_bgcolor="white")

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#CCCCCC')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#CCCCCC')


    return fig

@app.callback(                 # Para la grafica 1 de tipo de cambio y prom moviles
    Output('Chart_Carry', 'figure'),
    [Input('fx_value','value'),
      Input('multi_100_1', 'value'),
      Input('multi_100_2','value'),
      Input('multi_100_3','value'),
      Input('multi_100_4','value'),
      Input('multi_100_5','value'),
            Input('Fechas1','start_date'),
            Input('Fechas1','end_date')])
def update_graph(fx_value,fx1,fx2,fx3,fx4,fx5,start_date,end_date):  # Para la grafica 1 de tipo de cambio y prom moviles

    start = datetime.strptime(start_date[:10],'%Y-%m-%d')
    end =  datetime.strptime(end_date[:10],'%Y-%m-%d')

    df_n =df_last[['Date', fx_value]]
    df_n['Date'] =  pd.to_datetime(df_n['Date'], format = '%d/%m/%Y')
    df_n = df_n[(df_n['Date'] > start) & (df_n['Date'] < end)]
    df_n = df_n.set_index('Date').pct_change().fillna(0).add(1).cumprod().mul(100).reset_index()

    df_1 =df_carry[['Date', fx1]]
    df_1['Date'] =  pd.to_datetime(df_1['Date'], format = '%d/%m/%Y')
    df_1 = df_1[(df_1['Date'] > start) & (df_1['Date'] < end)]
    df_1 = df_1.set_index('Date').pct_change().fillna(0).add(1).cumprod().mul(100).reset_index()

    df_2 =df_carry[['Date', fx2]]
    df_2['Date'] =  pd.to_datetime(df_2['Date'], format = '%d/%m/%Y')
    df_2 = df_2[(df_2['Date'] > start) & (df_2['Date'] < end)]
    df_2 = df_2.set_index('Date').pct_change().fillna(0).add(1).cumprod().mul(100).reset_index()

    df_3 =df_carry[['Date', fx3]]
    df_3['Date'] =  pd.to_datetime(df_3['Date'], format = '%d/%m/%Y')
    df_3 = df_3[(df_3['Date'] > start) & (df_3['Date'] < end)]
    df_3 = df_3.set_index('Date').pct_change().fillna(0).add(1).cumprod().mul(100).reset_index()

    df_4 =df_carry[['Date', fx4]]
    df_4['Date'] =  pd.to_datetime(df_4['Date'], format = '%d/%m/%Y')
    df_4 = df_4[(df_4['Date'] > start) & (df_4['Date'] < end)]
    df_4 = df_4.set_index('Date').pct_change().fillna(0).add(1).cumprod().mul(100).reset_index()

    df_5 =df_carry[['Date', fx5]]
    df_5['Date'] =  pd.to_datetime(df_5['Date'], format = '%d/%m/%Y')
    df_5 = df_5[(df_5['Date'] > start) & (df_5['Date'] < end)]
    df_5 = df_5.set_index('Date').pct_change().fillna(0).add(1).cumprod().mul(100).reset_index()
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df_n['Date'], y=df_n[fx_value], name=fx_value,
                         line=dict(color='#004481', width=2)))
    fig.add_trace(go.Scatter(x=df_1['Date'], y=df_1[fx1], name=fx1,
                         line=dict(color='#2DCCCD', width=2)))
    fig.add_trace(go.Scatter(x=df_2['Date'], y=df_2[fx2], name=fx2,
                         line=dict(color='#D8BE75', width=2)))
    fig.add_trace(go.Scatter(x=df_3['Date'], y=df_3[fx3], name=fx3,
                         line=dict(color='#F7893B', width=2)))
    fig.add_trace(go.Scatter(x=df_4['Date'], y=df_4[fx4], name=fx4,
                         line=dict(color='#48AE64', width=2)))
    fig.add_trace(go.Scatter(x=df_5['Date'], y=df_5[fx5], name=fx5,
                         line=dict(color='#F8CD51', width=2)))

    fig.update_layout(title='Total Return Carry Index',
                       xaxis_title='Date',
                       yaxis_title='Level',
                       plot_bgcolor="white")

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#CCCCCC')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#CCCCCC')


    return fig

@app.callback(                 # Para la grafica 1 de tipo de cambio y prom moviles
    Output('Chart_TS', 'figure'),
    Input('fx_value', 'value'))
def update_graph(fx):  # Para la grafica 1 de tipo de cambio y prom moviles

    df = df_tabla_vol[['Period:', fx]]
    df_2 = df[fx].str.split(',',expand=True)
    df_2.columns = ['Actual', '1M Ago', '3M Ago', '6M Ago', '12M Ago']
    df3 = pd.concat([df['Period:'],df_2],axis=1)

    df3['Actual'] = df3['Actual'].astype(float)
    df3['1M Ago'] = df3['1M Ago'].astype(float)
    df3['3M Ago'] = df3['3M Ago'].astype(float)
    df3['6M Ago'] = df3['6M Ago'].astype(float)
    df3['12M Ago'] = df3['12M Ago'].astype(float)


    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df3['Period:'], y=df3['Actual'], name='Actual',
                             line=dict(color='#004481', width=2)))

    fig.add_trace(go.Scatter(x=df3['Period:'], y=df3['1M Ago'], name='1M Ago',
                             line=dict(color='#2DCCCD', width=2)))

    fig.add_trace(go.Scatter(x=df3['Period:'], y=df3['3M Ago'], name='3M Ago',
                             line=dict(color='#D8BE75', width=2)))

    fig.add_trace(go.Scatter(x=df3['Period:'], y=df3['6M Ago'], name='6M Ago',
                             line=dict(color='#F35E61', width=2)))

    fig.add_trace(go.Scatter(x=df3['Period:'], y=df3['12M Ago'], name='12M Ago',
                             line=dict(color='#48AE64', width=2)))


    fig.update_layout(title='FX Term Structure',
                           xaxis_title='Period',
                           yaxis_title='Level',
                           plot_bgcolor="white")

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#CCCCCC')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#CCCCCC')


    return fig

@app.callback(                 # Para la grafica 1 de tipo de cambio y prom moviles
    Output('Chart_IV3M', 'figure'),
    [Input('fx_value', 'value'),
     Input('Fechas3', 'start_date'),
     Input('Fechas3','end_date')])
def update_graph(fx,start_date,end_date):  # Para la grafica 1 de tipo de cambio y prom moviles

    start = datetime.strptime(start_date[:10],'%Y-%m-%d')
    end =  datetime.strptime(end_date[:10],'%Y-%m-%d')

    df_1 =df_iv3m[['Date', fx]]


    df_1['Date'] =  pd.to_datetime(df_1['Date'], format = '%d/%m/%Y')
    df_1 = df_1[(df_1['Date'] > start) & (df_1['Date'] < end)]

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df_1['Date'], y=df_1[fx], name='IV3M',
                         line=dict(color='#004481', width=2)))


    fig.update_layout(title='3-Month Implied Volatility',
                       xaxis_title='Date',
                       yaxis_title='Level',
                       plot_bgcolor="white")

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#CCCCCC')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#CCCCCC')

    fig.update_xaxes(
        rangeslider_visible=False,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1M", step="month", stepmode="backward"),
                dict(count=6, label="6M", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1Y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    return fig

@app.callback(                 # Para la grafica 1 de tipo de cambio y prom moviles
    Output('Chart_RR', 'figure'),
    [Input('fx_value', 'value'),
     Input('Fechas3', 'start_date'),
     Input('Fechas3','end_date')])
def update_graph(fx,start_date,end_date):  # Para la grafica 1 de tipo de cambio y prom moviles

    start = datetime.strptime(start_date[:10],'%Y-%m-%d')
    end =  datetime.strptime(end_date[:10],'%Y-%m-%d')

    df_1 =df_25rr[['Date', fx]]


    df_1['Date'] =  pd.to_datetime(df_1['Date'], format = '%d/%m/%Y')
    df_1 = df_1[(df_1['Date'] > start) & (df_1['Date'] < end)]

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df_1['Date'], y=df_1[fx], name='IV3M',
                         line=dict(color='#2DCCCD', width=2)))


    fig.update_layout(title='25D Risk Reversal',
                       xaxis_title='Date',
                       yaxis_title='Level',
                       plot_bgcolor="white")

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#CCCCCC')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#CCCCCC')

    fig.update_xaxes(
        rangeslider_visible=False,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1M", step="month", stepmode="backward"),
                dict(count=6, label="6M", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1Y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    return fig


if __name__ =='__main__':
    app.run_server()








    ################################### COLORES BBVA
    # 1 #004481
    # 2 #1464A5
    # 3 #2DCCCD
    # 4 #1973B8
    # 5 #D8BE75
    # 6 #5BBEFF
    # 7 #F7893B
    # 8 #F35E61
    # 9 #48AE64
    # 10 #F8CD51
    # 11 #F78BE8
