/* Javascript to do the poll */

window.onload = init;

var countGood = 0;
var countBad = 0;
var countIdc = 0;

function init(){
	if(!(localStorage.awesomeCount)){ /* Awesome */
		localStorage.awesomeCount = 0;
	}
	if(!(localStorage.terribleCount)){ /* Terrible */
		localStorage.terribleCount = 0;
	}
	if(!(localStorage.dontcareCount)){ /* Don't Care */
		localStorage.dontcareCount = 0;
	}
	
	drawSmiles();
}

function getData(){
	console.log("HAH! The button worked!");
	document.getElementById("pollForm").style.border = "none";
	if((document.getElementById("awesome").checked)){ /* Awesome */
		localStorage.awesomeCount = Number(localStorage.awesomeCount) + 1;
	}
	else if((document.getElementById("terrible").checked)){ /* Terrible */
		localStorage.terribleCount = Number(localStorage.terribleCount) + 1;
	}
	else if((document.getElementById("dontcare").checked)){ /* Don't Care */
		localStorage.dontcareCount = Number(localStorage.dontcareCount) + 1;
	}
	else{
		alert("Please select one");
		document.getElementById("pollForm").style.border = "solid";
		document.getElementById("pollForm").style.borderColor = "red";
	}
	
	drawSmiles();
}

function drawSmiles(){ /* STILL NEEDS FIXING */
	/* Get the li for each row */
	var good = document.getElementById("good")
	var bad = document.getElementById("bad")
	var idc = document.getElementById("idc")
	
	var happy = document.createElement("img");
	var sad = document.createElement("img");
	var why = document.createElement("img");
	
	happy.src = "../images/happy.png";
	sad.src = "../images/sad.png";
	why.src = "../images/why.png";
	
	happy.style.maxHeight = 60+"px";
	happy.style.maxWidth = 60+"px";
	sad.style.maxHeight = 60+"px";
	sad.style.maxWidth = 60+"px";
	why.style.maxHeight = 60+"px";
	why.style.maxWidth = 60+"px";
	
	/* Happy faces for like */
	while(countGood < localStorage.awesomeCount){
		/* add images to li here */
		console.log("countGood = " + countGood + " awesomeCount = " + localStorage.awesomeCount);
		good.appendChild(happy.cloneNode(true));
		/*good.appendChild(document.createElement("br"));*/
		countGood++;
	}
	
	/* Sad faces for dislike */
	while(countBad < localStorage.terribleCount){
		/* add images to li here */
		console.log("countBad = " + countBad + " terribleCount = " + localStorage.terribleCount);
		bad.appendChild(sad.cloneNode(true));
		/*good.appendChild(document.createElement("br"));*/
		countBad++;
	}
	
	/* Why face for don't care */
	while(countIdc < localStorage.dontcareCount){
		/* add images to li here */
		console.log("countIdc = " + countIdc + " dontcareCount = " + localStorage.dontcareCount);
		idc.appendChild(why.cloneNode(true));
		/*good.appendChild(document.createElement("br"));*/
		countIdc++;
	}
}
