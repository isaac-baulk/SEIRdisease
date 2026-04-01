#ifndef AGENT_H
#define AGENT_H

enum class InfectionState {SUSCEPTIBLE, EXPOSED, INFECTIOUS, RECOVERED};

class Agent {
    private:
        int id_;
        InfectionState current_state; 
        int x;
        int y;

    public:
        //init
        Agent(int id, int start_x, int start_y);

        //getters
        InfectionState getState() const;
        int getX() const;
        int getY() const;
        
        //behaviours
        void expose();
        void infect();
        void recover();
        void move(int newx, int newy);

        //setter to force state
        void setState(InfectionState new_state);
};

#endif