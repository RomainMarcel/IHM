<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>StatPerMatch</title>
</head>

<body>

<ul>
% for item in results_list:
    <li>{{item.machine_name}}</li>
    <li>{{item.start_game}}</li>
    <li>{{item.duree}}</li>
    <li>{{item.winner}}</li>
    % end
</ul>

<!--% if machine_name = "A"-->
<!--<a href="http://127.0.0.1:8080/Statpermatch/A">Machine A</a> <br>-->
<!--<a href="http://127.0.0.1:8080/Statpermatch/B">Machine B</a> <br>-->
<!--<a href="http://127.0.0.1:8080/Statpermatch/Date">Date</a> <br>-->

</body>

</html>