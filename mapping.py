# __author__ = 'Shayak'
# edits/changes to some things to make code work with py 3.5 and lupus tracker = philip
import vincent
import pandas as pd


def visualizeStateData(stateDict, dataBind, dataKey, thresholds, file_name, update):
    statePanda = {}
    stateCount = 0
    # If true means map was updated with new tweet and is to use appropriate color set
    if update:
        # Color set to display updated state in green
        color_option = 'Custom_set_1'
    else:
        # defualt color set for displaying the regular tweet map
        color_option = 'Purples'

    for (key, value) in stateDict.items():
        statePanda[stateCount] = [key, value]
        stateCount += 1
    stateData = pd.DataFrame.from_dict(statePanda, orient='index')
    stateData.columns = [dataKey, dataBind]
    visualizePandasData(stateData, dataBind, dataKey, thresholds, file_name, color_option)


# Creates the json file that will be read by the javascript to be displayed on a webpage
def visualizePandasData(stateData, dataBind, dataKey, thresholds, file_name, color_option):
    state_topo = 'https://raw.githubusercontent.com/wrobstory/vincent_map_data/master/us_states.topo.json'
    geo_data = [{'name': 'states', 'url': state_topo, 'feature': 'us_states.geo'}]
    vis = vincent.Map(data=stateData, geo_data=geo_data, scale=1000,
                      projection='albersUsa', data_bind=dataBind, data_key=dataKey,
                      map_key={'states': 'properties.NAME'}, brew=color_option)
    vis.scales[0].type = 'threshold'
    vis.scales[0].domain = thresholds
    vis.legend(title='# of Lupus Tweets')
    vis.to_json(file_name)
