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

<p> Choix de la date ou de la machine</p>



</body>
</html>


