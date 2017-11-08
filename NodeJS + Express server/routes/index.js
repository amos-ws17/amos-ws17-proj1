var express = require('express');
var router = express.Router();

/* GET home page. */
//router.get('/', function(req, res, next) {
//  res.render('index', { title: 'Express' });
//});

router.get('/', function(req, res, next) {
  res.send('Hello World');
});

router.get('/login', function(req, res, next) {
    res.send('Login');
});
module.exports = router;
