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

function clearUpdate() {
    parse("tweetMap.json");
}

function updateChecker() {
    pyTimeStamp(function(response)
    {
        pyTS = JSON.parse(response);
        if (pyTS.status ==  true)
        {
            parse("update_tweetMap.json");
            //Replace this with a better function to sleep for 5s then reload the defualt tweetMap
            //Consumes too much memory if let run for a little bit of time causeing massive page lag
            //window.setInterval(clearUpdate, 5000);
        }
    });
}

window.setInterval(updateChecker, 5000);
parse("tweetMap.json");
