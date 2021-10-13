use structopt::StructOpt;

#[derive(StructOpt)]
struct Cli {
    #[structopt(short = "s", long = "serial", default_value = "")]
    serial: String,
    #[structopt(short = "hp", long = "hostport")]
    host_port: i32,
    #[structopt(short = "dp", long = "deviceport")]
    device_port: i32,
    #[structopt(short = "n", long = "videonumber")]
    video_number: i32,
}

fn main() {
    let args = Cli::from_args();
    println!("{}", args.serial);
}
