// Purpose - This file contains all the logic relevant to the extension such as getting the URL, calling the server
function displayAlert(xhrResp){
	if (xhrResp == 'SAFE'){
		// Display safe message
		document.getElementById("safeAlert").style.display="block";
	}else if(xhrResp == 'PHISHING'){
		// Display dangerous message
		document.getElementById("phishingAlert").style.display="block";
	}else{
		// Display warning message
		document.getElementById("warningAlert").style.display="block";
	}

}

function transfer(){	
	var tablink;
	var xhrResp;
	chrome.tabs.getSelected(null,function(tab) {
	   	tablink = tab.url;
		// $("#mainText").text("The URL being tested is - "+tablink);
		$("#webUrl").text("The URL being tested is - "+tablink);

		var xhr=new XMLHttpRequest();
		params="url="+tablink;
        // alert(params);
		var temp = document.createElement("form");
		// var markup = "url="+tablink+"&html="+document.documentElement.innerHTML;
		var markup = "url="+tablink;
		// xhr.open("POST","http://127.0.0.1:8000/get_url/",false); //Django
		// xhr.open("POST","http://127.0.0.1:5000/get_url/",true); // FLASK
		xhr.open("POST","https://calm-peak-20355.herokuapp.com/get_url/",true); // Heroku app link
		
		xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		// xhr.setRequestHeader("Content-type", "text/plain");
		xhr.send(markup);
		// Uncomment this line if you see some error on the extension to see the full error message for debugging.
		// alert(xhr.responseText);
		// document.getElementById("mainText").innerHTML='Loading...';

		xhr.onreadystatechange=function(){
			// Justify if responses if finished：readystate=4
			// check if response availble again：xmlhttprequest object status=200
			 if(xhr.readyState==4 && xhr.status==200){
				// print response result：responseText
				xhrResp = xhr.responseText;
				// $("#div1").text(xhr.responseText);
				document.getElementById("myButton").style.display = "none";
				document.getElementById("mainText").innerHTML="Loaded";
				displayAlert(xhrResp);
				return xhrResp;
			
			 }else{
				 return("Timeout, please try again");
			 }
		 };
		// document.getElementById("warningAlert").style.display="block";
		
		return xhrResp;
	});
}
// window.onload = function (){
// 	divset = document.getElementsByClassName("aa");
// 	for (var i = 0; i<divset.length;i++) {
// 	  divset[i].style.display="none";
// 	};
// 	}
function clickCls1(){
	// function to delete phishing message
	document.getElementById("phishingAlert").style.display='none';
	// alert('clicked')
}
function clickCls2(){
	// function to delete safe message
	document.getElementById("safeAlert").style.display='none';
	// alert('clicked')
}
function clickCls3(){
	// function to delete warning message
	document.getElementById("warningAlert").style.display='none';
	// alert('clicked')
}

$(document).ready(function(){
    $("button").click(function(){	
		$("#mainText").text("Loading");
		document.getElementById("brick").style.display = "none";
		document.getElementById("loaderDiv").style.display = "block";
		var val = transfer();
		// $("#mainText").text("Loaded");
		// document.getElementById("mainText").innerHTML="Loaded";

    });
	// delete the message
	$("#clsBtn1").click(clickCls1);
	$("#clsBtn2").click(clickCls2);
	$("#clsBtn3").click(clickCls3);
});

chrome.tabs.getSelected(null,function(tab) {
   	var tablink = tab.url;
	$("#p1").text("The URL being tested is - "+tablink);
});

/*
document.addEventListener('DOMContentLoaded', function() {
    var link1 = document.getElementById('clsBtn1');
    // onClick's logic below:
    link1.addEventListener('click', function() {
        document.getElementById("phishingAlert").style.display='none';
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var link3 = document.getElementById('clsBtn2');
    // onClick's logic below:
    link3.addEventListener('click', function() {
        document.getElementById("safeAlert").style.display='none';
    });
});


document.addEventListener('DOMContentLoaded', function() {
    var link3 = document.getElementById('clsBtn3');
    // onClick's logic below:
    link3.addEventListener('click', function() {
        document.getElementById("warningAlert").style.display='none';
    });
});
*/