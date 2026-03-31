#ifndef MCSIM_H
#define MCSIM_H
#include <vector>
#include <random>
#include "../include/agent.h"
#include "../include/lattice.h"

class MCsim {
    private:
        std::vector<Agent> population;
        Lattice lattice;
        double beta; 
        double sigma; 
        double gamma;

        //tracking pop sizes
        std::vector<int> history_S;
        std::vector<int> history_E;
        std::vector<int> history_I;
        std::vector<int> history_R;
        void recordStats();

        //generator setup
        std::mt19937 rng;
        std::uniform_real_distribution<double> dist{0.0, 1.0};

    public:
        MCsim(int grid_w_, int grid_h_, double b, double s, double g);
        void step();
        void populate_agents(double p_sus, double p_exp, double p_inf, int pop_size);
        void printHistory() const;
        
        //will use these getters later for plotting
        std::vector<int> getHistoryS() const;
        std::vector<int> getHistoryE() const;
        std::vector<int> getHistoryI() const;
        std::vector<int> getHistoryR() const;

        std::vector<std::vector<int>> getAgentCoordinates() const;
};

#endif