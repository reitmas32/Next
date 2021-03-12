#include <manager_command.hpp>

ManagerCommand::ManagerCommand(/* args */) {}

ManagerCommand::~ManagerCommand()
{
    this->stackCommand.clear();
}

void ManagerCommand::execute()
{

    this->stackCommand.execute();
}

void ManagerCommand::initialize(int argc, char const *argv[])
{

    std::string list_args;
    list_args.reserve(100);

    if (argc < 2)
        return;

    for (int i = 1; i < argc; i++)
    {
        std::string line = argv[i];
        if (line == "create")
        {
            this->stackCommand.append(new PathCommand());
            this->stackCommand.append(new CreateProjectCommand(argv[i + 1]));
            this->stackCommand.append(new ReadHelpCommand());
        }
        else if (line == "mcreate")
        {
            this->stackCommand.append(new PathCommand());
            this->stackCommand.append(new MCreateProjectCommand(argv[i + 1]));
            this->stackCommand.append(new ReadHelpCommand());
        }
        else if (line == "build")
        {
            if (read_conf() == -1)
                return;
            std::string typeBuild;
            if (argv[i + 1] != nullptr)
            {
                typeBuild = argv[i + 1];
            }
            this->stackCommand.append(new BuildCommand(typeBuild));
        }
        else if (line == "run")
        {
            if (read_conf() == -1)
                return;
            this->stackCommand.append(new RunCommand());
        }
        else if (line == "clear" || line == "-cl")
        {
            if (read_conf() == -1)
                return;
            this->stackCommand.append(new ClearCommand());
        }
        else if (line == "import" || line == "i")
        {
            this->stackCommand.append(new ImportCommand(argv[i + 1]));
        }
        else if (line == "upgrade" || line == "u")
        {
            this->stackCommand.append(new PathCommand());
            this->stackCommand.append(new UpgradeCommand());
            this->stackCommand.append(new VersionCommand());
        }
        else if (line == "--help" || line == "-h")
        {
            this->stackCommand.append(new PathCommand());
            this->stackCommand.append(new ReadHelpCommand());
        }
        else if (line == "--version" || line == "-v")
        {
            this->stackCommand.append(new PathCommand());
            this->stackCommand.append(new VersionCommand());
        }
        else if (line == "--path" || line == "-p")
        {
            this->stackCommand.append(new PathCommand());
        }
        else if (line == "get" || line == "-g")
        {
            if (read_conf() == -1)
                return;
            this->stackCommand.append(new GetCommand());
        }
        else
        {
            list_args += " " + line;
        }
    }
}