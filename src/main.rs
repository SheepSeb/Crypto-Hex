extern crate crypto;
use self::crypto::digest::Digest;
use self::crypto::sha3::Sha3;
// use crypto::hmac::Hmac;
// use crypto::mac::Mac;


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

// #[get("/aes")]
// fn aes() -> String{
// }

#[launch]
fn rocket() -> _ {
    rocket::build()
                .mount("/", routes![index])
                .mount("/", routes![sha3])
}