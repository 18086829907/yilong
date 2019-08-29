import os
import pickle
filePath = os.path.join(os.getcwd(), 'allUser.txt')
allUsers = {}
with open(filePath, 'wb') as f:
    pickle.dump(allUsers, f)