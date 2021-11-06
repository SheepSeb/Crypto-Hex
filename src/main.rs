extern crate crypto;
use self::crypto::digest::Digest;
use self::crypto::sha3::Sha3;

#[macro_use] extern crate rocket;

#[get("/")]
fn index() -> &'static str {
    "Hello, world!"
}

#[get("/sha3")]
fn sha3() -> String {
    let mut hasher = Sha3::sha3_256();
    hasher.input_str("Hello, world!");
    hasher.result_str()
}

#[launch]
fn rocket() -> _ {
    rocket::build()
                .mount("/", routes![index])
                .mount("/", routes![sha3])
}

// async fn main() {
//     rocket::build()
//         .mount("/hello", routes![world])
//         .launch()
//         .await;
// }

// fn main(){
//     // create a SHA3-256 object
//     let mut hasher = Sha3::sha3_256();
//     // write input message
//     hasher.input_str("abc");
//     // read hash digest
//     let hex = hasher.result_str();
//     assert_eq!(hex, "3a985da74fe225b2045c172d6bd390bd855f086e3e9d525b46bfe24511431532");
//     println!("{}",hex);
// }