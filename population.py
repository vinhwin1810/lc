from os.path import basename, exists

def download(url):
    filename = basename(url)
    if not exists(filename):
        from urllib.request import urlretrieve
        local, _ = urlretrieve(url, filename)
        print('Downloaded ' + local)

download('https://github.com/AllenDowney/ModSimPy/raw/master/' +
         'modsim.py')
from modsim import *

#QUESTION 1:
def the_snappening(population):
    '''
    Thanos's finger snap => half of population gone
    '''
    return population // 2

def growth_func_quad(t, pop, system):
    '''
    quadratic growth function from Chap7
    '''
    return system.alpha * pop + system.beta * pop**2

def run_simulation(system, growth_func):
    '''
    This run_simulation function can run with any models because it takes the growth func as a param.
    '''
    results = TimeSeries()
    results[system.t_0] = system.p_0

    for t in range(system.t_0, system.t_end):
        growth = growth_func(t, results[t], system)
        results[t+1] = results[t] + growth

    return results

#QUESTION 2:
def the_unsnappening(current_population, snapped_population):
    '''
    Restores the snapped population back to the current population during the Un-Snappening event.
    current_population: The population in the year of the Un-Snappening (2030)
    snapped_population: The population that was lost during the Snappening
    '''
    return current_population + snapped_population

def run_simulation1(system, growth_func):
    '''
    Runs a population simulation for Snappening and Un-Snappening.
    '''
    results = TimeSeries()
    results[system.t_0] = system.p_0
    snapped_population = system.p_0 * 2 - system.p_0  # The population halved in 2025

    for t in range(system.t_0, system.t_end):
        if t == 2030:  #  Unsnappening
            results[t] = the_unsnappening(results[t], snapped_population)
        if t < system.t_end:
            growth = growth_func(t, results[t], system)
            results[t+1] = results[t] + growth

    return results

#Question 3:
'''
One way to reduce sufferings is to improvements in healthcare (government spend more money on healthcare)
'''
def growth_func_with_healthcare(t, pop, system):
    """
        t: Current time
        pop: Current population
    Returns:
        float: Net growth of the population at time t
    """
    
    death_rate_reduction = system.healthcare_investment * system.healthcare_efficiency # improved healthcare  => decrease in the death rate
    effective_death_rate = max(system.base_death_rate - death_rate_reduction, 0)

    alpha = system.birth_rate - effective_death_rate
    beta = system.beta
    
    return alpha * pop + beta * pop**2