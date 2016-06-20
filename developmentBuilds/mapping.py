# __author__ = 'Shayak'
# editor/change some things to make code work with py 3.5 = philip
import vincent
import pandas as pd
import matplotlib.pyplot as plt


def visualizeStateData(stateDict, dataBind, dataKey, thresholds=None, mapTitle=None, jsonFile=None, htmlFile=None):
    statePanda = {}
    stateCount = 0
    for (key, value) in stateDict.items():
        statePanda[stateCount] = [key, value]
        stateCount += 1
    stateData = pd.DataFrame.from_dict(statePanda, orient='index')
    stateData.columns = [dataKey, dataBind]
    visualizePandasData(stateData, dataBind, dataKey, thresholds, mapTitle, jsonFile, htmlFile)


def visualizePandasData(stateData, dataBind, dataKey, thresholds=None, mapTitle=None, jsonFile=None, htmlFile=None):
    state_topo = 'https://raw.githubusercontent.com/wrobstory/vincent_map_data/master/us_states.topo.json'
    geo_data = [{'name': 'states', 'url': state_topo, 'feature': 'us_states.geo'}]
    vis = vincent.Map(data=stateData, geo_data=geo_data, scale=1000,
                      projection='albersUsa', data_bind=dataBind, data_key=dataKey,
                      map_key={'states': 'properties.NAME'}, brew='Blues')
    vis.scales[0].type = 'threshold'
    vis.scales[0].domain = [0, 5, 10, 25, 50, 100, 150, 200, 250]
    vis.legend(title='June 2016 lupus tweets')
    vis.to_json('tweetMap.json')
    if jsonFile is not None and htmlFile is not None:
        vis.to_json(jsonFile, html_out=True, html_path=htmlFile)


def drawXYPlotByFactor(dataDict, xlabel='', ylabel='', legend=None, title=None, savefile=None):
    # Assuming that the data is in the format { factor: [(x1, y1),(x2,y2),...] }
    PLOT_STYLES = ['r^-', 'bo-', 'g^-', 'ks-', 'co-', 'ms-', 'y^-']
    styleCount = 0
    displayedPlots = []
    for factor in dataDict:
        xpoints = [a[0] for a in dataDict[factor]]
        ypoints = [a[1] for a in dataDict[factor]]
        displayedPlots.append(plt.plot(xpoints, ypoints, PLOT_STYLES[styleCount]))
        styleCount = min(styleCount+1, len(PLOT_STYLES)-1)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if legend is None:
        plt.legend(dataDict.keys(), loc=2, prop={'size': 12})
    else:
        plt.legend(legend, loc=2, prop={'size': 12})
    if title is not None:
        plt.title(title)
    if savefile is None:
        plt.show()
    else:
        plt.savefig(savefile)
