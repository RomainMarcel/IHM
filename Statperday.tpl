<h1>Stat per Day</h1>
<ul>
% for item in resultliste:
    <li>{{item.date}}</li>
    <li>{{item.machine_name}}</li>
    <li>{{item.nombre_partie}}</li>
    <li>{{item.duree_moy_partie}}</li>
    <li>{{item.joueur1_win}}</li>
    <li>{{item.joueur2_win}}</li>
    <li>{{item.egalite}}</li>
%end
</ul>