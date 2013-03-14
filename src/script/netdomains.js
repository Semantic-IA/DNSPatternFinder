// END of ParseUri
// BEGIN modified netlog.js example by PhantomJS
// Source: https://github.com/ariya/phantomjs/blob/master/examples/netlog.js
// Source of PhantomJS: https://github.com/ariya/phantomjs
// Original Code distributed under the BSD License

var page = require('webpage').create(),
    system = require('system'),
    address, set = {};
try {
	
	if (system.args.length === 1) {
	    console.log('Usage: netdomain.js <some URL>');
	    phantom.exit(1);
	} else {
	    address = system.args[1];
	
	    page.onResourceReceived = function (res) {
	        var data = JSON.stringify(res.url, undefined, 4).split("/")[2];
		if (~data.indexOf(".")) {  // Check if String contains "." (if not, it is a false positive)
		    if (data.substring(0,4) == "www.") { // Remove www., if it is there
			data = data.substring(4);
		    }
		    set[data] = true; // Save data
		}
	    };
	    page.onError = function(err) {
	    };
	
	    page.open(address, function (status) {
	        if (status !== 'success') {
	            console.log('FAIL to load the address');
		    phantom.exit(1);
	        }
		console.log(Object.keys(set).toString());
	        phantom.exit();
	    });
	}
	// END Modified netlog.js example
}
catch(err) {
	console.log(Object.keys(set).toString());
	phantom.exit();
}
