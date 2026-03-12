#ifndef LATTICE_H
#define LATTICE_H

#include <vector>
#include "agent.h"

class Lattice {
    public:
        Lattice(); //default constructor with no parameters
        Lattice(double width, double height);
        double getWidth();
        double getHeight();
    private:
        double width;
        double height;
        std::vector<std::vector<std::vector<Agent*>>> grid; //use pointers not actual agents
};

#endif