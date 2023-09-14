<DOCTYPE html>
<html>
<head>
    <title>PHP Test</title>
    <link rel="icon" href="favicon.ico" type="image/x-icon">
    <link type="text/css" rel="stylesheet" href="main.css">
</head>
<body>
    <?php for ($i=0; $i<=10; $i++): ?>
        <p id="row_<? echo $i ?>" class="row">Here some text in row <? echo $i ?></p>
    <?php endfor; ?>
    <script src="main.js"></script>
</body>
</html>