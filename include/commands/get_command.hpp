#pragma once
/**
 * @file run_command.hpp
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

#include <command_base.hpp>
#include <next_data.hpp>
#include <tools/exec.hpp>

#include <termcolor.hpp>

/**
 * @brief COmando para ejecutar el proyecto de Next
 * 
 */
class GetCommand : public CommandBase
{
private:
    std::string command;

public:
    /**
     * @brief Constructor
     * 
     */
    GetCommand(/* args */);

    /**
     * @brief Destructor
     * 
     */
    ~GetCommand();

    /**
     * @brief Ejecucion del comando
     * 
     * @return int 
     */
    int execute();
};