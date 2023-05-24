class Model:
  
  """ Model class represents a general model, while the OnlineModel \
  class is a subclass specifically designed for online processing. \
  The Model class has an __init__ method that can be used to initialize \
  any required variables or resources, and a process method that performs\
  some computations or applies a model to the provided data. In this case, \
  the process method simply prints the data."""

    def __init__(self):
        # Initialize any required variables or resources
        
    def process(self, data):
        # Process the data, perform some computations, or apply a model
        # Do whatever you need to do with the data
        
        # Example: Printing the data
        print(data)


class OnlineModel(Model):
  """ The OnlineModel subclass extends the Model class and overrides the process method.\ 
  It accepts a stream as input and iterates over the stream, calling the parent class's \
  process method for each data item in the stream. """

    def process(self, stream):
        for data in stream:
            super().process(data)
