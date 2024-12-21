import shutil
src = "D:/aaja lele/text.txt"
dst = "E:/rakhna hay mere dil me"

shutil.copy(src, dst)

#copy with meta data
src2 = "D:/aaja lele/meta_ve_lele.txt"
dst2 = "E:/rakhna hay mere dil me"
shutil.copy2(src2, dst2)