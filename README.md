# ghpages
Blog Source Code

!pip install pelican markdown

To build and run development code
---------------------------------
make html && make serve
goto  http://localhost:8000

To push to production
---------------------
make publish

cd output

git add .

git commit -m "misc content update"

git push -u origin master

To push content to github source control
----------------------------------------
cd ../ghpages

git add .

git commit -m "misc commit"

git push -u origin master


