var server = require('http').createServer(requestListener);
var io = require('../socket.io').listen(server);
var canvasManager = require('./canvas_manager.js');

var numOfusers = 0;


io.sockets.on('connection', function (socket) {
    socket.on('join', function (nickname) {
        if (nickname) {
            numOfusers++;
            socket.set('nickname', nickname, function () { });
            socket.broadcast.emit('join', nickname);
            socket.broadcast.emit('people_count', numOfusers);
            socket.emit('people_count', numOfusers);
            canvasManager.toDataURL(function(str) {
                socket.emit('canvas', str);
            });

        }
    });

    socket.on('action', function (action) {
        console.log(action);

        if (action.type == 'draw')
        {
            socket.get('pos', function(error, lastPos) {
				canvasManager.draw(action, lastPos);
				socket.set('pos', action.pos);
			});

        }
        else if (action.type == 'move')
        {
            //set the last position
            socket.set('pos', action.pos);
        }

        socket.broadcast.emit('action', action);
    });

    socket.on('disconnect', function () {
        socket.get('nickname', function (err, nickname) {
            if (nickname) {
                numOfusers--;
                socket.broadcast.emit('leave', nickname);
                socket.broadcast.emit('people_count', numOfusers);
            }
        });
    });
});

function requestListener(req, res) {
    res.end("hello world \n");
}

server.listen(8889);