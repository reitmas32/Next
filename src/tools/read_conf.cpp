#include <tools/read_conf.hpp>

int readString(std::string key, std::string &data, picojson::object &root)
{
    if (root[key].is<std::string>())
    {
        data = root[key].get<std::string>();
    }
    else
    {
        std::cout << termcolor::red << "ERROR!!! <<" << key << ">> not is a std::string in conf.json\n\n"
                  << termcolor::reset;
        return -1;
    }
    return 0;
}

int readVector(std::string key, std::vector<std::string> &data, picojson::object &root)
{
    if (root[key].is<picojson::array>())
    {
        auto cmake_flags = root[key].get<picojson::array>();

        for (auto flag : cmake_flags)
        {
            if (flag.is<std::string>())
            {

                data.push_back(flag.get<std::string>());
            }
            else
            {
                std::cout << termcolor::red << "ERROR!!!" << key << ">> not is a std::array<std::string> in conf.json\n\n"
                          << termcolor::reset;
                return -1;
            }
        }
    }
    else
    {
        std::cout << termcolor::red << "ERROR!!!" << key << ">> not is a std::array<std::string> in conf.json\n\n"
                  << termcolor::reset;
        return -1;
    }
    return 0;
}

int read_conf()
{
#if defined(_WIN32)
    NextData::getInstance()->pwd = exec("cd");
#elif defined(__linux)
    NextData::getInstance()->pwd = exec("pwd");
#endif
    std::stringstream stringStream;
    std::ifstream file;
    //std::string name_file = NextData::getInstance()->name_
    // Read Json file
    file.open("conf.json", std::ios::binary);
    if (!file.is_open())
    {
        std::cout << termcolor::red << "This not Next Project \n\n"
                  << termcolor::reset;
        return -1;
    }
    stringStream << file.rdbuf();
    file.close();

    // Parse Json data
    picojson::value v;
    stringStream >> v;
    std::string err = picojson::get_last_error();
    if (!err.empty())
    {
        std::cerr << err << std::endl;
        return -1;
    }
    picojson::object &root = v.get<picojson::object>();
    if (readString("name_project", NextData::getInstance()->name_project, root) != 0)
        return -1;
    if (readString("build_system", NextData::getInstance()->build_system, root) != 0)
        return -1;
    if (readString("c_compiler", NextData::getInstance()->c_compiler, root) != 0)
        return -1;
    if (readString("cxx_compiler", NextData::getInstance()->cxx_compiler, root) != 0)
        return -1;
    if (readString("build_dir", NextData::getInstance()->build_dir, root) != 0)
        return -1;
    if (readString("build_system_exe", NextData::getInstance()->build_system_exe, root) != 0)
        return -1;
    if (readString("name_build", NextData::getInstance()->name_build, root) != 0)
        return -1;
    if (readVector("cmake_flags", NextData::getInstance()->cmake_flags, root) != 0)
        return -1;
    if (readVector("build_system_flags", NextData::getInstance()->build_system_flags, root) != 0)
        return -1;
    if (readVector("local_dependencies", NextData::getInstance()->local_dependencies, root) != 0)
        return -1;
    return 0;
}