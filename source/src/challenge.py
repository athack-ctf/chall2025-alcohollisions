from flask import Flask
from flask import request
from flask import render_template 
import hashlib
  
app = Flask(__name__)

hashes = {
    "christmas": {
        "md5": "eb4a16b280e7cdd3c57a94efa7816b34",
        "sha256": "680d05711493a05f3a2d31a4a01dd021cc0ff8f33d188be3bc5f0a0d06129144"
    },
    "easter": {
        "md5": "362154565c523fdf1225b8fd70671bf0",
        "sha256": "dfa8d17ef706c03f3c9351d030cb58e361384d1722e7d5172a2ddb0a3f1af7ce"
    },
     "halloween": {
		"md5": "ee9893e7850e46796b79b778e58f394d",
        "sha256": "e5f0ab300eb102f90a91f6ba8a8e900721ebc5a6e4fac0562c05f42487b0284c"
    }
}

md5hashes = (
    hashes["christmas"]["md5"],
    hashes["easter"]["md5"],
    hashes["halloween"]["md5"],
)

sha256hashes = (
    hashes["christmas"]["sha256"],
    hashes["easter"]["sha256"],
    hashes["halloween"]["sha256"],
)

@app.route('/upload', methods=['POST'])
def upload_file():
    file_contents = request.files['collision_image'].read()
    if len(file_contents) == 0:
        return render_template('home.html', message="Make sure to upload a file first...")

    md5hash = hashlib.md5(file_contents).hexdigest()
    sha256hash = hashlib.sha256(file_contents).hexdigest()

    if md5hash not in md5hashes:
        return render_template('home.html', message=f"The MD5 hash of this image is not the same as that of any of the wine labels")
        
    if sha256hash in sha256hashes:
        return render_template('home.html', message=f"The file you upload must have a different sha256 hash, try again!")

    return render_template('home.html', message=r"ATHACKCTF{y0uar3aSharpStud3nt}")


@app.route("/") 
def hello(): 
    message = "Hello, Hacker"
    return render_template('home.html',  
                           message=message) 
   