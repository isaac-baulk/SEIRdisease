#include "../include/lattice.h"
#include "../include/agent.h"
#include <vector>

//initialise lattice
Lattice::Lattice(int width, int height): width_(width), height_(height){
    grid.resize(width * height, nullptr);
}

//get 2d index
int Lattice::getIndex(int x, int y) const {
    return (y * width_) + x;
}

//method to check if grid cell is empty
bool Lattice::isOccupied(int x, int y) const {
    return grid[getIndex(x, y)] != nullptr;
}

//getters
int Lattice::getWidth() {
    return width_;
}

int Lattice::getHeight() {
    return height_;
}

//initially place agents
void Lattice::placeAgent(Agent* agent, int x, int y) { 
    int index = getIndex(x, y);
    grid[index] = agent;   
    agent->move(x, y);
}

//move agents
bool Lattice::moveAgent(Agent* agent, int old_x, int old_y, int new_x, int new_y) {
    int new_index = getIndex(new_x, new_y);
    int old_index = getIndex(old_x, old_y);

    //only move agent if target cell is empty
    if (grid[new_index] == nullptr) {
        
        grid[new_index] = agent;
        grid[old_index] = nullptr; //clear the old square
        
        agent->move(new_x, new_y); 
        
        return true;
    }
    
    return false; 
}

//get 8 nearest neighbours
std::vector<Agent*> Lattice::getNeighbours(int x, int y) const {

    std::vector<Agent*> neighbours;
    //loop through nearest neighbours
    for (int dx = -1; dx <= 1; dx++) {
        for (int dy = -1; dy <= 1; dy++) {
            if (dx == 0 && dy == 0) continue; //don't check the cell itself

            int check_x = x + dx;
            int check_y = y + dy;

            //ensure we don't look outside the map - using hard boundaries
            if (check_x >= 0 && check_x < width_ && check_y >= 0 && check_y < height_) {

                    int check_index = (check_y * width_) + check_x;
                    //if cell is not empty, add this neighbour to the list
                    if (grid[check_index] != nullptr) {
                        neighbours.push_back(grid[check_index]);
                    }
                }
            }
        }
    return neighbours;
}