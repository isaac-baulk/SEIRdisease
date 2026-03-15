#include <iostream>
#include <cstdlib>
#include "../include/mcsim.h"
#include "../include/lattice.h"
#include "../include/agent.h"

int main(){

    int grid_w = 100;
    int grid_h = 100;
    double b = 1;
    double s = 0.1;
    double g = 0.005;

    MCsim MCsim(grid_w, grid_h, b, s, g);

    MCsim.populate_agents(0.95, 0.05, 1000);

    for (int i = 0; i < 100; i++) {
        MCsim.step();
    };

    MCsim.printHistory();
    
    return 0;
}