# seek() and tell()

# seek(offset, whence) - change stream position and return the new absolute position
# tell() - return the current position  

# SEEK_SET - beginning of the file
# SEEK_CUR - current position
# SEEK_END - end of the file

# f = open('file.txt', 'r')
# print(f.tell())
# f.seek(10)
# print(f.tell())
# f.close

# truncate method 

# f = open('file.txt', 'r+')
# print(f.tell())
# f.truncate(10)
# print(f.tell())
# f.close
