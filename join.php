<?php

session_start(); //keeps track of user data in the form

// form titles
$msg = array("Basic Information", "Education", "Major", "More About You", "Professional Interests");

$submitno = 1; // start on page 1
$nextpage = $submitno + 1;
$prevpage = max($submitno - 1, 1);

// variables to track who the person is
$undergrad = isset($_SESSION['undergrad']) ? $_SESSION['undergrad'] : NULL;
$cornell = isset($_SESSION['cornell']) ? $_SESSION['cornell'] : NULL;
$cornell_grad = isset($_SESSION['cornell_grad']) ? $_SESSION['cornell_grad'] : NULL;
$cornell_ugrad = isset($_SESSION['cornell_ugrad']) ? $_SESSION['cornell_ugrad'] : NULL;

// displayed on prev/next buttons
$currpage_msg = 'Part ' . $submitno . ': ' . $msg[$submitno - 1];
$nextpage_msg = ($nextpage == 6) ? 'Submit' : '"' . 'Part ' . $nextpage . '"';
$prevpage_msg = ($prevpage == 1 && $nextpage != 3) ?  '"" style="visibility:hidden"' : '"' . 'Back to Part ' . $prevpage . '"';




// if ($undergrad) print 'pageload: is an undergrad';
// if (!($undergrad)) print 'pageload: is grad';
// if ($cornell) print 'pageload: is at cornell';
// if (!($cornell)) print 'pageload: is elsewhere';

