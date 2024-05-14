// websockets

var ws_scheme = window.location.protocol === "https:" ? "wss" : "ws";
      const ws = new WebSocket(
        ws_scheme
        + '://'
        + window.location.host
        + '/ws/'
      );
      var allComments = document.getElementById("allComments");
      var newComment = document.getElementById("newComments");

      ws.onopen = function(){
        ws.send(JSON.stringify({
            action: "list",
            request_id: new Date().getTime(),
        }))
        ws.send(JSON.stringify({
            action: "subscribe_to_comment_activity",
            request_id: new Date().getTime(),
        }))
      } 

      ws.onmessage = function(e){
          const data = JSON.parse(e.data); 
          console.log(data)
          switch(data.action) {

            case "list":
              allComments.textContent = JSON.stringify(JSON.parse(e.data), undefined, 2)
              break;

            default:
              newComment.textContent = JSON.stringify(JSON.parse(e.data), undefined, 2)        
              break;
          }
                      
      };

// comments creation on template
