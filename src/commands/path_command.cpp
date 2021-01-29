#include <commands/path_command.hpp>

#include <tools/exec.hpp>

#include <next_data.hpp>

#define NUM_VARS 50

PathCommand::PathCommand(/* args */) : CommandBase()
{
}

PathCommand::~PathCommand()
{
}

int PathCommand::execute(/* args */)
{
    int status;
    std::string path_command = exec("echo $PATH");

    std::vector<std::string> list_vars;
    list_vars.reserve(NUM_VARS);

    std::string line = "";

    if (path_command.find("Next") > path_command.size())
    {
        std::cout << "No se encontro Next en el Path" << '\n';
        return -1;
    }

    for (auto c : path_command)
    {
        if (c != ':')
        {
            line += c;
        }
        else
        {
            list_vars.push_back(line);
            line.clear();
        }
    }

    list_vars.push_back(line);
    line.clear();

    for (auto var : list_vars)
    {
        if(var.find("Next") < var.size()){
            //Esto esta absolutamente mal, es para quitar '/bin' del PATH 
            std::size_t index = var.size();
            index -= 4;
            var.replace(index, 4, "");
            //Hasta aca
            NextData::getInstance()->path = var;
        }
    }

    return status;
}