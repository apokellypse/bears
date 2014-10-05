<!doctype html>
<html class="no-js" lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title> Cornell Bears | Building Empowered and Resourceful Scholars</title>
    <meta name="description" content="Cornell BEARS website">
    <meta name="keywords" content="Cornell BEARS website mentor mentee">
    <meta name="author" content="Mark Yoon">
    <META HTTP-EQUIV="expires" CONTENT="Sun, 31 Aug 2014 08:00:00 GMT">
    <link rel="icon" type="image/ico" href="img/bear.gif"/>
    <link rel="stylesheet" href="css/loader.css" />
    <link rel="stylesheet" href="css/foundation.css" />
    <link rel="stylesheet" href="css/animate.min.css" />
    <link rel="stylesheet" href="css/elegant-icons.css" />
    <link rel="stylesheet" href="css/outline-icons.css" />
    <link rel="stylesheet" href="css/flexslider.css" />
    <link rel="stylesheet" href="css/style.css" />
    <link rel="stylesheet" href="css/responsive.css" />
    <script src="js/vendor/modernizr.js"></script>
    <link href='http://fonts.googleapis.com/css?family=Open+Sans:400italic,400,600,700%7CRaleway:400,700' rel='stylesheet' type='text/css'>
  </head>
  <body>

<?php

//where the .errorbox div is:
$varMessage = "";

//http://www.html-form-guide.com/php-form/php-form-tutorial.html
if ($_POST['submit'] == "Submit") {
	$varPlscomplete = "";
	if (empty($_POST['mentor'])) {
		$varPlscomplete = '<div class="incomplete">You need to enter in the Mentor\'s ID.</div>';
	}
	if (empty($_POST['mentee'])) {
		$varPlscomplete = $varPlscomplete . '<div class="incomplete">You need to enter in the Mentee\'s ID.</div>';
	}
	$varMentor = $_POST['mentor'];
	$varMentee = $_POST['mentee'];

	if(!empty($varPlscomplete)) {
		$varMessage = '<div class="incomplete">There was an error with your form:' . $varPlscomplete . "</div>";
	}
}

//begin handling picture upload:


if ($_SERVER['REQUEST_METHOD'] == 'POST') { 

$allowedExts = array("gif", "jpeg", "jpg", "png", "GIF", "JPEG", "JPG", "PNG");
$temp = explode(".", $_FILES["the_file"]["name"]); //separates the name into an array, and grabs the extension name
$extension = end($temp);

//now we want to access the mentor and mentee name so we can rename the picture to be mentorNetID_menteeNetID_month_day_militarytime

$mentorNetID = $_POST['mentor'];
// echo ($mentorNetID);
$menteeNetID = $_POST['mentee'];
// echo ($menteeNetID);
// echo $_SERVER['REQUEST_TIME'];


//GETTING TIME
date_default_timezone_set("America/New_York");

//below 4 lines are from php.net
$nextWeek = time() + (7 * 24 * 60 * 60);
                   // 7 days; 24 hours; 60 mins; 60 secs
// echo 'Now:       '. date('Y-m-d H:i:s') ."\n";
$year = date('Y');
$month = date('m');
$date = date('d');
$hour = date('H');
$min = date('i');
$sec = date('s');

// echo 'Next Week: '. date('Y-m-d', $nextWeek) ."\n";

if ((($_FILES["the_file"]["type"] == "image/gif")
	|| ($_FILES["the_file"]["type"] == "image/jpeg")
	|| ($_FILES["the_file"]["type"] == "image/jpg")
	|| ($_FILES["the_file"]["type"] == "image/pjpeg")
	|| ($_FILES["the_file"]["type"] == "image/x-png")
	|| ($_FILES["the_file"]["type"] == "image/png"))
	&& ($_FILES["the_file"]["size"] < 2000000)
	&& in_array($extension, $allowedExts)) {

	if ($_FILES["the_file"]["error"] > 0) {
		// echo '<div class="upload_fail">We encountered an error: ' . $_FILES["the_file"]["error"] . "</div>";
		if ($varMessage == "") $varMessage = '<div class="upload_fail">We encountered an error: ' . $_FILES["the_file"]["error"] . "</div>";
	} else {
		$newname = "" . $mentorNetID . "_" . $menteeNetID . '_' . $year . '_' . $month . '_' . $date . '_' . $hour . '_' . $min . '_' . $sec . '_' . "." . $extension;
		// if (file_exists("uploads/{$_FILES['the_file']['name']}")) {
		if (file_exists("uploads/" . $newname)) {
			// echo '<div class="upload_warning">' . $_FILES["the_file"]["name"] . " already exists in our database.</div>";
			if ($varMessage == "") $varMessage = '<div class="upload_warning">' . $_FILES["the_file"]["name"] . " already exists in our database.</div>";
		} else {
			if (move_uploaded_file($_FILES['the_file']['tmp_name'], "uploads/" . $newname)) { //I've renamed the file
				// print '<div class="upload_success">Your picture has been uploaded! Great job this month!</div>';
				if ($varMessage == "") $varMessage = '<div class="upload_success">Your picture has been uploaded! Great job this month!</div>';
			
				//begin handling saving data to .csv file
				$fs = fopen("data.csv", "a");
				fwrite($fs, $varMentor . ", " . $varMentee . "\n");
				fclose($fs);

				// header("index.php");
				// exit;

			} else { 
				print '<div class="upload_fail">Your file could not be uploaded because: ';
				switch ($_FILES['the_file']['error']) {
					case 1:
						print 'you exceeded the max upload size which is 2 MB';
						break;
					case 2:
						print 'you exceeded the max upload size which is 2 MB';
						//exceeded max file size in html form
						break;
					case 3:
						print 'your file was only partially uploaded';
						break;
					case 4:
						print 'there was no file specified';
						break;
					case 6:
						print 'our temp folder does not yet exist';
						break;
					default:
						print 'of an unsepcified error';
						break;
				}
				print '. Please try again.</div>'; 
			} 
		}
	}
} else {
	// echo '<div class="upload_fail">You have tried to upload an invalid file type, or your file is too big (please keep sizes under 2 MB).</div>';
	if ($varMessage == "") $varMessage = '<div class="upload_fail">You have tried to upload an invalid file type, or your file is too big (please keep sizes under 2 MB).</div>';
}
}

