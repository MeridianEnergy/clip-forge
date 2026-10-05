from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>

<head>

<title>CLIP⚔FORGE | Esports Network</title>

<style>

* {
    box-sizing: border-box;
}


body {
    margin: 0;
    background: #080b12;
    color: white;
    font-family: Arial, Helvetica, sans-serif;
}


/* Navigation */

nav {
    background: #111827;
    padding: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}


.logo {
    font-size: 30px;
    font-weight: bold;
    color: #00eaff;
}


.logo span {
    color: white;
}


nav a {
    color: white;
    text-decoration: none;
    margin-left: 25px;
}


nav a:hover {
    color: #00eaff;
}


/* Hero */

.hero {

    text-align: center;
    padding: 90px 20px;

}


.hero h1 {

    font-size: 70px;
    margin-bottom: 10px;

}


.hero h1 span {

    color: #00eaff;

}


.hero h2 {

    font-size: 30px;
    color: #00ff99;

}


.hero p {

    font-size: 20px;
    color: #cccccc;
    max-width: 700px;
    margin: auto;

}



/* Buttons */

.button {

    display: inline-block;
    margin: 30px 10px;
    padding: 16px 35px;
    background: #00eaff;
    color: black;
    text-decoration: none;
    border-radius: 8px;
    font-weight: bold;

}


.button:hover {

    background: #00ff99;

}



/* Cards */


.section {

    padding: 40px;

}


.cards {

    display: flex;
    justify-content: center;
    gap: 25px;
    flex-wrap: wrap;

}


.card {

    background: #141a24;
    width: 300px;
    padding: 30px;
    border-radius: 15px;
    border: 1px solid #263244;

}


.card h3 {

    color: #00eaff;

}



/* Partnership */

.partner {

    text-align:center;
    padding:50px;
    background:#111827;

}


.partner h2 {

    color:#00ff99;

}


/* Footer */


footer {

    text-align:center;
    padding:25px;
    color:#888;

}


</style>


</head>


<body>



<nav>

<div class="logo">
⚔ CLIP<span>-FORGE</span>
</div>


<div>

<a href="#">Home</a>
<a href="#">Players</a>
<a href="#">Teams</a>
<a href="#">Tournaments</a>
<a href="#">Login</a>

</div>


</nav>




<section class="hero">


<h1>
⚔ CLIP<span>-FORGE</span>
</h1>


<h2>
Forge Your Esports Legacy
</h2>


<p>
The competitive gaming network connecting players,
teams and esports organisations.
Find your squad. Showcase your skills. Rise together.
</p>



<a class="button" href="#">
Create Player Profile
</a>


<a class="button" href="#">
Find A Team
</a>


</section>





<section class="section">


<div class="cards">


<div class="card">

<h3>
⚔ Find Your Squad
</h3>

<p>
Connect with competitive players,
discover teams and build your roster.
</p>

</div>




<div class="card">

<h3>
🔥 Showcase Your Skills
</h3>

<p>
Create your esports identity,
display achievements and highlight clips.
</p>

</div>




<div class="card">

<h3>
🏆 Compete
</h3>

<p>
Follow tournaments, rankings and
your journey through esports.
</p>

</div>



</div>


</section>






<section class="partner">


<h2>
TEF eSports Africa × Nexus Valor
</h2>


<p>
Building the future of African esports talent.
</p>


<p>
Clip-Forge is owned by Nexus Valor
and developed as a competitive esports platform.
</p>


</section>






<footer>

© 2026 Clip-Forge  
<br>
Forge Your Esports Legacy

</footer>



</body>

</html>

"""


if __name__ == "__main__":
    app.run(debug=True)