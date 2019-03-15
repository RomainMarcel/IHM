<!doctype html>
<html lang="fr">
<head class="container-fluid">
    <meta charset="utf-8>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
   <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
   <title>GAMES</title>




		<div class="row align-items-center justify-content-center">
            <div class="col-12 col-lg-8 text-center text-lg-left">

    <h1>PUISSANCE 4 VS MORPION</h1>


        <div class="row align-items-center justify-content-center">
            <div class="col-12 col-lg text-center text-lg-left">

<a href="#" class="btn btn-primary btn-lg active" role="button" aria-pressed="true">INDEX</a>
<a href="#" class="btn btn-primary btn-lg active" role="button" aria-pressed="true">GAME SERVER</a>
<a href="#" class="btn btn-primary btn-lg active" role="button" aria-pressed="true">LAST GAME RESULT</a>
<a href="#" class="btn btn-primary btn-lg active" role="button" aria-pressed="true">STATS PER DAY</a>
<a href="#" class="btn btn-primary btn-lg active" role="button" aria-pressed="true">STATS PER MATCH</a>
<a href="#" class="btn btn-primary btn-lg active" role="button" aria-pressed="true">CONFIGURATION</a>

</div>
</div>
</head>
<body>

            <ul>
            % for i in data_list:
                <li><p>L'adresse IP est :<p>{{i.adress_ip}}</li>
                <li><p>Le nom du serveur est :</p>{{i.nom_serveur}}</li>
                <li><p>Le jeu utilisé est :</p>{{i.game}}</li>
                <br>
            % end
            </ul>

</header>


<footer>
</footer>
</body>
</html>