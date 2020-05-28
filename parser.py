import ConfigParser
with open("output_filev2.txt") as f:
        fileread = f.read()

Config = ConfigParser.ConfigParser()
Config
Config.read(fileread)
print(Config.sections())
