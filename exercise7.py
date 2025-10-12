# import os
# import random 

# def randomFileNameGenerator(n):
#     res = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k = n))
#     return res

# os.mkdir("clutter")
# for i in range(0,100):
#     with open(os.path.join("clutter", f"{randomFileNameGenerator(5)}{i}.txt"), "w") as f:
#         pass
# os.rename("clutter", "organizedClutter")
# files = [os.path.join("organizedClutter", f) for f in os.listdir("organizedClutter") if f.endswith(".txt")]
# files.sort(key=lambda f: int(os.path.splitext(os.path.basename(f))[0]))
# for i, f in enumerate(files, start=1):
#     os.rename(f, os.path.join("organizedClutter", f"{i}.txt"))

