mod interface;

use structopt::StructOpt;
use interface::commands;

#[derive(StructOpt)]
#[structopt(name = "next", about = "Una aplicación de ejemplo con comandos")]
enum Next {
    #[structopt(name = "create", about = "Crea un nuevo proyecto")]
    Create {
        #[structopt(help = "El directorio donde se creará el proyecto")]
        path: String,
    },

    #[structopt(name = "version", about = "Muestra la versión de la aplicación")]
    Version,

    #[structopt(name = "info", about = "Muestra información sobre la aplicación")]
    Info,
}

fn main() {
    match Next::from_args() {
        Next::Create { path } => commands::create::create(path),
        Next::Version => {
            println!("next versión 1.0");
        },
        Next::Info => {
            println!("next es una aplicación de ejemplo.");
        },
    }
}