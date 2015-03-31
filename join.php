<?php

session_start(); //keeps track of user data in the form

$submitno = 1; // start on page 1
$nextpage = $submitno + 1;
$prevpage = max($submitno - 1, 1);
$undergrad = isset($_SESSION['undergrad']) ? $_SESSION['undergrad'] : NULL;
$cornell = isset($_SESSION['cornell']) ? $_SESSION['cornell'] : NULL;
$cornell_grad = isset($_SESSION['cornell_grad']) ? $_SESSION['cornell_grad'] : NULL;
$msg = array("Basic Information", "Education", "Major", "College", "Major");
$currpage_msg = 'Part ' . $submitno . ': ' . $msg[$submitno - 1];
// $nextpage_msg = '"' . 'Part ' . $nextpage . ': ' . $msg[$submitno] . '"';
$nextpage_msg = '"' . 'Part ' . $nextpage . '"';
// $prevpage_msg = '"' . 'Part ' . $prevpage . ': ' . $msg[$submitno - 1] . '"';
$prevpage_msg = '"' . 'Back to Part ' . $prevpage . '"';



if ($undergrad) print 'pageload: is an undergrad';
if (!($undergrad)) print 'pageload: is grad';
if ($cornell) print 'pageload: is at cornell';
if (!($cornell)) print 'pageload: is elsewhere';

// if the user tries to access another page, or if the user submits
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
	$submit = $_POST['submit'];

	$submitno = max((int)substr($submit, 5, 1), 1);
	print $submitno;
	$nextpage = $submitno + 1;
	$prevpage = max($submitno - 1, 1);
	$currpage_msg = 'Part ' . $submitno . ': ' . $msg[$submitno - 1];
	$nextpage_msg = '"' . 'Part ' . $nextpage . '"';
	$prevpage_msg = '"' . 'Back to Part ' . $prevpage . '"';

	if (isset($_POST['form-student-level'])) {
		$undergrad = ($_POST['form-student-level'] == 'Undergraduate') ? TRUE : FALSE;
		print $_POST['form-student-level'];
		$_SESSION['undergrad'] = $undergrad;
	}

	if (isset($_SESSION['undergrad'])) {
		$undergrad = $_SESSION['undergrad'];
	}

	if (isset($_POST['form-college'])) {
		$cornell = ($_POST['form-college'] == 'Cornell') ? TRUE : FALSE;
		$_SESSION['cornell'] = $cornell;
	}

	if (isset($_SESSION['cornell'])) {
		$cornell = $_SESSION['cornell'];
	}

	if (isset($_POST['form-college-cornell-grad'])) {
		$cornell_grad = $_POST['form-college-cornell-grad'];
		$_SESSION['cornell_grad'] = $cornell_grad;
	}

	if (isset($_SESSION['cornell_grad'])) {
		$cornell_grad = $_SESSION['cornell_grad'];
	}

	// print '<div> ' . $submitno . '</div>';
	// print $submitno;
}


?>

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
<!--   	<div class="loader">
		<div id="preload">
			<img src="img/bears.png" alt="preload">
		</div>
	</div> -->
  	
	<?php include 'nav.php';?>
  	
  	<header class="divider-background">
		<div class="overlay background-dark-grey"></div>
		<img alt="Header Background" class="background-image" src="img/bg5.jpg" />
		
		<div class="row">
			<div class="medium-12 medium-centered columns text-center">
				<h2 class="text-white underline">Join</h2>
			</div>
		</div>
	
	</header>
    
	<section class="background-mid-grey">
		<div class="row">
			<div class="centerheading"><h6 class="page-title">Register Here</h6></div>
			<div class="centerheading"><h5><?=$currpage_msg?></h5></div>
			<form class="form-contact" action="join.php" method="post" enctype="multipart/form-data">
<!-- 
                       _   _               __  
                      | | (_)             /  | 
  __ _ _   _  ___  ___| |_ _  ___  _ __   `| | 
 / _` | | | |/ _ \/ __| __| |/ _ \| '_ \   | | 
