
import React from 'react'
import Rotate from './Rotate'

const Home = () => {
  

    return (
        
        <html lang="en">
          <head>
            <meta charset="UTF-8" />
            <meta http-equiv="X-UA-Compatible" content="IE=edge" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <link rel="stylesheet" href="styles.css" />
            <title>SOBHAN | Sobhan Jahanmard</title>
            <link
              rel="icon"
              href="https://img.icons8.com/ios-filled/50/000000/cloud-arrow-left.png"
            />
            <link
              rel="stylesheet"
              href="https://use.fontawesome.com/releases/v5.15.3/css/all.css"
              integrity="sha384-SZXxX4whJ79/gErwcOYf+zWLeJdY/qpuqC4cAa9rOGUstPomtqpuNWT9wdPEn2fk"
              crossorigin="anonymous"
            />
          </head>
          <body>
            <div class="navbar">
              <div class="container flex">
                <h1 class="logo"><i class="fas fa-gem"></i>SOBHAN</h1>
                <ul>
                  <li><a href="/">Home</a></li>
                  <li><a href="Comments.js">Comments</a></li>
                </ul>
              </div>
            </div>
            <Rotate/>
        
        
            <div class="cards">
              <div class="container">
                <div class="card">
                  <h4>Node.js</h4>
                  <img src={require("./images/logos/node.png").default} alt="" />
                </div>
                <div class="card">
                  <h4>Python</h4>
                  <img src={require("./images/logos/python.png").default} alt="" />
                </div>
                <div class="card">
                  <h4>C#</h4>
                  <img src={require("./images/logos/csharp.png").default} alt="" />
                </div>
                <div class="card">
                  <h4>Ruby</h4>
                  <img src={require("./images/logos/ruby.png").default} alt="" />
                </div>
                <div class="card">
                  <h4>PHP</h4>
                  <img src={require("./images/logos/php.png").default} alt="" />
                </div>
                <div class="card">
                  <h4>Scala</h4>
                  <img src={require("./images/logos/scala.png").default} alt="" />
                </div>
                <div class="card">
                  <h4>Clojure</h4>
                  <img src={require("./images/logos/clojure.png").default} alt="" />
                </div>
              </div>
            </div>
            <div class="footer">
              <div class="container">
                <div class="copy">
                  <h1>Sobhan</h1>
                  <h6>Copyright &copy; 2021</h6>
                </div>
                <div class="icon">
                  <a href="https://www.instagram.com/"
                    ><i class="fab fa-instagram fa-2x"></i
                  ></a>
                  <a href="https://www.instagram.com/"
                    ><i class="fab fa-github fa-2x"></i
                  ></a>
                  <a href="https://www.instagram.com/"
                    ><i class="fab fa-facebook fa-2x"></i
                  ></a>
                </div>
              </div>
            </div>
          
          </body>
          
          
        </html>  
         
    );

} 
export default Home

