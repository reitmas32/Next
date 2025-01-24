use clap::{Arg, ArgMatches, Command};

mod interface;
use interface::command_Handlers::{handle_create, handle_run};

fn main() {
    let matches = Command::new("next")
        .about("Manage your Next app development")
        .version("1.0")
        //TODO: Add mail account for the project
        .author("Next Development Team <mail@placeholder.com>")
        .subcommand_required(true)
        .arg_required_else_help(true)
        .arg(
            Arg::new("help")
                .short('h')
                .long("help")
                .help("Print this usage information"),
        )
        .subcommand(
            Command::new("create")
                .about("Create a new project of Next")
                .arg(
                    Arg::new("output_directory")
                        .help("The directory where the project will be created")
                        .required(true),
                ),
        )
        .subcommand(
            Command::new("run")
                .about("Run your Next application")
                .arg(
                    Arg::new("options")
                        .help("Options for running the application")
                        .required(false),
                ),
        )
        .subcommand(
            Command::new("add")
                .about("Add to property of current Next Project"))
        .subcommand(
            Command::new("build")
                .about("Build a project of Next"))
        .subcommand(
            Command::new("check_env")
                .about("Check env the NextPackages"))
        .subcommand(
            Command::new("clean")
                .about("Clean a project of Next"))
        .subcommand(
            Command::new("exce")
                .about("Add to property of current Next Project"))
        .subcommand(
            Command::new("get")
                .about("Get property of current Next Project"))
        .subcommand(
            Command::new("info")
                .about("View info the Next"))
        .subcommand(
            Command::new("set")
                .about("Set property of current Next Project"))
        .subcommand(
            Command::new("use")
                .about("Add new library in current project"))
        .subcommand(
            Command::new("version")
                .about("View version of the Next"))
        .get_matches();

    match matches.subcommand() {
        Some(("create", sub_matches)) => handle_create(sub_matches),
        Some(("run", sub_matches)) => handle_run(sub_matches),
        Some(("add", _)) => handle_add(sub_matches),
        Some(("build", _)) => handle_build(sub_matches),
        Some(("check_env", _)) => handle_check_env(sub_matches),
        Some(("clean", _)) => handle_clean(sub_matches),
        Some(("exce", _)) => handle_exce(sub_matches),
        Some(("get", _)) => handle_get(sub_matches),
        Some(("info", _)) => handle_info(sub_matches),
        Some(("set", _)) => handle_set(sub_matches),
        Some(("use", _)) => handle_use(sub_matches),
        Some(("version", _)) => handle_version(sub_matches),
        _ => unreachable!(), // clap ensures we don't reach here
    }
}
