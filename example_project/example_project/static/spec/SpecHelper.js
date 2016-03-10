beforeEach(function() {
    var jasVer = jasmine.version;

    var before2 = function(expectedSong) {
        var player = this.actual;
        return player.currentlyPlayingSong === expectedSong
          && player.isPlaying;
    }

    var ver2 = function (util) {
        return {
            compare: function (actual, expected) {
                result = {pass: util.equals(actual.currentlyPlayingSong, expected) && actual.isPlaying};
                return result
            }
        }
    }

    if (parseFloat(jasVer) >= 2.0) {
        jasmine.addMatchers({
            toBePlaying: ver2
        })
    } else {
        this.addMatchers({
            toBePlaying: before2
        })
    }
});
