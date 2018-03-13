const express = require('express');
const app = express();
const relaod = require('reload');
const path = require('path');
// const mongoose = require('mongoose');
const bparser = require('body-parser');


//mongodb connection
// mongoose.connect('mongodb://localhost/traversy');
// let db = mongoose.connection;
// var cards = null;
// db.once('open', () => {
// 	console.log('connected to mongoDB');
// 	cards = require('./models/cards');
// });

// db.on('error', (err) => {
// 	console.log(err);
// });

//set functions
app.set('port', 3000);
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug')
//use functions
// parse application/x-www-form-urlencoded
app.use(bparser.urlencoded({ extended: false }))

// parse application/json
app.use(bparser.json())
app.use(express.static(path.join(__dirname, '/public')));


//Routes
app.get('/', (req, res) => {
	res.render('index');
});

app.get('/images', (req, res) => {
	res.render('images', {
		responses: {'No Data': ' '},
		source: '/images.png'	
	});
});

app.get('/videos', (req, res) => {
	res.render('videos', {
		responses: {'No Data': ' '},
		source: '/videos.jpg',
		source2: ''
	});
});

app.post('/images', (req, res) => {
	let path = req.body.process;
	const spawn = require('child_process').spawn;
      const run = spawn('python', ['public/scripts/run.py', 'public/scripts/img/'+path]);

		run.stdout.on('data', (data) => {
		var response = JSON.parse(data);
		res.render('images', {
			responses: response,
			source: '/scripts/img/'+path
		});
	});
		run.stderr.on('data', (data) => {
		  console.log(`stderr: ${data}`);
	});
		run.on('close', (code) => {
		  console.log(`child process exited with code ${code}`);
	});
 });

app.post('/videos', (req, res) => {
	let path = req.body.process;
	const spawn = require('child_process').spawn;
      const run = spawn('python', ['public/scripts/videos.py', 'public/scripts/vid/'+path]);

      run.stdout.on('data', (data) => {
		var response = JSON.parse(data);
		console.log(response);
		res.render('videos', {
			responses: response,
			source: '/scripts/vid/'+path,
			source2: '/scripts/vid/'+path
		});
	});
		run.stderr.on('data', (data) => {
		  console.log(`stderr: ${data}`);
	});
		run.on('close', (code) => {
		  console.log(`child process exited with code ${code}`);
	});
});



const server = app.listen(app.get('port'), () =>{
	console.log('server is running on '+app.get('port'));
});

relaod(server, app);