#ifndef LATTICE_H
#define LATTICE_H

#include <vector>
#include "../include/agent.h"

class Lattice {
    public:
        Lattice(int width, int height);
        bool placeAgent(Agent* agent, int x, int y); //need to count agents in population when placing
        std::vector<Agent*> getNeighbors(int x, int y) const;
        bool moveAgent(Agent* agent, int old_x, int old_y, int new_x, int new_y);
    private:
        double width_;
        double height_;
        int getIndex(int x, int y) const; //helper function to get index for 2d array
        std::vector<Agent*> grid; //use pointers not actual agents
};

#endif