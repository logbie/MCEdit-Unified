import zipfile
import os
import json

models = {}

#ARGS: reference name, filename in jar
#registers a model
def registerModel(blockname, filename):
    models[blockname] = Model(blockname, filename)

#ARGS: reference name
#RETURNS: a model object
def getModel(blockname):
    return models[blockname]
    
class Model:
    
    #ARGS: reference name, filename in jar
    def __init__(self, inblockname, filename):
        self.blockname = inblockname
        self.shapes = []
        
        file = open("models/block/" + filename + ".json", "r")
        data = json.loads(file.read())
        file.close()
        while True :
            if "elements" in data:
                for i in range(0, len(data["elements"])): #loop through all elements
                    self.shapes.extend([[data["elements"][i]["from"], data["elements"][i]["to"]]]) #add model to list
            if "parent" in data:
                file = open("models/" + data["parent"] + ".json", "r")
                data = json.loads(file.read())
                file.close()
            else:
                break #breaks when there is no parent file
        
    def render(self):
        #render stuffz
        print(self.getBlockName() + ": " + str(self.shapes))
    
    #RETURNS: reference name
    def getBlockName(self):
        return self.blockname
        
registerModel("dave", "cobblestone")
getModel("dave").render()