#include <pybind11/pybind11.h>
#include <pybind11/stl.h>  
#include "../include/mcsim.h"

namespace py = pybind11;

PYBIND11_MODULE(seir_sim, m) {
    m.doc() = "C++ SEIR Monte Carlo Simulation Engine";

    py::class_<MCsim>(m, "MCsim")

        .def(py::init<int, int, double, double, double>(), 
             py::arg("grid_width"), py::arg("grid_height"), 
             py::arg("beta"), py::arg("sigma"), py::arg("gamma"))
        
        .def("populate_agents", &MCsim::populate_agents,
             py::arg("prob_susceptible"), py::arg("prob_exposed"),
             py::arg("pop_size"))
        
        .def("step", &MCsim::step)
        
        .def("getHistoryS", &MCsim::getHistoryS)
        .def("getHistoryE", &MCsim::getHistoryE)
        .def("getHistoryI", &MCsim::getHistoryI)
        .def("getHistoryR", &MCsim::getHistoryR)

        .def("getAgentCoordinates", &MCsim::getAgentCoordinates);
}