#[derive(Debug)]
enum TOKENS {
	FN,
	IDENT,
	LB,
	RB,
	LPAREN,
	RPAREN,
}

use TOKENS::*;


fn lexer(block_code:&mut String) -> Vec<TOKENS> {
	let pre_process = block_code.split(" ");
	let mut token_vec:Vec<TOKENS> = Vec::new();
	
	for i in pre_process {
		match i {
			"fn" => token_vec.push(FN),
			"{" => token_vec.push(LB),
			"(" => token_vec.push(LPAREN),
			")" => token_vec.push(RPAREN),
			"}" => token_vec.push(RB),
			_ => token_vec.push(IDENT),
		}
	}
	token_vec
}

fn paren_check(block:&String) -> bool {

	let mut stack: Vec<char> = Vec::new();
	for i in block.chars() {
		match i {
			'{' => stack.push(i),
			_ => {},
		}
	}
	for i in block.chars() {
		print!("{:?}", i);
	}	
	for i in block.chars() {
		match i {
			'}' => {stack.pop();},
			_ => {},
		}
	}
	
	match stack.is_empty() {
		true => return true,
		false => return false,
	}
}

fn main() {
	let block = "{{{{}}}}".to_string();
	let mut block_code = "fn main ( ) { }".to_string();
	
	match paren_check(&block) {
		false => {println!("Missing one or more parenthesis");},
		true => {println!("Braces check valid");},
	}
	let lex_output = lexer(&mut block_code);
	println!("{:?}",lex_output);
}