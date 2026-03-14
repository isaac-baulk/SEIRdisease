#include "../include/lattice.h"
#include "../include/agent.h"
#include <vector>

//constructor
Lattice::Lattice(int width, int height): width_(width), height_(height){
    grid.resize(width * height, nullptr);
}

//get 2d index
int Lattice::getIndex(int x, int y) const {
    return (y * width_) + x;
}

//should implement this helper in moveAgent later
bool Lattice::isOccupied(int x, int y) const {
    return grid[getIndex(x, y)] != nullptr;
}

int Lattice::getWidth() {
    return width_;
}

int Lattice::getHeight() {
    return height_;
}

//initially place agents
void Lattice::placeAgent(Agent* agent, int x, int y) { //should merge with moveAgent
    int index = getIndex(x, y);
    grid[index] = agent;   
    agent->move(x, y);
}

//move agents
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

//get 8 nearest neighbors
std::vector<Agent*> Lattice::getNeighbors(int x, int y) const {

    std::vector<Agent*> neighbors;
    //loop through nearest neighbors
    for (int dx = -1; dx <= 1; dx++) {
        for (int dy = -1; dy <= 1; dy++) {
            if (dx == 0 && dy == 0) continue;

            int check_x = x + dx;
            int check_y = y + dy;

            //ensure we don't look outside the map - using hard boundaries
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