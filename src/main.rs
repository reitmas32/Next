mod interface;

use clap::{Parser, Subcommand};
use interface::commands;

#[derive(Parser, Debug)]
#[command(
    name = "next",
    about = "Manage your Next app development",
    version = "1.0",
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
    Create {
        output_directory: String,
    },

    Run{
        options: Option<String>,
    },

    Add,

    Build,

    CheckEnv,

    Clean,

    Exce,

    Get,

    Info,

    Set,

    Use,

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
