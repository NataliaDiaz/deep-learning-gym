    def image2double(self, filename):
        import cv2
        import numpy as np
        info = np.iinfo(im.dtype) # Get the data type of the input image
        return im.astype(np.float) / info.max # Divide all values by the largest possible value in the datatype

    def image2npArray(self, filename):
        pic = Image.open(filename)
        pix = np.array(pic)
        print "image2array:", pix.shape, type(pix)
        return image
    
    def save_architecture_and_weights(self, model):
        #The generated JSON / YAML files are human-readable and can be manually edited if needed.
        self.model_json = model.to_json()
        create_path_if_doesnt_exist(self.json_filename)
        with open(self.json_filename, 'w+') as outfile: # + creates the file if does not exist
            json.dump(self.model_json, outfile, indent=4) #json.dump(data, outfile) # data is a dict
            print "writing json model to ", self.json_filename, "\n",self.model_json
    
        #return a representation of the model as a YAML string (does not include the weights, only the architecture).
        self.yaml_string = model.to_yaml()
        # saves the weights of the model as a HDF5 file.
        model.save_weights(self.weights_filename)
        self.weights = model.get_weights()
        # save a dictionary containing the configuration of the model. The model can be reinstantiated from its config via:
        self.config = model.get_config()
        model.save('model_'+self.model_name+'.h5')  # creates a HDF5 file 'my_model.h5'
        #del model  # deletes the existing model
        print "Saved weights in ",self.weights_filename,"\nYaml string for model: \n",self.yaml_string
        print "Model summary: \n", model.summary()
    
    def get_trained_model(self):
        #model = Model.from_config(self.config)
        # or, for Sequential:
        #model = Sequential.from_config(self.config)
        #model.get_weights() returns a list of all weight tensors in the model, as Numpy arrays.
        # return a compiled model
        return load_model(self.model_filename)
        # needed? model.set_weights(self.weights)
    
    def create_path_if_doesnt_exist(path_to_file):
        if not os.path.exists(os.path.dirname(path_to_file)):
            try:
                os.makedirs(os.path.dirname(path_to_file))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

       