<form action='/configuration' method='post'>
    adresse_ip :<input type="text" name="serveur">
    nom du serveur : <input type="text" name="nom">
    Jeux : <input type="text" name="jeux">
    max player : <input type="number" name="max">
    max coin : <input type="number" name="coin">
    Victory : <input type="number" name="victory">
    Level : <input type="number" name="level" value="1" max="5">
    Player 1 color : <select name="player1">
                    <option>Bleu</option>
                    <option>Vert</option>
                    <option>Rouge</option>
                    </select>
    Player 2 color : <select name="player2">
                    <option>Bleu</option>
                    <option>Vert</option>
                    <option>Rouge</option>
                    </select>
    <input type="reset">
    <input type="submit">

</form>