use clap::ArgMatches;

pub fn handle_create(matches: &ArgMatches) {
    if let Some(output_directory) = matches.value_of("output_directory") {
        println!("Creating project in directory: {}", output_directory);
    }
}

pub fn handle_run(matches: &ArgMatches) {
    if let Some(options) = matches.value_of("options") {
        println!("Running application with options: {}", options);
    } else {
        println!("Running application with default options.");
    }
}

pub fn handle_add(matches: &ArgMatches){

}
