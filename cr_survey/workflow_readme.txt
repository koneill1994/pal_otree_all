Careless responding workflow

changes to question items, or to variables or functions based on question items and measures,
should be the r-script, careless_respond.R

changes to the webpage should be made in q_test_1.html
and then create_pages.py should be run to copy those changes to the other pages

Order of changes goes like this:
Make changes to csv read in by careless_respond.R
copy from cr_for_otree.txt, the output of careless_respond.R, 
    into the indicated python file, either models.py or pages.py
