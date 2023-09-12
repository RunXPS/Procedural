<!DOCTYPE html>
<!-- saved from url=(0080)https://faculty.ncssm.edu/~morrison/currentClasses/4240/specs/chapter1/keywords/ -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
 
<link rel="stylesheet" href="./Keywords2_files/pageContent0220.css">
<link rel="stylesheet" href="./Keywords2_files/boxes.css">
<link rel="stylesheet" href="./Keywords2_files/gridLayout0820.css">
<link rel="stylesheet" href="./Keywords2_files/menus.css">
<link href="./Keywords2_files/css" rel="stylesheet">
<link rel="shortcut icon" href="https://faculty.ncssm.edu/~morrison/CSS/rhino.ico">
<link rel="stylesheet" href="./Keywords2_files/sunburst.css">
<script src="./Keywords2_files/highlight.min.js.download"></script>
<script>hljs.initHighlightingOnLoad();</script>
<style>
table
{
    width:80%;
}
</style>
<!--
Uncomment for mathJax
<script type="text/javascript"
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
-->
<!--
Uncomment for JQuery
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js"></script>
-->

        <title>medium_functions.py</title>

</head>
<body data-new-gr-c-s-check-loaded="14.1028.0" data-gr-ext-installed="">
<header>
<h2>medium_functions.py</h2>
<div id="menu">
<ul>
   <li class="active has-sub"><a href="https://faculty.ncssm.edu/~morrison/currentClasses"><span>Classes</span></a>
        <ul>
            <li><a href="https://faculty.ncssm.edu/~morrison/big6.php">The Big 6</a></li>
            <!--<li><a href = "/~morrison/JTerm2021">JTerm 20201</a></li>-->
            <li><a href="https://faculty.ncssm.edu/~morrison/currentClasses/4020">CSC 4020</a></li>
            <li><a href="https://faculty.ncssm.edu/~morrison/currentClasses/4240">CSC 4240</a></li>
            <li><a href="https://www.youtube.com/channel/UCMxP_bP8whMGN63IpvGFPTQ/">My YouTube Channel</a></li>
            <li><a href="https://faculty.ncssm.edu/~morrison/youTubeChannel"> YouTube Files</a></li>
        </ul>
   </li>
   <li class="active has-sub"><a href="https://faculty.ncssm.edu/~morrison/resources"><span>resources</span></a>
        <ul>
            <li><a href="https://faculty.ncssm.edu/~morrison/educators"><span>Resources for Educators</span></a></li>
            <li><a href="https://faculty.ncssm.edu/~morrison/resources/fileSystem"><span>File System Organization</span></a></li>
            <li><a href="https://faculty.ncssm.edu/~morrison/resources/python"><span>Python</span></a></li>
            <li><a href="https://faculty.ncssm.edu/~morrison/resources/java"><span>Java</span></a></li>
            <li><a href="https://faculty.ncssm.edu/~morrison/resources/UNIXResources"><span>UNIX</span></a></li>
            <li><a href="https://github.com/ncmathsadist"><span>Morrison's GitHub Repository</span></a></li>
            <li><a href="https://faculty.ncssm.edu/~morrison/resources/googleCalendar/"><span>Using Google Calendar</span></a></li>

       </ul>
   </li>
   <li class="active has-sub"><a href="https://faculty.ncssm.edu/~morrison/math"><span>Math</span></a>
      <ul>
            <li><a href="https://math.stackexchange.com/users/4154/ncmathsadist"><span>Stack Exchange Profile</span></a></li>
      </ul>
   </li>
   <li class="active has-sub"><a href="https://faculty.ncssm.edu/~morrison/school"><span>School</span></a>
        <ul>
            <li><a href="https://faculty.ncssm.edu/~morrison/school/college"> <span>College Matters</span></a></li>
    </ul>
   </li>
   <li class="active has-sub"><a href="https://faculty.ncssm.edu/~morrison/general"><span>Contact/Schedule</span></a>
        <ul>
            <li><a href="https://faculty.ncssm.edu/~morrison/general/schedule.php"><span>Schedule</span></a></li>
            <li><a href="https://faculty.ncssm.edu/~morrison/general/contact.php"><span>Contact</span></a></li>
            <li><a href="https://calendar.google.com/calendar/embed?src=morrison%40ncssm.edu&amp;ctz=America%2FNew_York"><span>Google Calender</span></a></li>
            <li class="last"><a href="https://faculty.ncssm.edu/~morrison/general/parents.php"><span>Parents FAQ</span></a></li>
        </ul>
   </li>
   <li class="active has-sub"><a href="https://faculty.ncssm.edu/~morrison/personal"><span>Personal</span></a>
      <ul>
         <li class="has-sub"><a href="https://faculty.ncssm.edu/~morrison/personal/crackerBarrel/"><span>The Cracker Barrel</span></a>
            <ul>
               <li><a href="https://faculty.ncssm.edu/~morrison/personal/crackerBarrel/facebook.php"><span>Using Facebook</span></a></li>
               <li><a href="https://faculty.ncssm.edu/~morrison/personal/crackerBarrel/mathStudyGuide.php"><span>Math Study Guide</span></a></li>
               <li><a href="https://faculty.ncssm.edu/~morrison/personal/crackerBarrel/plants.php"><span>Plants Page</span></a></li>
               <li><a href="https://faculty.ncssm.edu/~morrison/personal/crackerBarrel/computingHistory.php"><span>Personal Computing History</span></a></li>
               <li><a href="https://faculty.ncssm.edu/~morrison/personal/crackerBarrel/eats.php"><span>The Eats Page</span></a></li>
               <li class="last"><a href="https://www.yelp.com/user_details?userid=-Fm05tmJz_10qOkL6JAsmw"><span>Yelp Profile</span></a></li>
            </ul>
         </li>
         <li><a href="https://faculty.ncssm.edu/~morrison/personal/resume.php"><span>Resume</span></a></li>
      </ul>
   </li>
