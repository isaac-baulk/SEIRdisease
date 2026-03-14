#include "lattice.h"
#include "agent.h"
#include <vector>

Lattice::Lattice(int width, int height) {
    width_ = width;
    height_ = height;
    grid.resize(width * height, nullptr);
}

int Lattice::getIndex(int x, int y) const {
    return (y * width_) + x;
}

bool Lattice::placeAgent(Agent* agent, int x, int y) { //should merge with moveAgent
    int index = getIndex(x, y);
    if (grid[index] == nullptr) {
        
        grid[index] = agent;   
        agent->move(x, y);
        
        return true;
    }
    
    return false; 
}

bool Lattice::moveAgent(Agent* agent, int old_x, int old_y, int new_x, int new_y) {
    int new_index = getIndex(new_x, new_y);
    int old_index = getIndex(old_x, old_y);

    if (grid[new_index] == nullptr) {
        
        grid[new_index] = agent;
        grid[old_index] = nullptr; // Clear the old square
        
        agent->move(new_x, new_y); 
        
        return true;
    }
    
    return false; 
}

std::vector<Agent*> Lattice::getNeighbors(int x, int y) const {

    std::vector<Agent*> neighbors;
    // Loop through the 3x3 grid centered on (x, y)
    for (int dx = -1; dx <= 1; dx++) {
        for (int dy = -1; dy <= 1; dy++) {
            
            // Skip the center cell (the agent shouldn't infect itself)
            if (dx == 0 && dy == 0) continue;

            int check_x = x + dx;
            int check_y = y + dy;

            // BOUNDARY CHECK: Ensure we don't look outside the map - using hard boundaries
            if (check_x >= 0 && check_x < width_ && check_y >= 0 && check_y < height_) {

                    int check_index = (check_y * width_) + check_x;

                    if (grid[check_index] != nullptr) {
                        neighbors.push_back(grid[check_index]);
                    }
                }
            }
        }
    return neighbors;
}