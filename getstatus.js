$(document).ready(function(){

function parse(spec)
        {
            vg.parse.spec(spec, function(chart) { chart({el:"#vis"}).update(); });
        }

    dropdown_selected = "tweetMap.json";

    $(".dropdown-menu li a").click(function(){
        $(this).parents(".dropdown").find('.btn').html($(this).text() + ' <span class="caret"></span>');
        $(this).parents(".dropdown").find('.btn').val($(this).data('value'));
    });

    $("#option-1").click(function(e){
        parse("tweetMap.json");
        dropdown_selected = "#option-1";
        e.preventDefault();
    });

    $("#option-2").click(function(e){
        parse("Geo_data_optional_tweet_filters/lupus_tweetMap.json");
        dropdown_selected = "Geo_data_optional_tweet_filters/lupus_tweetMap.json";
        e.preventDefault();
    });

    $("#option-3").click(function(e){
        parse("Geo_data_optional_tweet_filters/lupusawarenessmonth_tweetMap.json");
        dropdown_selected = "Geo_data_optional_tweet_filters/lupusawarenessmonth_tweetMap.json";
        e.preventDefault();
    });

    /*$("#option-4").click(function(e){
        parse("Geo_data_optional_tweet_filters/#TEAMLUPUS_tweetMap.json");
        dropdown_selected = "Geo_data_optional_tweet_filters/#TEAMLUPUS_tweetMap.json";
        e.preventDefault();
    });

    $("#option-5").click(function(e){
        parse("Geo_data_optional_tweet_filters/#beatlupus_tweetMap.json");
        dropdown_selected = "Geo_data_optional_tweet_filters/#beatlupus_tweetMap.json";
        e.preventDefault();
    });*/

    $("#option-6").click(function(e){
        parse("Geo_data_optional_tweet_filters/lhandsign_tweetMap.json");
        dropdown_selected = "Geo_data_optional_tweet_filters/lhandsign_tweetMap.json";
        e.preventDefault();
    });

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
            else
            {
                parse(dropdown_selected);
            }
        });
    }

    window.setInterval(updateChecker, 5000);
    parse("tweetMap.json");
});