#include "../include/agent.h"

//initialise agent
Agent::Agent(int id, int start_x, int start_y) : id_(id), x(start_x), y(start_y){
    current_state = InfectionState::SUSCEPTIBLE;
}

//getters
InfectionState Agent::getState() const {
    return current_state;
}

int Agent::getX() const {
    return x;
}

int Agent::getY() const {
    return y;
}

//methods to update state of agent
void Agent::expose() {
    if (current_state == InfectionState::SUSCEPTIBLE) {
        current_state = InfectionState::EXPOSED;
        steps_in_state = 0;
    }
}
 
void Agent::infect() {
    if (current_state == InfectionState::EXPOSED) {
        current_state = InfectionState::INFECTIOUS;
        steps_in_state = 0;
    }
}

void Agent::recover() {
    if (current_state == InfectionState::INFECTIOUS) {
        current_state = InfectionState::RECOVERED;
        steps_in_state = 0;
    }
}

//set agent position to new position 
void Agent::move(int newx, int newy) {
    x = newx;
    y = newy;
}

//update timestep
void Agent::incrementStep() {
    steps_in_state++;
}