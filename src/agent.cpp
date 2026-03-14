#include "agent.h"

// Constructor implementation
Agent::Agent(int id, double start_x, double start_y) 
    : id(id), current_state(InfectionState::SUSCEPTIBLE), x(start_x), y(start_y) {
}

// Getter implementation
InfectionState Agent::getState() const {
    return current_state;
}

double Agent::getX() const {
    return x;
}

double Agent::getY() const {
    return y;
}

// Behavior implementation
void Agent::expose() {
    if (current_state == InfectionState::SUSCEPTIBLE) {
        current_state = InfectionState::EXPOSED;
    }
}

void Agent::infect() {

}

void Agent::recover() {

}

//setters 
void Agent::move(int newx, int newy) {
    x = newx;
    y = newy;
}

void Agent::incrementStep() {
    steps_in_state++;
}