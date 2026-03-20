from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension(
        "seir_sim",      
        [
            "bindings/bindings.cpp", 
            "src/Agent.cpp", 
            "src/Lattice.cpp", 
            "src/mcsim.cpp"
        ],

        include_dirs=["include"],
        cxx_std=17,
    ),
]

setup(
    name="seir_sim",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)