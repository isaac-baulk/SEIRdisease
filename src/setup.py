from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension(
        "seir_sim",
        ["bindings.cpp", "agent.cpp", "lattice.cpp", "MCsim.cpp"],
        cxx_std=17,
    ),
]

setup(
    name="seir_sim",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)