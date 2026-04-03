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
    double g = 0.1;
    double r = 0.005;

    //generate simulation
    MCsim MCsim(grid_w, grid_h, b, s, g, r);

    //populate grid
    MCsim.populate_agents(0.94, 0.05, 0.01, 1000);

    //complete 100 monte carlo steps
    for (int i = 0; i < 100; i++) {
        MCsim.step();
    };

    MCsim.printHistory(); //output population history
    
    return 0;
}