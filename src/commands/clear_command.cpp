#include <commands/clear_command.hpp>

ClearCommand::ClearCommand(/* args */)
    : CommandBase()
{
    this->command += "rm -r " + NextData::getInstance()->build_dir;
}

ClearCommand::~ClearCommand()
{
}

int ClearCommand::execute()
{
    exec_void(this->command);
    std::cout<< termcolor::red << "Clear CmakeCache\n"<<termcolor::reset;
    return 0;
}