# quantum-multiverse-bifurcator
Simple flask app to pull quantum coin flips from https://qrng.anu.edu.au and convert them to major life decisions.  Enjoy :)

## Running Locally

Make sure you have Python installed

```sh
$ git clone https://github.com/lots-of-things/quantum-multiverse-bifurcator.git # or clone your own fork
$ cd quantum-multiverse-bifurcator
$ pip install -r requirements.txt
$ python app.py
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

### Cache measurements
there is an added method in main.py called `_write_random_to_file`, which banks 
