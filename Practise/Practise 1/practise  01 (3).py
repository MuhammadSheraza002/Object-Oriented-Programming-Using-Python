# It return squirel is playing or not
def squirel_play(temperature,is_summer):
    end_limit_temperature=90
    start_limit_temperature=60
    if is_summer==True:
        end_limit_temperature=100
    if temperature <=end_limit_temperature and temperature>=start_limit_temperature:
        return True
    return False

def main():
    temperature = int(input("Enter temperature: "))
    is_summer = False
    print(squirel_play(temperature,is_summer))
main()


