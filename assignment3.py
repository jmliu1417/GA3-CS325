'''
    For testing he'll put it in a different directory, call <three_min_spanning_trees>,
    then check its output or whatever lmao
'''

def three_min_spanning_trees(input_file_path, output_file_path):
    '''
        code is put here
    '''
    
    #i just stored it in an array for now but it might be different
    
    infile = open(input_file_path, 'r')
    trees = []
    for x in infile.readline().strip().split(','):
        trees.append(int(x))
    infile.close()
    
    pass


# three_min_spanning_trees('','')