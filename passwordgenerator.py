import random
import string

def generate_password(length, lowercase=True, uppercase=True, digits=True, symbols=True):
  """
  Generates a random password based on user-specified criteria.

  Args:
      length (int): Desired length of the password.
      lowercase (bool, optional): Include lowercase letters. Defaults to True.
      uppercase (bool, optional): Include uppercase letters. Defaults to True.
      digits (bool, optional): Include digits. Defaults to True.
      symbols (bool, optional): Include symbols. Defaults to True.

  Returns:
      str: The generated random password.
  """

  char_sets = []
  if lowercase:
    char_sets.append(string.ascii_lowercase)
  if uppercase:
    char_sets.append(string.ascii_uppercase)
  if digits:
    char_sets.append(string.digits)
  if symbols:
    char_sets.append(string.punctuation)

  if not char_sets:
    raise ValueError("At least one character set (lowercase, uppercase, digits, or symbols) must be included.")

  all_chars = ''.join(char_sets)
  random.shuffle(all_chars)

  password = ''.join(random.sample(all_chars, length))

  return password

if __name__ == "__main__":
  while True:
    try:
      length = int(input("Enter desired password length (minimum 8 characters): "))
      if length < 8:
        raise ValueError("Password length must be at least 8 characters.")

      lowercase = input("Include lowercase letters (y/n)? ").lower() == 'y'
      uppercase = input("Include uppercase letters (y/n)? ").lower() == 'y'
      digits = input("Include digits (y/n)? ").lower() == 'y'
      symbols = input("Include symbols (y/n)? ").lower() == 'y'

      password = generate_password(length, lowercase, uppercase, digits, symbols)
      print(f"Your generated password is: {password}")
      break

    except ValueError as e:
      print(f"Error: {e}")
      print("Please enter a valid length and character set preferences.")

