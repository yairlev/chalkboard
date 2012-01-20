var Canvas = require('canvas/lib/canvas');

canvas = new Canvas(800, 600);
ctx = canvas.getContext('2d');

var CanvasManager = function () {
}

CanvasManager.prototype = {

    draw:function (action, lastPos) {
        ctx.beginPath();
		ctx.lineWidth = 3;
        ctx.strokeStyle = action.color;
        ctx.moveTo(lastPos.x, lastPos.y);
        ctx.lineTo(action.pos.x, action.pos.y);
        ctx.stroke();

    },

    toDataURL: function(callback) {
        canvas.toDataURL(function(err, str) {
            callback.call(this, str);
        });
    }
}

module.exports = new CanvasManager();
