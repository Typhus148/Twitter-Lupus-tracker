function parse(spec)
        {
            vg.parse.spec(spec, function(chart) { chart({el:"#vis"}).update(); });
        }
function pyTimeStamp(callback)
{
    var xobj = new XMLHttpRequest();
    xobj.overrideMimeType("application/json");
    xobj.open('GET', 'geo_data_states_update_status.json', true);
    xobj.onreadystatechange = function ()
    {
        if (xobj.readyState == 4 && xobj.status == "200")
        {
                callback(xobj.responseText);
        }
    }
    xobj.send(null);
}

function updateChecker() {
//console.log("updateChecker has been executed.");
pyTimeStamp(function(response)
{
    pyTS = JSON.parse(response);
    console.log(pyTS.status);
    if (pyTS.status ==  true)
    {
       parse("tweetMap.json");
       console.log("Map was just updated with new data!");
    }
    else
    {
      console.log("No update to map.");
    }
});
}

window.setInterval(updateChecker, 5000);
parse("tweetMap.json");
