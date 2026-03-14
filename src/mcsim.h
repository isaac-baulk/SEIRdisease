#ifndef MCSIM_H
#define MCSIM_H
#include <vector>
#include <random>
#include "agent.h"
#include "lattice.h"

class MCsim {
private:
    std::vector<Agent> population;
    Lattice lattice;
    double beta; 
    double sigma; 
    double gamma;
    int pop_size;
    int inf_size;
    int initial_population;
    int initial_infected;

    // Random number generator setup
    std::mt19937 rng;
    std::uniform_real_distribution<double> dist{0.0, 1.0};

public:
    MCsim(int initial_population, int initial_infected, int grid_w_, int grid_h_);
    void step();
};

#endif