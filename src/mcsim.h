#ifndef MCSIM_H
#define MCSIM_H
#include <vector>
#include <random>
#include "agent.h"

class MonteCarloSolver {
private:
    std::vector<Agent> population;
    double beta; 
    double sigma; 
    double gamma;
    double interaction_radius;

    // Random number generator setup
    std::mt19937 rng;
    std::uniform_real_distribution<double> dist{0.0, 1.0};

public:
    void step();
};
#endif