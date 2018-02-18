function output(file) {
	if (document.getElementById){
		 objXml = new XMLHttpRequest();
		 objXml.open("GET",file,false);
		 objXml.send(null);
		 document.write(objXml.responseText);
     }
}

function output1(file, attr1) {
	if (document.getElementById){
		 objXml = new XMLHttpRequest();
		 objXml.open("GET",file,false);
		 objXml.send(null);
		 document.write(objXml.responseText.replace("<attr1/>", attr1));
     }
}

function blocking(nr) {
	displayNew = (document.getElementById(nr).style.display == 'none') ? 'block' : 'none';
	buttonText = (document.getElementById(nr).style.display != 'none') ? 'Expand' : 'Collapse';
	document.getElementById(nr).style.display = displayNew;
	document.getElementById(nr + 'Button').text = buttonText;
}