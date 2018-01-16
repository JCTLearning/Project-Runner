<!-- login.html main Electron script -->
<!DOCTYPE html>

<html>
  <head>
    <meta charset="UTF-8">
    <title> Project Runner </title>
    <script type="text/javascript" src="login.js"></script>
  </head>


  <body>

	
    <h>  </h>
    <div id = "linking">
    <p></p>
    </div>
	<div id = "login">
    <input type="text" placeholder="Username" id="username"/>
    <input type="password" placeholder="Password" id="password"/>
	<div id = "b">
    <button type="button" id="loginButton"> Login </button>
	</div>
	</div>
    <p id='erroCont'></p>
	<div id = "logo">
	
	</div>
	<div id = "footer">
	<p><img src = "download.png" width = "20" height = "20"></p>
	<div id = "information">
	<a href="a" style = "font-size: 12px; color:#b5b6b7;"> About </a>
		</div>
	<div id = "copyright">
	<p> © 2018 Project Runner, Inc. <p>
	</div>
	<div id = "terms">
	<a href="terms.html" style = "font-size: 12px; color:#b5b6b7;"> Terms </a>
	</div>
	<div id = "privacy"> 
	<a href ="a" style = "font-size: 12px; color:#b5b6b7;"> Privacy </a>
	</div>
	<div id = "contact">
	<a href = "a" style = "font-size: 12px; color:#b5b6b7;"> Contact </a>
	</div>
	<div id = "register">
	<a href = "a" style = "font-size: 12px; color: #b5b6b7;"> Register </a>
	</div>
	<div id = "status">
	<a href = "a" style = "font-size: 12px; color: #b5b6b7;"> Status </a>
	</div>
	<style>
	#status {
	position: absolute;
	bottom: 20px;
	left: 80%
	}
	#register {
	position: absolute;
	bottom: 20px;
	left: 85%
	}
	#contact {
	position: absolute;
	bottom: 20px;
	left: 90%;
	}
	#privacy {
	position: absolute;
	bottom: 20px;
	left: 21%;
	}
	#terms {
	position: absolute;
	bottom: 20px;
	left: 17%;
	}
	#copyright {
	position: absolute;
	bottom: 8px;
	left: 2%;
	color:#b5b6b7;
	font-size: 12px;
	}
	#information {
	position: absolute;
	bottom: 20px;
	left: 95%;
	}
		#footer {
	position: absolute;
	right: 0;
	bottom: 0;
	left: 0;
	padding: 1 rem;
	background-color: #3a3a3a;
	text-align: center;
	
	}
	body {
	background:
	  linear-gradient(217deg, rgba(255,0,0,.8), rgba(255,0,0,0) 70.71%),
	  linear-gradient(127deg, rgba(0,0,255,0.3), rgba(0,255,0,0) 70.71%),
      linear-gradient(336deg, rgba(255,0,255,0.3), rgba(255,0,255,0.3) 70.71%);
	}
    #linking {
    position: absolute;
	left: 49%;
    bottom: 40%;
    font-size: 12px;
    }

	#login {
	position: absolute;
	left: 40%;
	top: 25%;
	width:20%;
	background-color: #ff6de4;
	border: 1px solid black;
	margin: 50px auto 0;
	padding: 1em;
	-moz-border-radius: 10px;
	-webkit-border-radius: 10px;
	}
	input[type=text], input[type=password] {
	margin: auto
	display: block;
	margin: 0 0 1em 0;
	width: 90%;
	border: 1px solid #818181;
	padding: 5px
	}
	#b { 
	font-size: 12px;
	}
	</style>
  </body>



</html>
