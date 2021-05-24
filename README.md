Contained within this branch are my own (commented) implementations of the protocols SIDH and SITH in Sage 9.0 - "SIDH.ipynb" and "SITH.ipynb", and an aplet demonstrating a random instance of these protocols - "form.py".


Instructions on launching the aplet:

- Download Sage 9.0 or higher : https://www.sagemath.org/download.html
 
- Install bottle package - Enter "sage --pip3 install bottle" in Sage shell

- Download files "SIDH.py", "SITH.py" and "form.py" and place them all into one directory

- Find the path of "form.py" - eg. C:/Users/User/Folder - and open the file "form.py" in Sage shell - "sage form.py"

- Open //localhost:port from Sage shell


Instructions on using the aplet:

- Choose a protocol - SIDH or SITH

- Enter lA, eA, lB, eB such that p = lA^eA * lB^eB - 1 is a prime with p = -1 mod 4 - eg. lA = 2, eA = 8, lB = 3, eB = 5

- Click on [SIDH] or [SITH]

- And finally, enjoy!
