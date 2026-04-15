def get_valid_prob(param_name):
    #validate probabibilites and fractions
    while True:
        user_input = input(f'Enter a value for {param_name} (must be between 0 and 1): ')
        
        try:
            value = float(user_input)
            #check value is in valid range for probability
            if (value > 1) or (value < 0):
                print('Must be between 0 and 1')
            else:
                return value 
                
        except ValueError: #raise error if float not entered
            print('Invalid float')

def get_inputs():
    #validate grid size --------------------------------------------
    while True:
        user_input = input('Enter a grid size: ')
    
        try:
            grid_size = int(user_input)
            
            if grid_size <= 0 or grid_size > 1000:
                print('Must be greater than zero and smaller than 1000')
            else:
                break
            
        except ValueError:
            print('Invalid int')

    #validate population size --------------------------------------------
    while True:
        user_input = input('Enter a population size: ')
    
        try:
            N = int(user_input)
            
            if (N <= 0) or (N > (grid_size * grid_size)):
                print('Must be greater than zero and smaller than squared grid size')
            else:
                break
            
        except ValueError:
            print('Invalid int')

    #validate number of days --------------------------------------------
    while True:
        user_input = input('Enter number of days to run (20 steps per day): ')
    
        try:
            days = int(user_input)
            
            if days <= 0:
                print('Must be greater than zero')
            else:
                break
            
        except ValueError:
            print('Invalid int')

    # validate infection parameters --------------------------------------------
    param_names = ['beta', 'sigma', 'gamma', 'reinfect', 'prop_exp', 'prop_inf']
    param_results = {}

    for name in param_names:
        param_results[name] = get_valid_prob(name)

    # calculate adjusted beta for MC sim --------------------------------------------
    beta = param_results['beta']
    pop_density = N/(grid_size*grid_size)
    k = 8 * pop_density #avg number of nearest neighbours is 8 neighbours * population density
    beta_mc = beta / k #beta accounts for number of contacts that agents make per step

    return param_results, N, beta_mc, grid_size, days
   