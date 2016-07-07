$(document).ready(function(){

function parse(spec)
        {
            vg.parse.spec(spec, function(chart) { chart({el:"#vis"}).update(); });
        }

    $("#option-1").click(function(e){
        parse("tweetMap.json");
        console.log("got the click");
        e.preventDefault();
    });

    $("#option-2").click(function(e){
        parse("Geo_data_optional_tweet_filters/lupus_tweetMap.json");
        console.log("got the click");
        e.preventDefault();
    });

    $("#option-3").click(function(e){
        parse("Geo_data_optional_tweet_filters/#lupusawarenessmonth_tweetMap.json");
        e.preventDefault();
    });

    $("#option-4").click(function(e){
        parse("Geo_data_optional_tweet_filters/#teamlupus_tweetMap.json");
        e.preventDefault();
    });

    $("#option-5").click(function(e){
        parse("Geo_data_optional_tweet_filters/#beatlupus_tweetMap.json");
        e.preventDefault();
    });

    $("#option-6").click(function(e){
        parse("Geo_data_optional_tweet_filters/#lhandsign_tweetMap.json");
        e.preventDefault();
    });

});