?>

<!--removing preload because takes too darn long-->
<!--changed my mind, it stalls while the rest of the page to format, which is nice-->
  	<div class="loader">
			<div id="preload">
				<img src="img/bears.png" alt="preload">
			</div>
		</div>
  	
  	<nav class="nav-transparent overlay-nav sticky-nav">
  	
  		<div class="row">
  			<div class="medium-3 columns">
  				<a class="bears-logo-text" href="index.html">BEARS</a>
  			</div>
  			
  			<div class="medium-9 columns text-right">
  				<ul class="menu">
  					<li><a href="index.html">Home</a></li>
  					<li><a href="about-us.html">About Us</a></li>
  					<!-- <li><a href="https://cornell.qualtrics.com/SE/?SID=SV_cIT8rVXLtnTyG5n">Join</a></li> -->
  					<li><a href="members.php">Members</a></li>
  					<li><a href="faq.html">FAQ</a></li>
  					<li><a href="contact.html">Contact</a></li>
  				</ul>
  			</div>
  		</div>
  		
  		<div class="mobile-toggle"><i class="icon icon_menu"></i></div>
  	
  	</nav><!--end of navigation-->
  	
  	<header class="divider-background">
		<div class="overlay background-dark-grey"></div>
		<img alt="Header Background" class="background-image" src="img/bg6.jpg" />
		
		<div class="row">
			<div class="medium-12 medium-centered columns text-center">
				<h2 class="text-white underline">Members</h2>
			</div>
		</div>
	
	</header>

	<section class="background-white errorbox">
		<?=$varMessage;?>
	</section>

<!-- 	<section class="background-white errorbox">
		<?=$varPlscomplete;?>
	</section> -->

   	<section class="background-white logformsection">

   		<div class="row">
			<h3 class="headtitle">Current Members Only</h3>
		</div>
   		<div class="text-center">
   			<div id="logform">
			<a href="javascript:void(0)" id="logformclick" class="button button-small button-black button-filled">Upload Monthly Picture Here!<i class="icon icon_upload"></i></a>
				<form action="members.php" method="post" enctype="multipart/form-data">
					<div class="logformbox">
						<label for="text">Mentor NetID:</label>
						<input type="text" name="mentor" maxlength="7" placeholder="type here">
					</div>
					<div class="logformbox">
						<label for="text">Mentee NetID:</label>
						<input type="text" name="mentee" maxength="7" placeholder="type here">
					</div>
					<label for="file">Browse for the picture</label>
					<input type="file" name="the_file" id="file"><br>
					<!-- <input type="image" name="the_file" id="file"><br> -->
					<label for="submit">Press Submit after you've selected your picture</label>
					<input type="submit" name="submit" value="Submit">
				</form>
			</div>
		</div>
	</section>

	<section class="background-mid-grey">
	
