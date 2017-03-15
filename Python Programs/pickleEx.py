import pickle 

example_dict = {'first': 23 , 'second': 45, 'third': 65, 'fourth': 'this will not be in the correct order' , 'fifth': 'dictionaries are not ordered by number', 'sixth': 897}
example_dict['seventh'] = 'I did not do the keys correctly'
example_dict['eight'] = 9080

#print(example_dict.keys())
#print(example_dict.values())

# wb : write binary
pickle_out = open('dict.pickle', 'wb')

# read data from the dictionary and put in the pickle file
pickle.dump(example_dict, pickle_out)
pickle_out.close()

# rb : read bytes
pickle_in = open('dict.pickle', 'rb')
# read the pickle file and put information into the dictionary
example_dict = pickle.load(pickle_in)

