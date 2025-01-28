mod interface;

use clap::{Parser, Subcommand};
use interface::commands;

#[derive(Parser, Debug)]
#[command(
    name = "next",
    about = "Manage your Next app development",
    version = "1.0",
    //TODO: Add mail account for the project
    author = "Next Development team <mail@placeholder.com>",
    subcommand_required = true,
    arg_required_else_help = true
)]
struct Cli{
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand, Debug)]
enum Commands {
    #[command(
        name = "create",
        about = "Create a new project of Next",
    )]
    Create {
        #[arg(
            help = "The directory where the project will be created"
        )]
        output_directory: String,
    },

    #[command(
        name = "run",
        about = "Run your Next application"
    )]
    Run{
        #[arg(
            help = "Options for running the application"
        )]
        options: Option<String>,
    },

    #[command(
        name = "add",
        about = "Add to property of current Next project"
    )]
    Add,

    #[command(
        name = "build",
        about = "Build a project of Next"
    )]
    Build,

    #[command(
        name = "check_env",
        about = "Check env for the NextPackages"
    )]
    CheckEnv,

    #[command(
        name = "clean",
        about = "Clean a project of Next"
    )]
    Clean,

    #[command(
        name = "exce",
        //Is this description correct? I copied from the README but idk lol
        about = "Add to property of Next project"
    )]
    Exce,

    #[command(
        name = "get",
        about = "Get property of the current Next project"
    )]
    Get,

    #[command(
        name = "info",
        about = "View info of current Next project"
    )]
    Info,

    #[command(
        name = "set",
        about = "Set property for the current Next project"
    )]
    Set,

    #[command(
        name = "use",
        about = "Add new library in current project"
    )]
    Use,

    #[command(
        name = "version",
        about = "View version of Next"
    )]
    Version,
}

fn main() {
    let cli = Cli::parse();

    match cli.command {
        Commands::Create { output_directory } => commands::create::create(output_directory),
        //TODO: Add the rest of the commands
        _ => println!("Not implemented")
    }

}
