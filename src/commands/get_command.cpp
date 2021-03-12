#include <commands/get_command.hpp>

GetCommand::GetCommand(/* args */)
    : CommandBase()
{
    #if defined(_WIN32)
    //this->command += "cd build\\cmake && cmake ..\\.. && msbuild HELLO.sln "
    //                 "/p:Configuration=Release";
    this->command += "cd vendor ";
    for (auto dependencie : NextData::getInstance()->local_dependencies)
    {
        this->command += " && git clone " + dependencie;
    }
    
#elif defined(__linux)
    this ->command += "mkdir -p " + NextData::getInstance()->build_dir + " && ";
    this->command += "cd " + NextData::getInstance()->build_dir + " && cmake " + NextData::getInstance()->pwd + " -G \""+NextData::getInstance()->build_system+"\"";
    //Add Compilers
#endif
}

GetCommand::~GetCommand()
{
}

int GetCommand::execute()
{
#if defined(_WIN32)
    exec_void("mkdir vendor");
#endif
    exec_void(this->command);
    return 0;
}