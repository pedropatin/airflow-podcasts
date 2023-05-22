from dotenv import dotenv_values
import pwd

env_vars = dotenv_values('.env')

value = env_vars['CONSTRAINT_URL']

print(value)
