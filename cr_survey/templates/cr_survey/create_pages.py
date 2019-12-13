import shutil

# this will copy q_test_1.html to n_pages other pages
# use with care

# Kevin O/'Neill

n_pages=16

for x in range(1,16):
    shutil.copy("q_test_1.html","Page_"+str(x)+".html")

