import time
from plyer import notification


if __name__ == '__main__':
    notification.notify(
        title="Please Drink Water",
        message="Most studies believe that drinking 3-4 litres of water every day can give you a radiant skin, better immune system, and healthier heart.",
        # app_icon = "C:\Users\Atharva\OneDrive\Documents\Python tutorial\glassofwater_84019.ico",
        timeout=1
    )
    time.sleep(60*60)