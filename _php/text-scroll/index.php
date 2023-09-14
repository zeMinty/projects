<!DOCTYPE html>
<html>

<head>
	<title>Test Php</title>
	<link href='main.css' rel='stylesheet' type='text/css' />
</head>

<body>
	<div id="section1">
		<p class="clickable">
			<a href="#section2"> Go to second section </a>
		</p>
		<?php for ($i = 0; $i < 50; $i++) : ?>
			<p class="filler">line: <?= $i ?></p>
		<?php endfor; ?>
	</div>
	<div id="section2">
		<p class="clickable">
			<a href="#section1"> Go to first section </a>
		</p>
		<?php for ($i = 50; $i < 100; $i++) : ?>
			<p class="filler">line: <?= $i ?></p>
		<?php endfor; ?>
	</div>
</body>

</html>