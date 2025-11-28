app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nandani Kumari - Portfolio</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: "Poppins", sans-serif;
        }

        body {
            background: #f5f5f5;
            color: #333;
        }

        /* NAVBAR */
        nav {
            width: 100%;
            background: #1a1a1a;
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 40px;
            position: fixed;
            top: 0;
            z-index: 100;
        }

        nav ul {
            list-style: none;
            display: flex;
        }

        nav ul li {
            margin-left: 25px;
        }

        nav ul li a {
            text-decoration: none;
            color: white;
            font-size: 16px;
            transition: 0.3s;
        }

        nav ul li a:hover {
            color: #00aaff;
        }

        .logo {
            font-size: 22px;
            font-weight: 600;
        }

        /* HOME SECTION */
        .home {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 120px 60px;
            height: 100vh;
            background: linear-gradient(to right, #eef7ff, #ffffff);
        }

        .home .text h1 {
            font-size: 45px;
            margin-bottom: 10px;
        }

        .home .text h1 span {
            color: #0077ff;
            font-weight: bold;
        }

        .home .text p {
            font-size: 18px;
            margin-bottom: 20px;
        }

        .btn {
            padding: 10px 20px;
            background: #0077ff;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            transition: 0.3s;
        }

        .btn:hover {
            background: #005fcc;
        }

        /* IMAGE PLACEHOLDER */
        .image-box {
            width: 350px;
            height: 350px;
            background: white;
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        }

        .img-placeholder {
            width: 80%;
            height: 80%;
            border: 2px dashed #0077ff;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #0077ff;
            font-weight: bold;
        }

        /* ABOUT SECTION */
        .about {
            padding: 80px 60px;
            background: #ffffff;
            text-align: center;
        }

        .about h2 {
            font-size: 32px;
            margin-bottom: 20px;
            color: #0077ff;
        }

        .about p {
            font-size: 18px;
            width: 80%;
            margin: auto;
        }

        .skills {
            margin-top: 20px;
        }

        .skills span {
            display: inline-block;
            background: #0077ff;
            color: white;
            padding: 8px 15px;
            border-radius: 8px;
            margin: 5px;
        }

        /* PROJECT SECTION */
        .projects {
            padding: 80px 60px;
            text-align: center;
            background: #eef7ff;
        }

        .projects h2 {
            color: #0077ff;
            margin-bottom: 10px;
        }

        /* CONTACT SECTION */
        .contact {
            padding: 80px 60px;
            text-align: center;
        }

        .contact h2 {
            color: #0077ff;
            margin-bottom: 10px;
        }

        /* FOOTER */
        footer {
            text-align: center;
            padding: 15px;
            background: #1a1a1a;
            color: white;
            margin-top: 30px;
        }
    </style>
</head>
<body>

    <!-- Navbar -->
    <nav>
        <div class="logo">Portfolio</div>
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#projects">Projects</a></li>
            <li><a href="#contact">Contact Us</a></li>
        </ul>
    </nav>

    <!-- Home Section -->
    <section id="home" class="home">
        <div class="text">
            <h1>Hello, I'm <span>Nandani Kumari</span></h1>
            <p>B.Tech 3rd Semester Student • AI & ML</p>
            <a href="#about" class="btn">Know More</a>
        </div>

        <div class="image-box">
            <div class="img-placeholder">Your Image Here</div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
        <h2>About Me</h2>
        <p>
            I am <strong>Nandani Kumari</strong>, a dedicated B.Tech student in the 3rd semester 
            specializing in <strong>Artificial Intelligence and Machine Learning</strong>.  
            I enjoy learning new technologies and building creative projects.  
            My technical skills include:
        </p>

        <div class="skills">
            <span>HTML</span>
            <span>CSS</span>
            <span>Python</span>
            <span>VS Code</span>
            <span>Basic Technical Skills</span>
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="projects">
        <h2>Projects</h2>
        <p>Coming Soon...</p>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <h2>Contact Me</h2>
        <p>Email: yourmail@example.com</p>
        <p>LinkedIn / GitHub (Add your links)</p>
    </section>

    <footer>
        © 2025 Nandani Kumari · All Rights Reserved
    </footer>

</body>
</html>

    """

    
if __name__ =='__main__':
    app.run()
