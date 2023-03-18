from pydantic import  BaseSettings, SecretStr

class Settings(BaseSettings):
    # I used SecretStr because bot token  is the private information
    bot_token: SecretStr

    class Config:
        # The file name extension, this files extension will be read
        env_file = '.env'
        # Reading file's coding
        env_file_encoding = 'utf-8'


config = Settings()