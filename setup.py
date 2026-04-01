from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        "seir_sim",      
        [
            "bindings/bindings.cpp", 
            "src/agent.cpp", 
            "src/lattice.cpp", 
            "src/mcsim.cpp"
        ],

        include_dirs=[pybind11.get_include(), 'include'],
        language='c++',
        extra_compile_args=['-std=c++17', '-O3']
    ),
]

setup(
    name='seir_project',
    version='1.0',
    ext_modules=ext_modules,
)
