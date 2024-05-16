// websockets

var ws_scheme = window.location.protocol === "https:" ? "wss" : "ws";

const ws = new WebSocket(
ws_scheme
+ '://'
+ window.location.host
+ '/ws/'
);
var allCommentsSection = document.getElementById("allCommentsSection");

ws.onopen = function(){
    ws.send(JSON.stringify({
        action: "list",
        request_id: new Date().getTime(),
    }));
    ws.send(JSON.stringify({
        action: "subscribe_to_comment_activity",
        request_id: new Date().getTime(),
    }));
} 

ws.onmessage = function(e){
    const rawData = JSON.parse(e.data);
    const comments = rawData.data
    const responseAction = rawData.action;

    if (responseAction == "list") {
        allCommentsSection.innerHTML = ""
        for (const comment of comments) {
            commentTreeBuilder(comment, allCommentsSection);  
        };
    }else{
    ws.send(JSON.stringify({
    action: "list",
    request_id: new Date().getTime(),
    })); 
    };  
}
