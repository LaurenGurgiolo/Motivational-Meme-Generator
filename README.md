This project has two functions: 1) Generating a random meme with an image, quote, and author from selected databases of existential philosophers, philosophers throughout history, and images of grave sites.  2) Create a custom meme with user input. User input includes a URL to an image and text for the quote and author. If any of the inputs are not defined a random selection will be made instead.

Please view the requirements.txt for all libraries and updates needed to run the program. Please make sure to update pip ('python -m pip install --upgrade pip') before loading requirements.txt and install 
"sudo apt-get install -y xpdf" in the terminal as well.

Meme.py can be run from the terminal and will take the optional arguments:  -body -path -author. Run python3 meme.py for a random meme or define the arguments for a custom meme.

App.py takes in user input from HTML. Run “export FLASK_APP=app.py flask run --host 0.0.0.0 --port 3000 –reload” in the terminal.  The following webpage will be active: https://yzqecjg54u.prod.udacity-student-workspaces.com/.  You can then select to generate a random meme or a custom meme.

Package includes a QuoteEngine module in a MemeEngine module. The QuoteEngine module takes in as input user defined quotes and authors or selects quotes and authors randomly from multiple databases. The module can process multiple file types into the database including JSON, PDF, CSV, TXT, and DOCX.  The module either creates a quote class object with the users input or selects a object at random.  If the body of the quote is not defined a random one will be selected.

The MemeEngine module accepts a URL from the user or selects a random image from a database of JPEG grave sites. The module resizes the image and prints the selected quote object on the image. The module returns a completed meme either to HTML or file.