<!-- 		<div class="row">
			<div class="medium-12 columns">
				<h6 class="page-title">Members</h6>
			</div>
		</div> -->
	
		<div class="row">

			<h3 class="headtitle">BEARS Roster Fall 2014</h3>
			<div class="headquote">Meet the Bears Pairs!</div>

			<h6 style="text-align: center;">Mentors &amp; Mentees</h6>
			<div class="horizontal-line"></div>
				
			<div class="medium-4 columns text-center">
				<p style="text-align: center; color: black;">
					Natasha Deb &amp; Saie Ganoo<br>
					Anthony Halmon &amp; Da Hee Kim<br>
					Jeff Horner &amp; Dhruv Gaba<br>
					Lauren Ferraiuolo &amp; Jennifer Eppinger<br>
					Carly Schuller &amp; Nicole Levine<br>
					Michael Kaplan &amp; Lauren Lin<br>
					Mark Yoon &amp; Neil Chand<br>
					Pooja Shah &amp; Nora Rabah<br>
					Nicole Altomare &amp; Sarah Hanif<br>
					Andrew Dabydeen &amp; Koonj Vekaria<br>
					Kaysie Anderson &amp; Jing Si<br>
					Kimberly Blacutt &amp; Matthew Flores<br>
					Taylor Hale &amp; Shamae Burrell<br>
					Alexandra McClellan &amp; Christina Thomas<br>
					Fangfang Wan &amp; Mary Chen<br>
					James Dunlea &amp; Shreya Mathur<br>
					Mark LaPointe &amp; Alyssa Bruce<br>
					Tori Ricelli &amp; Gabrielle Villafana<br>
					Olivia Vaz &amp; Justin Bae<br>
					Shayan Salam &amp; Jack Kim<br>
					Ee Khoo &amp; Ke Wang<br>
					Evelyn Haynes &amp; Melody Spencer<br>
					Mohamed Alsabbagh &amp; Meredith Thompson<br>
					Allie Saint Laurent &amp; Alekhya Chaparala<br>
					Hope Sailer &amp; Marissa Patel<br>
					Logan Stevenson &amp; Lia Tan<br>
					Joe Barsotti &amp; Kevin Kee<br>
					Lydia Mrowiec &amp; Jasmine Liu<br>
					Max Weisbrod &amp; Morgan Palmiter<br>
					Morgan Shelton &amp; Maria Chak<br>
					James Palmer &amp; Nicole Tan<br>
				</p>
			</div>

			<div class="medium-4 columns text-center">
				<p style="text-align: center; color: black;">
					Moyosola Soyemi &amp; Jesrae Johnson<br>
					Jacky Falkenberg &amp; Richard Shin<br>
					Virginia Giard &amp; Ava jarvis<br>
					Phoebe Ross &amp; Alexandra Galleta<br>
					Sarah Harrison &amp; Albert Kung<br>
					Lauren Cooley &amp; Tiffany Fotopoulos<br>
					Ebere Joseph &amp; Deanna Deyhim<br>
					Rachel Murro &amp; Anna mo<br>
					Rohit Biswas &amp; Esther Chen<br>
					Stephanie Chan &amp; Shuqing Tang<br>
					Jenny Feng &amp; Crystal Liu<br>
					Bridget Charhut &amp; Kwabena Nimo<br>
					Christina Seo &amp; Daniel Kim<br>
					Gaylord Minet &amp; Amy Gilligan<br>
					Will Shao &amp; Elizabeth Yam<br>
					Justin &amp; Richard Wu<br>
					Kelsey Bernal &amp; Maria Chak<br>
					Coffy &amp; James Gan<br>
					Zach Praiss &amp; Nethan Reddy<br>
					Jonathan Dawson &amp; Ashley Vincent<br>
					Sueho Lee &amp; Alex Huang<br>
					Jackie Gerow &amp; Sachi Koide<br>
					Sophia Levine &amp; Sophia Yang<br>
					Jenna Marinstein &amp; Zoe Kalos<br>
					Kendall Scanlon &amp; Samuel Turer<br>
					Daniel Klausner &amp; Raymond Chung<br>
					Kelly Jirka &amp; Meng Tong<br>
					Susan Liao &amp; Tenzin Dechen<br>
					Molly Orbon &amp; Elizabeth Gorman<br>
					Abigail Forth &amp; Jacqueline Pecaro<br>
					Hannah Mezheritsky &amp; Jiangshan Yan<br>
					Kern Sharma &amp; Eric Dai<br>
				</p>
			</div>

			<div class="medium-4 columns text-center">
				<p style="text-align: center; color: black;">
					Emma Lichtenstein &amp; Yufei Yi<br>
					Anudeep Gavini &amp; Sophie Li<br>
					Minkyu Kim &amp; Alexandra Nagele<br>
					Elizabeth Selva &amp; Justin Lio<br>
					Abram Saroufim &amp; Alina Kim<br>
					Yena Kang &amp; Catherine Li<br>
					Nick Mileti &amp; Yashvi Gattani<br>
					Christian Kim &amp; Janilya Baizack<br>
					Eunu Song &amp; Christina Xu<br>
					Nadia Mckinney &amp; Angela Zhang<br>
					Janice Lopez &amp; Jennifer Mizhquiri<br>
					Tae Hoon Kim &amp; Sung Min Lee<br>
					Christine Leu &amp; Wenjia You<br>
					Tom Zhao &amp; Frenda Yip<br>
					Karen Ortega &amp; Rachel Kim<br>
					Imani Sanders &amp; Christopher Yoo<br>
					Timothy Arena &amp; Samantha Hunter<br>
					Jade Algarin &amp; Genesis Miranda Soto<br>
					Justin Yu &amp; John Fitzpatrick<br>
					Yifei Wu &amp; Xinlu (Grace) Ye<br>
					Isabella Leon &amp; Rosalyn Xu<br>
					Brooke Neider &amp; Amberly Robinson<br>
					Danielle Soloway &amp; Ibrahym Sabha<br>
					Catherine Bravo &amp; Inyoung Hong<br>
					Paola Rosa-Aquino &amp; Xiaoning Wang<br>
					Jasmine Khayami &amp; Simon Wynter<br>
					Lisa Feng &amp; Juyoung Lee<br>
					Lillian Chen &amp; Yu Gu<br>
					Nabiha Keshwani &amp; Janaki Narayanan<br>
					Emma Scher &amp; Patricia Zhang<br>
					William Wong &amp; Grace Park<br>
				</p>
			</div>
			
		</div>
	
	</section><!--end home features-->
				
	<footer class="dark">
		
		<div class="row">
			<div class="medium-3 columns">
				<img alt="Logo" src="img/logo.png" class="logo push-bottom" />
				<p class="push-bottom-small">
					Building Empowered and Resourceful Scholars
				</p>
			</div>
			
			<div class="medium-3 columns"></div>
			
			<div class="medium-3 columns"></div>
			
			<div class="medium-3 columns">
				<h6><a href="contact.html">Contact Us</a></h6>
				<p class="push-bottom-small">
					Cornell University<br />
					Ithaca, NY 14850
				</p>
				<p>
					<i class="icon icon_mail"></i> bearscornell@gmail.com 
				</p>
			</div>
		</div>
		
		<div class="footer-lower">
			<div class="row">
				<div class="medium-7 columns">
					<span>Copyright © 2014 - Design by <a href="http://mark-yoon.com"><strong>Mark Yoon</strong></a> &amp;&amp; Cover Photos by <a href="http://kellyyu.com"><strong>Kelly Yu</strong></a></span>
				</div>
				
				<div class="medium-5 columns text-right">
					<ul class="social-profiles">
						<li><a href="https://www.facebook.com/cornellbears"><i class="icon social_facebook"></i></a></li>
						<li><a href="/contact.html"><i class="icon icon_mail"></i></a></li>
					</ul>
				</div>
			</div>
		</div>
			
		
	</footer>
    
    <script src="js/vendor/jquery.js"></script>
    <script src="js/foundation.min.js"></script>
    <script src="js/jquery.flexslider-min.js"></script>
    <script src="js/smooth-scroll.js"></script>
    <script src="js/isotope.pkgd.min.js"></script>
    <script src="js/inview.js"></script>
    <script src="js/skrollr.min.js"></script>
    <script src="js/scripts.js"></script>
    <script>
      $(document).foundation();
    </script>
  </body>
</html>