| (_| | |_| |  __/\__ \ |_| | (_) | | | | _| |_
 \__, |\__,_|\___||___/\__|_|\___/|_| |_| \___/
    | |                                        
    |_|                                         -->
			<?php if ($submitno == 1): ?>

				<div class="centerheading"><h4>General Info</h4></div>
				<label for="form-fname">First Name</label>
				<input id="form-fname" type="text" placeholder="Your First Name" />
				<label for="form-lname">Last Name</label>
				<input id="form-lname" type="text" placeholder="Your Last Name" />
				<label for="form-email">Email</label>
				<input id="form-email" type="text" placeholder="Your Email" />
				<label for="form-netid">NetId</label>
				<input id="form-netid" type="text" placeholder="Your NetId" />

				<div class="centerheading"><h4>Are you an Undergraduate or Graduate?</h4></div>
				<select name="form-student-level">
					<option>Undergraduate</option>
					<option>Graduate</option>
				</select>
<!-- 				
                       _   _               _____ 
                      | | (_)             / __  \
  __ _ _   _  ___  ___| |_ _  ___  _ __   `' / /'
 / _` | | | |/ _ \/ __| __| |/ _ \| '_ \    / /  
| (_| | |_| |  __/\__ \ |_| | (_) | | | | ./ /___
 \__, |\__,_|\___||___/\__|_|\___/|_| |_| \_____/
    | |                                          
    |_|                                           -->


			
			<?php elseif ($submitno == 2): ?>
				<?php if ($undergrad === TRUE): ?>
				<div class="centerheading"><h4>What Year are You?</h4></div>
				<select name="form-role" id="form-role">
					<option value="Freshman">Freshman</option>
					<option value="Sophomore">Sophomore</option>
					<option value="Junior">Junior</option>
					<option value="Senior">Senior</option>
				</select>

				<div class="centerheading"><h4>Do you want a Mentor or Mentee?</h4></div>
				<select>
					<option>I want a Mentee</option>
					<option>I want an undergraduate Mentor</option>
					<option>I want a graduate Mentor</option>
					<option>I want an undergraduate or graduate Mentor</option>
				</select>

				<div class="centerheading"><h4>What College?</h4></div>
				<select name="form-college-cornell">
					<option>College of Agriculture and Life Sciences (CALS)</option>
					<option>College of Architecture, Art, and Planning (AAP)</option>
					<option>College of Arts and Sciences (AS)</option>
					<option>College of Engineering (ENG)</option>
					<option>School of Hotel Administration (SHA)</option>
					<option>College of Human Ecology (HumEc)</option>
					<option>School of Industrial and Labor Relations (ILR)</option>
				</select>

				<?php else: ?>
				<!-- <div class="centerheading"><h4>Previous Education?</h4></div> -->
				<div class="centerheading"><h4>Previous Education?</h4></div>
				<label for="grad-college">Your Undergraduate University/College</label>
				<input type="text" id="grad-college" placeholder="Hogwarts" name="grad-college">
				<label for="grad-deg">Degree Acquired</label>
				<select id="grad-deg">
					<option>Associate Degree</option>
					<option>Bachelor's Degree</option>
				</select>

				<label for="grad-major">Your Undergraduate Major / Field of Study</label>
				<select id="grad-college">
					<?php include 'bachelors2.php';?>
				</select>

				<div class="centerheading"><h4>Current Education</h4></div>
				<label for="grad-current-education">What Degree are you pursuing right now at Cornell?</label>
				<select id="grad-current-education" name="form-role">
					<option value="Master's">Master's</option>
					<option value="PhD">PhD</option>
				</select>

				<div class="centerheading"><h4>What Cornell Graduate School are You Part Of?</h4></div>
				<select name="form-college-cornell-grad">
					<option value="0">Cornell Tech</option>
					<option value="1">Cornell Law School</option>
					<option value="2">Samuel Curtis Johnson Graduate School of Management</option>
					<option value="3">College of Veterinary Medicine</option>
					<option value="4">Weill Cornell Medical College</option>
					<option value="5">Other</option>
				</select>


				<?php endif; ?>
<!-- 				
                       _   _               _____ 
                      | | (_)             |____ |
  __ _ _   _  ___  ___| |_ _  ___  _ __       / /
 / _` | | | |/ _ \/ __| __| |/ _ \| '_ \      \ \
| (_| | |_| |  __/\__ \ |_| | (_) | | | | .___/ /
 \__, |\__,_|\___||___/\__|_|\___/|_| |_| \____/ 
    | |                                          
    |_|                                           -->


			<?php elseif ($submitno == 3): ?>
				<?php if ($cornell === FALSE && $undergrad === FALSE): ?>

				
				<?php elseif ($cornell === TRUE && $undergrad === FALSE && $cornell_grad == '0'): ?>
				<div class="centerheading"><h4>What Field of Study at Cornell Tech?</h4></div>
				<select name="form-tech" id="form-tech">
					<option>MEng in Computer Science</option>
					<option>MS in IS, Connective Media</option>
					<option>MBA Johnson Cornell Tech</option>
					<option>MS in IS, Healthier Life</option>
					<option>PhD Computer Science</option>
					<option>PhD Electrical and Computer Engineering</option>
					<option>PhD Information Science</option>
				</select>

				<?php elseif ($cornell === TRUE && $undergrad === FALSE && $cornell_grad == '1'): ?>
				<div class="centerheading"><h4>What Field of Study at Cornell Law School?</h4></div>
				<select name="form-law" id="form-law">
					<option>Juris Doctor (JD)</option>
					<option>Master of Laws (LL.M.)</option>
					<option>Doctor of Juridical Science (J.S.D.)</option>
					<option>Joint Program with Johnson Grad School of Management (JD/MBA)</option>
					<option>Joint Program with Cornell School of ILR (JD/MILR)</option>
					<option>Joint Program with Cornell Institute for Public Affairs (JD/MPA)</option>
					<option>Joint Program with Cornell College of Architecture, Art, and Planning (JD/MRP)</option>
					<option>Joint Program in International and Comparative Law (JD/LL.M)</option>
					<option>Other (Specify)</option>
				</select>

				<?php elseif ($cornell === TRUE && $undergrad === FALSE && $cornell_grad == '2'): ?>
				<div class="centerheading"><h4>What Field of Study at the Johnson?</h4></div>
				<select name="form-role" id="form-role">
					<option>MBA</option>
					<option>Accelerated MBA (AMBA)</option>
					<option>MBA/MEng</option>
					<option>MBA/MD</option>
					<option>MBA/ILR</option>
					<option>MPA/MPS</option>
					<option>MBA/MPA</option>
					<option>PhD (Specify)</option>
				</select>

				<?php elseif ($cornell === TRUE && $undergrad === FALSE && $cornell_grad == '3'): ?>
				<div class="centerheading"><h4>What Field of Study at the Vet School?</h4></div>
				<select>
					<option>The Biological and Biomedical Sciences (BBS) Graduate Program</option>
				</select>

				<?php elseif ($cornell === TRUE && $undergrad === FALSE && $cornell_grad == '4'): ?>
				<div class="centerheading"><h4>What Field of Study at Weill Cornell Medical College?</h4></div>
				<select name="form-role" id="form-role">
					<option>Tri-Institutional MD-PhD Program</option>
					<option>M.D. with Honors in Research Program</option>
					<option>M.D. with Honors in Service Program</option>
					<option>MD-MBA Program</option>
					<option>Global Health</option>
					<option>Music and Medicine</option>
					<option>Humanism in Medicine</option>
				</select>

				<?php elseif ($cornell === TRUE && $undergrad === FALSE && $cornell_grad == '5'): ?>
				<div class="centerheading"><h4>What Field of Study at Cornell?</h4></div>
				<select>
					<?php include 'graduatelist.php';?>
				</select>

				<?php else: ?>
				<select>
					<option>Agricultural Sciences</option>
					<option>Animal Science</option>
					<option>Applied Economics and Management</option>
					<option>Atmospheric Science</option>
					<option>Biological Engineering</option>
					<option>Biological Sciences</option>
					<option>Biology and Society</option>
					<option>Biometry and Statistics</option>
					<option>Communication</option>
					<option>Development Sociology</option>
					<option>Entomology</option>
					<option>Environmental Engineering</option>
					<option>Environmental Science and Sustainability (new students only)</option>
					<option>Food Science</option>
					<option>Information Science</option>
					<option>Interdisciplinary Studies (current students only)</option>
					<option>International Agriculture and Rural Development</option>
					<option>Landscape Architecture</option>
					<option>Natural Resources (current students only)</option>
					<option>Nutritional Sciences</option>
					<option>Plant Sciences</option>
					<option>Science of Earth Systems</option>
					<option>Science of Natural and Environmental Systems (current students only)</option>
					<option>Viticulture and Enology</option>
				</select>

				<?php endif; ?>
<!-- 
                       _   _                 ___ 
                      | | (_)               /   |
  __ _ _   _  ___  ___| |_ _  ___  _ __    / /| |
 / _` | | | |/ _ \/ __| __| |/ _ \| '_ \  / /_| |
| (_| | |_| |  __/\__ \ |_| | (_) | | | | \___  |
 \__, |\__,_|\___||___/\__|_|\___/|_| |_|     |_/
    | |                                          
    |_|                                           -->


<!-- 				
                       _   _               _____ 
                      | | (_)             |  ___|
  __ _ _   _  ___  ___| |_ _  ___  _ __   |___ \ 
 / _` | | | |/ _ \/ __| __| |/ _ \| '_ \      \ \
| (_| | |_| |  __/\__ \ |_| | (_) | | | | /\__/ /
 \__, |\__,_|\___||___/\__|_|\___/|_| |_| \____/ 
    | |                                          
    |_|                                           -->


<!-- 				<label for="form-degree">What Degree?</label>
				<select name="form-degree" id="form-degree">
					<option value="Bachelors">Bachelors</option>
					<option value="Masters">Master's</option>
					<option value="Doctorate">Doctorate</option>
				</select> -->

				<!-- <label for="form-tech">If you went to Cornell's NYC Tech Campus</label>
				








				<p>Your Gender</p>
				<select name="form-gen" id="form-gen">
					<option>Male</option>
					<option>Female</option>
					<option>Other</option>
				</select>

				<p>Ethnicity</p>
				<input type="text" placeholder="Hometown">

				<p>Professional Interests</p>
-->
			<?php endif; ?>
				<div class="prevnext">
					<input type="submit" class="button button-small tim" name="submit" value=<?=$prevpage_msg?> />
					<input type="submit" class="button button-small tim" name="submit" value=<?=$nextpage_msg?> />
				</div>
<!-- 				<div id="details-error">*Please complete all fields correctly!</div>
				<div id="form-sent">Thank you, your enquiry has been sent!</div> -->
			</form>
		</div>
	</section>
	
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
