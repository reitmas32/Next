#pragma once
/**
 * @file next_data.hpp
 * @author Oswaldo Rafael Zamora Ramirez rafa.zamora.rals@gmail.com
 * @brief 
 * @version 2.0.0
 * @date 2021-02-08
 * 
 * @copyright Copyright (c) 2021
 * 
 */
#include <iostream>
#include <string>
#include <vector>

/**
 * @brief Clase que almacena los datos necesarios para el uso de Next por ejemplo 7
 *        La ubicacion en el sistema donde esta instalado Next
 * 
 */
class NextData
{
private:
    /* Here will be the instance stored. */
    static NextData *instance;

    /* Private constructor to prevent instancing. */
    NextData();

public:
    /* Static access method. */
    static NextData *getInstance();

    std::string path = "";
    std::string name_project;
    std::string name_build;
    std::string build_system;
    std::string c_compiler;
    std::string cxx_compiler;
    std::string build_dir;
    std::string pwd;
    std::string build_system_exe;
    std::vector<std::string> build_system_flags;
    std::vector<std::string> cmake_flags;
    std::vector<std::string> local_dependencies;

    void printData()
    {
        std::cout << NextData::getInstance()->path << '\n';
        std::cout << NextData::getInstance()->name_project << '\n';
        std::cout << NextData::getInstance()->name_build << '\n';
        std::cout << NextData::getInstance()->build_system << '\n';
        std::cout << NextData::getInstance()->c_compiler << '\n';
        std::cout << NextData::getInstance()->cxx_compiler << '\n';
        std::cout << NextData::getInstance()->build_dir << '\n';
        std::cout << NextData::getInstance()->pwd << '\n';
        std::cout << NextData::getInstance()->build_system_exe << '\n';

        std::cout << "cmake_flags" << '\n';
        for (auto flag : NextData::getInstance()->cmake_flags)
        {
            std::cout << flag << '\n';
        }
        std::cout << "build_system_flags" << '\n';
        for (auto flag : NextData::getInstance()->build_system_flags)
        {
            std::cout << flag << '\n';
        }
        std::cout << "local_dependencies" << '\n';
        for (auto flag : NextData::getInstance()->local_dependencies)
        {
            std::cout << flag << '\n';
        }
    }
};