// if the user tries to access another page, or if the user submits
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
	$submit = $_POST['submit'];

	// extract the number X from the string "Back to Part X" or "Part X"
	$submitno = (strlen($submit) > 6) ? max((int)substr($submit, 13, 1), 1) : max((int)substr($submit, 5, 1), 1);

	// print $submitno;
	$nextpage = $submitno + 1;
	$prevpage = max($submitno - 1, 1);
	$currpage_msg = 'Part ' . $submitno . ': ' . $msg[$submitno - 1];
	$nextpage_msg = ($nextpage == 6) ? 'Submit' : '"' . 'Part ' . $nextpage . '"';
	$prevpage_msg = ($prevpage == 1 && $nextpage != 3) ?  '"" style="visibility:hidden"' : '"' . 'Back to Part ' . $prevpage . '"';

	if (isset($_POST['form-student-level'])) {
		$undergrad = ($_POST['form-student-level'] == 'Undergraduate') ? TRUE : FALSE;
		// print $_POST['form-student-level'];
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

	if (isset($_POST['form-college-cornell'])) {
		$cornell_ugrad = $_POST['form-college-cornell'];
		$_SESSION['cornell_ugrad'] = $cornell_ugrad;
	}

	if (isset($_SESSION['cornell_ugrad'])) {
		$cornell_ugrad = $_SESSION['cornell_ugrad'];
	}

	if ($submit == 'Submit') {
		print 'form submitted';	
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
					<option value="0">College of Agriculture and Life Sciences (CALS)</option>
					<option value="1">College of Architecture, Art, and Planning (AAP)</option>
					<option value="2">College of Arts and Sciences (AS)</option>
					<option value="3">College of Engineering (ENG)</option>
					<option value="4">School of Hotel Administration (SHA)</option>
					<option value="5">College of Human Ecology (HumEc)</option>
					<option value="6">School of Industrial and Labor Relations (ILR)</option>
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

				<label for="form-cornell-grad-school">What Cornell Graduate School are You Part Of?</label>
				<select name="form-college-cornell-grad" id="form-cornell-grad-school">
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

				<?php if ($undergrad === FALSE && $cornell_grad == '0'): ?>
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

				<?php elseif ($undergrad === FALSE && $cornell_grad == '1'): ?>
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

				<?php elseif ($undergrad === FALSE && $cornell_grad == '2'): ?>
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

				<?php elseif ($undergrad === FALSE && $cornell_grad == '3'): ?>
				<div class="centerheading"><h4>What Field of Study at the Vet School?</h4></div>
				<select>
					<option>The Biological and Biomedical Sciences (BBS) Graduate Program</option>
				</select>

				<?php elseif ($undergrad === FALSE && $cornell_grad == '4'): ?>
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

				<?php elseif ($undergrad === FALSE && $cornell_grad == '5'): ?>
				<div class="centerheading"><h4>What Field of Study at Cornell?</h4></div>
				<select>
					<?php include 'graduatelist.php';?>
				</select>

				
				<?php elseif ($undergrad === TRUE && $cornell_ugrad == '0'): ?>
				<div class="centerheading"><h4>What Major in CALS?</h4></div>
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

				<?php elseif ($undergrad === TRUE && $cornell_ugrad == '1'): ?>
				<div class="centerheading"><h4>What Major in AAP?</h4></div>
				<select>
					<option>Architecture</option>
					<option>Art</option>
					<option>Urban and Regional Planning</option>
				</select>

				<?php elseif ($undergrad === TRUE && $cornell_ugrad == '2'): ?>
				<div class="centerheading"><h4>What Major in A&amp;S?</h4></div>
				<select>
					<option>Africana Studies</option>
					<option>American Studies</option>
					<option>Anthropology</option>
					<option>Archaeology</option>
					<option>Asian Studies</option>
					<option>Astronomy</option>
					<option>Biological Sciences</option>
					<option>Biology &amp; Society</option>
					<option>Chemistry and Chemical Biology</option>
					<option>China and Asia-Pacific Studies</option>
					<option>Classics</option>
					<option>Comparative Literature</option>
					<option>Computer Science</option>
					<option>Economics</option>
					<option>English</option>
					<option>Feminist, Gender, and Sexuality Studies</option>
					<option>French</option>
					<option>German Studies</option>
					<option>Government</option>
					<option>History</option>
					<option>History of Art</option>
					<option>Information Science</option>
					<option>Italian</option>
					<option>Linguistics</option>
					<option>Mathematics</option>
					<option>Music</option>
					<option>Near Eastern Studies</option>
					<option>Performing and Media Arts</option>
					<option>Philosophy</option>
					<option>Physics</option>
					<option>Psychology</option>
					<option>Religious Studies</option>
					<option>Science &amp; Technology Studies</option>
					<option>Science of Earth Systems</option>
					<option>Sociology</option>
					<option>Spanish</option>
					<option>Statistics</option>
				</select>

				<?php elseif ($undergrad === TRUE && $cornell_ugrad == '3'): ?>
				<div class="centerheading"><h4>What Major in ENG?</h4></div>
				<select>
					<option>Applied and Engineering Physics</option>
					<option>Biological and Environmental Engineering</option>
					<option>Biomedical Engineering</option>
					<option>Chemical and Biomolecular Engineering</option>
					<option>Civil and Environmental Engineering</option>
					<option>Computer Science</option>
					<option>Earth and Atmospheric Sciences</option>
					<option>Electrical and Computer Engineering</option>
					<option>Engineering Management</option>
					<option>Information Science</option>
					<option>Materials Science and Engineering</option>
					<option>Sibley School of Mechanical and Aerospace Engineering</option>
					<option>Operations Research and Information Engineering</option>
					<option>Systems Engineering</option>
				</select>

				<?php elseif ($undergrad === TRUE && $cornell_ugrad == '4'): ?>
				<div class="centerheading"><h4>What Major in the Hotel School?</h4></div>
				<select>
					<option>Hotel Administration</option>
				</select>

				<?php elseif ($undergrad === TRUE && $cornell_ugrad == '5'): ?>
				<div class="centerheading"><h4>What Major in HuMec?</h4></div>
				<select>
					<option>Design and Environmental Analysis</option>
					<option>Fiber Science and Apparel Design</option>
					<option>Global and Public Health Sciences</option>
					<option>Human Biology, Health, and Society</option>
					<option>Human Development</option>
					<option>Nutritional Sciences</option>
					<option>Policy Analysis and Management</option>
				</select>

				<?php elseif ($undergrad === TRUE && $cornell_ugrad == '6'): ?>
				<div class="centerheading"><h4>What Major in ILR?</h4></div>
				<select>
					<option>Industrial and Labor Relations</option>
				</select>


				<?php else: ?>


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
    		<?php elseif ($submitno == 4): ?>
    			<label for="form-gen">
				<select name="form-gen" id="form-gen">
					<option>Male</option>
					<option>Female</option>
					<option>Other</option>
				</select>

				<label for="form-eth">Ethnicity</label>
				<select name="form-eth" id="form-eth">
					<option>White</option>
					<option>Middle Eastern</option>
					<option>Black/African-American</option>
					<option>Latino/Hispanic</option>
					<option>East Asian</option>
					<option>South Asian</option>
					<option>Pacific Islander</option>
					<option>Native American</option>
					<option>Decline To Answer</option>
				</select>

				<label for="form-rel">Religion</label>
				<select name="form-rel" id="form-rel">
					<option>Christian</option>
					<option>Jewish</option>
					<option>Muslim</option>
					<option>Hindu</option>
					<option>Buddhist</option>
					<option>Atheist/Agnostic</option>
					<option>Other</option>
				</select>

				<label for="form-music">Music</label>
				<select name="form-music" id="form-rel">
					<option>Alternative</option>
					<option>Classical</option>
					<option>Country</option>
					<option>EDM</option>
					<option>Hiphop</option>
					<option>Jazz</option>
					<option>Latin</option>
					<option>Opera</option>
				</select>

				<label for="form-sports">Sports</label>
				<select name="form-sports" id="form-sports">
					<option>Archery</option>
					<option>Badminton</option>
					<option>Baseball</option>
					<option>Basketball</option>
					<option>Bowling</option>
					<option>Climbing</option>
					<option>Cycling</option>
					<option>Dance</option>
					<option>Equestrian</option>
					<option>Fishing</option>
					<option>Football</option>
					<option>Golf</option>
					<option>Gymnastics</option>
					<option>Lacrosse</option>
					<option>Martial Arts</option>
					<option>Wrestling</option>
					<option>Skating</option>
					<option>Skiing</option>
					<option>Soccer</option>
					<option>Swimming</option>
					<option>Tennis</option>
					<option>Track</option>
					<option>None</option>
					<option>Other</option>
				</select>


				<label for="hometown">Hometown</label>
				<input type="text" id="hometown" placeholder="New York, NY">



<!-- 				
                       _   _               _____ 
                      | | (_)             |  ___|
  __ _ _   _  ___  ___| |_ _  ___  _ __   |___ \ 
 / _` | | | |/ _ \/ __| __| |/ _ \| '_ \      \ \
| (_| | |_| |  __/\__ \ |_| | (_) | | | | /\__/ /
 \__, |\__,_|\___||___/\__|_|\___/|_| |_| \____/ 
    | |                                          
    |_|                                           -->


    		<?php elseif ($submitno == 5): ?>

    			<select>
					<option>Administration</option>
					<option>Aerospace Engineering</option>
					<option>Architecture</option>
					<option>Attorney</option>
					<option>Broadcasting</option>
					<option>Chemical Engineering</option>
					<option>Civil Engineering</option>
					<option>Clergy</option>
					<option>Coaching</option>
					<option>Computer Science</option>
					<option>Corporate</option>
					<option>Culinary Arts</option>
					<option>Design</option>
					<option>Diet</option>
					<option>Doctor</option>
					<option>Electrical Engineering</option>
					<option>Emergency Care</option>
					<option>Energy</option>
					<option>Entrepreneurship</option>
					<option>Environmental Science</option>
					<option>Fashion</option>
					<option>Finance</option>
					<option>Fine Art</option>
					<option>Foreign Service</option>
					<option>Forestry / Wilderness</option>
					<option>Geography</option>
					<option>Government / Politics</option>
					<option>Hotel Management</option>
					<option>Human Resources</option>
					<option>Information Science</option>
					<option>International Trade</option>
					<option>Journalism</option>
					<option>Judge</option>
					<option>Lab Research</option>
					<option>Language Translation</option>
					<option>Legal</option>
					<option>Management Counseling</option>
					<option>Manufacturing</option>
					<option>Marketing / Advertising</option>
					<option>Mechanical Engineering</option>
					<option>Music</option>
					<option>Nonprofit</option>
					<option>Nursing</option>
					<option>Other</option>
					<option>Parks / Recreation</option>
					<option>Performing Arts</option>
					<option>Pharmacy</option>
					<option>Photography</option>
					<option>Product Design</option>
					<option>Psych / Counseling</option>
					<option>Public Relations</option>
					<option>Public Service</option>
					<option>Publishing</option>
					<option>Real Estate</option>
					<option>Research</option>
					<option>Social Work</option>
					<option>Sports</option>
					<option>Statistics / Math</option>
					<option>Teaching K-12</option>
					<option>University / College</option>
					<option>Vet</option>
    			</select>

    			<?php if ($undergrad === TRUE): ?>
    			<div class="centerheading"><h4>Interested in Research?</h4></div>
    			<select>
    				<option>Yes</option>
    				<option>No</option>
    			</select>


    			<?php else: ?>
    			<div class="centerheading"><h4>Are you doing Research?</h4></div>
    			<select>
    				<option>Yes</option>
    				<option>No</option>
    			</select>

    			<div class="centerheading"><h4>If doing Research, do you want Undergrads involved?</h4></div>
				<select>
    				<option>Yes</option>
    				<option>No</option>
    			</select>



    			<?php endif; ?>




<!-- 				<label for="form-degree">What Degree?</label>
				<select name="form-degree" id="form-degree">
					<option value="Bachelors">Bachelors</option>
					<option value="Masters">Master's</option>
					<option value="Doctorate">Doctorate</option>
				</select> -->

				<!-- <label for="form-tech">If you went to Cornell's NYC Tech Campus</label>
				










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
