#include "mcsim.h"

MCsim::MCsim(int initial_population, int initial_infected, int grid_w, int grid_h) {
    pop_size = initial_population;
    inf_size = initial_infected;
    Lattice(grid_w, grid_h);
}

void populate_agents() {

}

void MCsim::step() {

}