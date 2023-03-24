import json

file = open("morse.json")
data = json.load(file)

def encode(message:str, mode:["return", "print"]="return") -> str:
	if mode in ["return", "print"] and type(message) == str:
		msg_list = [*message]
		encoded = []
		for character in msg_list:
			new_character = data["encode"][character]
			encoded.append(new_character)
		final_message = ' '.join(encoded)
		if mode == "return":
			return final_message
		else:
			print(final_message)
	else:
		if mode not in ["return", "print"]:
			print(f"error: argument \"mode\" must either be \"return\" or \"print\" (default is return)")
		if type(message) != str:
			print("error: message must be a string")

def decode(message:str, mode:["return", "print"]="return") -> str:
	if mode in ["return", "print"] and type(message) == str:
		msg_list = message.split(' ')
		decoded = []
		for character in msg_list:
			new_character = data["decode"][character]
			decoded.append(new_character)
		final_message = ''.join(decoded)
		if mode == "return":
			return final_message
		else:
			print(final_message)
	else:
		if mode not in ["return", "print"]:
			print(f"error: argument \"mode\" must either be \"return\" or \"print\" (default is return)")
		if type(message) != str:
			print("error: message must be a string")