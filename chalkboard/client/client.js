(function () {

    var socket;

    var eventController = function () {
    }

    eventController.prototype = {
        addEventListener: function (name, callback) {
            this[name] = callback;
        },				

        connect: function (nickname) {

            socket = io.connect('http://localhost:8888');

            socket.on('connect', function () {
                socket.emit('join', nickname)
            });

            socket.on('action', function (action) {
                if (EventController['action']) {
                    EventController['action'].call(this, action);
                }
            });

            socket.on('join', function (nickname) {
                if (EventController['join']) {
                    EventController['join'].call(this, nickname);
                }
            });

            socket.on('leave', function (nickname) {
                if (EventController['leave']) {
                    EventController['leave'].call(this, nickname);
                }
            });

            socket.on('people_count', function (count) {
                if (EventController['people_count']) {
                    EventController['people_count'].call(this, count);
                }
            });

			socket.on('canvas', function (canvasData) {
				if (canvasData && EventController['canvas'])
				{
					EventController['canvas'].call(this, canvasData);
				}
			});

            
        },

        sendAction: function (action) {
            socket.emit('action', action);
        }
        
    }

    window.EventController = new eventController();

})();