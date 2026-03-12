#ifndef AGENT_H
#define AGENT_H

enum class InfectionState { SUSCEPTIBLE, EXPOSED, INFECTIOUS, RECOVERED };

class Agent {
    private:
        int id;
        InfectionState current_state; 
        double x;
        double y;
        int steps_in_state;

    public:
        //init
        Agent(int id, double start_x, double start_y);

        //getters
        InfectionState getState() const;
        double getX() const;
        double getY() const;
        int getStepsInState() const;
        
        //behaviours
        void expose();
        void infect();
        void recover();
        void randomWalk(double max_x, double max_y);
        void incrementStep();
};

#endif