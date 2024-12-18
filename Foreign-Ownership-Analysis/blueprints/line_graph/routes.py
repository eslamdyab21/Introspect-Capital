from flask import request, jsonify, current_app
from . import line_graph_blueprint
from services.line_graph.service import get_line_data


@line_graph_blueprint.route('/line_graph', methods=['GET', 'POST'])
def get_data():
    data = request.get_json()['selections']
    ticker = data['Tickers']
    country = data['Countries']
    sector = data['Sectors']
    exchange = data['Exchanges']
    y_axis = data['Y-axis']
    start_date = data['Start Date']
    end_date = data['End Date']

    df_merged = current_app.config['df_merged']

    df_filtered = get_line_data(df_merged = df_merged, ticker = ticker, country = country, sector = sector,
                                exchange = exchange, y_axis = y_axis, start_date = start_date, 
                                end_date = end_date)
    
    return df_filtered


# ?ticker=ADNOCGAS UH&country=UAE&sector=Energy&exchange=Abu Dhabi&y_axis=FO%