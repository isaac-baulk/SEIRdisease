#include "../include/mcsim.h"
#include <iostream>

MCsim::MCsim(int grid_w, int grid_h, double b, double s, double g)
    : lattice(grid_w, grid_h), beta(b), sigma(s), gamma(g), rng(std::random_device{}())
{}

void MCsim::recordStats() {
    int current_S = 0;
    int current_E = 0;
    int current_I = 0;
    int current_R = 0;

    //recount all agents in all states
    for (const auto& agent : population) {
        switch (agent.getState()) {
            case InfectionState::SUSCEPTIBLE: current_S++; break;
            case InfectionState::EXPOSED:     current_E++; break;
            case InfectionState::INFECTIOUS:  current_I++; break;
            case InfectionState::RECOVERED:   current_R++; break;
        }
    }

    history_S.push_back(current_S);
    history_E.push_back(current_E);
    history_I.push_back(current_I);
    history_R.push_back(current_R);
}

void MCsim::populate_agents(double p_sus, double p_exp, int pop_size) {

    //check pop isnt too big
    int max_capacity = lattice.getWidth() * lattice.getHeight();
    if (pop_size > max_capacity) {
        throw std::runtime_error("Population size exceeds lattice capacity!");
    }

    population.reserve(pop_size);

    //set up distributions
    std::uniform_int_distribution<int> dist_x(0, lattice.getWidth() - 1);
    std::uniform_int_distribution<int> dist_y(0, lattice.getHeight() - 1);
    std::uniform_real_distribution<double> dist_prob(0.0, 1.0);

    //make pop
    for (int i = 0; i < pop_size; ++i) {
        
        //find empty coord using do/while loop
        int random_x, random_y;
        do {
            random_x = dist_x(rng);
            random_y = dist_y(rng);
        } while (lattice.isOccupied(random_x, random_y)); //keep going if cell is occupied

        //make agent
        Agent new_agent(i, random_x, random_y);

        //assign state
        double p = dist_prob(rng);
        
        //only need to update exposed cause susceptible is default state
        if (p < p_exp) {
            new_agent.expose();
        } 

        population.push_back(new_agent);
        lattice.placeAgent(&population.back(), random_x, random_y);
    }
    recordStats();
}

void MCsim::step() {
    
    //distributions
    std::uniform_int_distribution<int> dist_dir(-1, 1);
    std::uniform_real_distribution<double> dist_prob(0.0, 1.0);

    for (auto& agent : population) {
        int dx, dy;
        do {
            dx = dist_dir(rng);
            dy = dist_dir(rng);
        } while (dx == 0 && dy == 0); //make sure not zero 

        int old_x = agent.getX();
        int old_y = agent.getY();

        //periodic boundaries
        int new_x = (old_x + dx + lattice.getWidth()) % lattice.getWidth();
        int new_y = (old_y + dy + lattice.getHeight()) % lattice.getHeight();

        lattice.moveAgent(&agent, old_x, old_y, new_x, new_y);


        if (agent.getState() == InfectionState::EXPOSED) {
            if (dist_prob(rng) < sigma) {
                agent.infect();
            }
        }

        else if (agent.getState() == InfectionState::INFECTIOUS) {
            if (dist_prob(rng) < gamma) {
                agent.recover();
            }
        }

        if (agent.getState() == InfectionState::SUSCEPTIBLE) {
            //check neighbors
            std::vector<Agent*> neighbors = lattice.getNeighbors(agent.getX(), agent.getY());
            
            for (Agent* neighbor : neighbors) {
                if (neighbor->getState() == InfectionState::INFECTIOUS) {
                    
                    //check prob against beta
                    if (dist_prob(rng) < beta) {
                        agent.expose();
                        break;
                    }
                }
            }
        }

        agent.incrementStep();
    }
    recordStats();
}

//getters
std::vector<int> MCsim::getHistoryS() const {
    return history_S;
}

std::vector<int> MCsim::getHistoryE() const {
    return history_E;
}

std::vector<int> MCsim::getHistoryI() const {
    return history_I;
}

std::vector<int> MCsim::getHistoryR() const {
    return history_R;
}

std::vector<std::vector<int>> MCsim::getAgentCoordinates() const {
    
    std::vector<std::vector<int>> agent_data;
    agent_data.reserve(population.size()); 

    for (const auto& agent : population) {
        
        //make enum class a normal integer
        int state_int = static_cast<int>(agent.getState());
        
        //make agent data into a vector
        agent_data.push_back({agent.getX(), agent.getY(), state_int});
    }

    return agent_data;
}

//output
void MCsim::printHistory() const {
    std::cout << "Step\tS\tE\tI\tR\n";
    std::cout << "------------------------------------\n";

    for (size_t i = 0; i < history_S.size(); i += 5) {
        std::cout << i << "\t"
                  << history_S[i] << "\t"
                  << history_E[i] << "\t"
                  << history_I[i] << "\t"
                  << history_R[i] << "\n";
    }

    size_t last_step = history_S.size() - 1;
    if (last_step % 5 != 0) {
        std::cout << last_step << "\t"
                  << history_S[last_step] << "\t"
                  << history_E[last_step] << "\t"
                  << history_I[last_step] << "\t"
                  << history_R[last_step] << "\n";
    }
}