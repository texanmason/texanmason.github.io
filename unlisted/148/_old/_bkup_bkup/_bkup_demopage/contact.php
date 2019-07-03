<?php

if($_POST["submit"]) {
	$recipient="9792854244@mms.att.net";
	$subject=$_POST["category"];
	$sender=$_POST["name"];
	$senderEmail=$_POST["email"];
	$message=$_POST["message"];
	
	$mailBody="Name: $sender\nEmail: $senderEmail\n\n$message";
	
	mail($recipient,$subject,$mailBody, "From: $sender <$senderEmail>");
	
	$thankYou="<p>Thank you! Your message has been sent and we well contact you shortly.</p>";
	}
?>