</ul>
</div>
</header>

<nav>

<h2>Navigation</h2>

<hr>
<h3>Directories</h3>

<ul><li><a href="https://faculty.ncssm.edu/~morrison/currentClasses/4240/specs/chapter1/">Parent Directory</a></li></ul><hr><h3>Files</h3><ul><li><a href="https://faculty.ncssm.edu/~morrison/currentClasses/4240/specs/chapter1/keywords/keywords.py">keywords.py</a></li>
<li><a href="https://faculty.ncssm.edu/~morrison/currentClasses/4240/specs/chapter1/keywords/keywords.py.out">keywords.py.out</a></li>
<li><a href="https://faculty.ncssm.edu/~morrison/currentClasses/4240/specs/chapter1/keywords/run_tests.py">run_tests.py</a></li>
</ul><hr><h3>Other Places</h3><ul><li><a href="https://faculty.ncssm.edu/~morrison/currentClasses/4240/specs/chapter1/keywords/index.php">Back to Index Page</a></li><li><a href="https://faculty.ncssm.edu/~morrison/currentClasses">Current Courses Page</a></li><li><a href="https://faculty.ncssm.edu/~morrison">Morrison's Main Page</a></li></ul>

</nav>

<main>
    <p>Download both files at the left and put them in the
    same directory (smart idea: make a directory for this assignment)
    Save time by right-clicking on the links and using Save Link As.
    </p>
    
    <p>You will import the testing apparatus into your code.  </p>

<p>Here is my test module</p>

<pre><code class="hljs python">
<span class="hljs-keyword">from</span> math <span class="hljs-keyword">import</span> log, e, sin, cos
<span class="hljs-keyword">from</span> run_tests <span class="hljs-keyword">import</span> close_enough, run_test, run_test_float
<span class="hljs-comment">## you can now use log(x) for the natural log of x.</span>
<span class="hljs-comment">## You can only use the imported functions that I specify.</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">greet</span>(<span class="hljs-params">name</span>):</span>
    <span class="hljs-string">"""prec:  name is a keyword argument with default value "Stranger"
    postc: returns the string Hello, name!"""</span>  
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello"</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">log_base</span>(<span class="hljs-params">x, b</span>):</span>
    <span class="hljs-string">"""prec:  x &gt; 0 and b &gt; 0 is a keyword argument
    postc: use the change-of-base formula to compute 
    the logarithm of x with base b.  The default is that
    the natural log of x is returned."""</span>
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">truncate</span>(<span class="hljs-params">s, n</span>):</span>
    <span class="hljs-string">"""prec:  s is a string, n is a nonnegative integer
    and a keyword argument.  if len(x) &gt; s return s; otherwise
    truncate at n.  By default, n = 3."""</span>
    <span class="hljs-keyword">return</span> <span class="hljs-string">""</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">protean_sin</span>(<span class="hljs-params">x, radians</span>):</span>
    <span class="hljs-string">"""prec: x is a number, radians is a boolean and a
    keyword argument.  
    postc: returns sin(x) using radians if radians is True
    and sin(x) in degrees if radians is false.
    The default is True"""</span>
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">protean_asin</span>(<span class="hljs-params">x, radians</span>):</span>
    <span class="hljs-string">"""prec: x is a number, -1 &lt;= x &lt;= 1.
    radians is a keyword argument.  
    postc: returns sin(x) using radians if radians is True
    and arcsin(x) in degrees if radians is false.
    The default is True."""</span>
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">main</span>():</span>

</code></pre>

<p>Here is the shell code.  It runs out of the box.</p>

<pre><code class="hljs python">
<span class="hljs-keyword">from</span> math <span class="hljs-keyword">import</span> log, e, sin, cos
<span class="hljs-comment">## you can now use log(x) for the natural log of x.</span>
<span class="hljs-comment">## You can only use the imported functions that I specify.</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">greet</span>(<span class="hljs-params">name</span>):</span>
    <span class="hljs-string">"""prec:  name is a keyword argument with default value "Stranger"
    postc: returns the string Hello, name!"""</span>  
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello"</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">log_base</span>(<span class="hljs-params">x, b</span>):</span>
    <span class="hljs-string">"""prec:  x &gt; 0 and b &gt; 0 is a keyword argument
    postc: use the change-of-base formula to compute 
    the logarithm of x with base b.  The default is that
    the natural log of x is returned."""</span>
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">truncate</span>(<span class="hljs-params">s, n</span>):</span>
    <span class="hljs-string">"""prec:  s is a string, n is a nonnegative integer
    and a keyword argument.  if len(x) &gt; s return s; otherwise
    truncate at n.  By default, n = 3."""</span>
        <span class="hljs-keyword">return</span> <span class="hljs-string">""</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">protean_sin</span>(<span class="hljs-params">x, radians</span>):</span>
    <span class="hljs-string">"""prec: x is a number, radians is a boolean and a
    keyword argument.  
    postc: returns sin(x) using radians if radians is True
    and sin(x) in degrees if radians is false.
    The default is True"""</span>
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">protean_asin</span>(<span class="hljs-params">x, radians</span>):</span>
    <span class="hljs-string">"""prec: x is a number, -1 &lt;= x &lt;= 1.
    radians is a keyword argument.  
    postc: returns sin(x) using radians if radians is True
    and arcsin(x) in degrees if radians is false.
    The default is True."""</span>
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>
</code></pre>


</main>


</body><grammarly-desktop-integration data-grammarly-shadow-root="true"></grammarly-desktop-integration></html>