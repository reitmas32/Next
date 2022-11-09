from src.app.builders.cmake import create_cmake, build_cmake

base_builders = {}


base_builders['cmake'] = {'create': create_cmake, 'build': build_cmake}