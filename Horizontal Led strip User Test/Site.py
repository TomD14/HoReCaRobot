def WebPage():
    html = """
        <html>
        <head>
        <title>ESP Web Server</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="icon" href="data:,">
        <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
            h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}
            .button{display: inline-block; background-color: #e7bd3b; border: none; 
            border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
            .button2{background-color: #4286f4;}
            .button3{background-color: #10E109;}
        </style>
        </head>
        <body> <h1>Scenario 1</h1> 
            <p><a href="/?LeftScenario1"><button class="button">Left Scenario 1</button></a>
            <a href="/?RightScenario1"><button class="button">Right Scenario 1</button></a></p>
            <p><a href="/?DriveScenario1"><button class="button">Drive Scenario 1</button></a>
            <a href="/?BrakeScenario1"><button class="button">Brake Scenario 1</button></a></p>
            <p><a href="/?ClosingScenario1"><button class="button">Closing Scenario 1</button></a></p>
            
            <p></p>
            <h1>Scenario 2</h1> 
            <p><a href="/?LeftScenario2"><button class="button">Left Scenario 2</button></a>
            <a href="/?RightScenario2"><button class="button">Right Scenario 2</button></a></p>
            <p><a href="/?DriveScenario2"><button class="button">Drive Scenario 2</button></a>
            <a href="/?BrakeScenario2"><button class="button">Brake Scenario 2</button></a></p>
            <p><a href="/?ClosingScenario2"><button class="button">Closing Scenario 2</button></a></p>
            
            <p></p>
            <h1>Scenario 3</h1>
            <p><a href="/?LeftScenario3"><button class="button">Left Scenario 3</button></a>
            <a href="/?RightScenario3"><button class="button">Right Scenario 3</button></a></p>
            <p><a href="/?DriveScenario3"><button class="button">Drive Scenario 3</button></a>
            <a href="/?BrakeScenario3"><button class="button">Brake Scenario 3</button></a></p>
            <p><a href="/?ClosingScenario3"><button class="button">Closing Scenario 3</button></a></p>
            
            <p></p>
            <h1>Scenario 4</h1>
            <p><a href="/?LeftScenario4"><button class="button">Left Scenario 4</button></a>
            <a href="/?RightScenario4"><button class="button">Right Scenario 4</button></a></p>
            <p><a href="/?DriveScenario3"><button class="button">Drive Scenario 4 (uses Scenario 3)</button></a>
            <a href="/?BrakeScenario3"><button class="button">Brake Scenario 4 (uses Scenario  3)</button></a></p>
            <p><a href="/?ClosingScenario4"><button class="button">Closing Scenario 4</button></a></p>
            
            <p></p>
            <h1>Scenario 5</h1>
            <p><a href="/?LeftScenario5"><button class="button">Left Scenario 5</button></a>
            <a href="/?RightScenario5"><button class="button">Right Scenario 5</button></a></p>
            <p><a href="/?DriveScenario2"><button class="button">Drive Scenario 5 (uses Scenario 2)</button></a>
            <a href="/?BrakeScenario2"><button class="button">Brake Scenario 5 (uses Scenario 2)</button></a></p>
            <p><a href="/?ClosingScenario4"><button class="button">Closing Scenario 5 (uses Scenario 4)</button></a></p>
            
            <p></p>
            <p></p>

            <h1>General buttons</h1>
            <p><a href="/?NeoOffSides"><button class="button button2">OFF Sides</button></a></p>
            <p><a href="/?NeoOffColl"><button class="button button2">OFF Collision</button></a></p>
        </body>
        </html>
        """
    return html