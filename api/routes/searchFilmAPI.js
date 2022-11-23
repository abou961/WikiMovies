var express = require('express');
var router = express.Router();
//Import PythonShell module.
const {PythonShell} =require('python-shell');
const {exec, spawn} = require('child_process');

//Router to handle the incoming request.
router.get('*', function(req, res, next) {
	var capitalizedFirstInput = req.query.input.charAt(0).toUpperCase() + req.query.input.slice(1);

	var process = spawn('python',["./python/main.py", "0", capitalizedFirstInput]);
	var listResults;
	process.stdout.on('data', (data) => {
		console.log('Child Process STDOUT');
		listResults = JSON.parse(data);
		//listResults.films
		res.send(listResults);

	});
	process.stderr.on('data', (error) => {
		try{
			res.send(JSON.parse(error));
		} catch(e) {
			res.send(e);
		}
	});
});

module.exports = router;