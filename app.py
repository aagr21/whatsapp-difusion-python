import webbrowser as web
import time
import pyautogui as pg

phone_numbers = [
    76371096,
    76001604,
    77800061,
    71388156,
    60978044,
    73419120,
    70482347,
    78478886,
    76086684,
    70857062,
    72131602,
    77304634,
    70356490,
    77313000,
    78457483,
    74622427,
    69240891,
    71004033,
    65864287,
    68583388,
    71757599,
    75570072,
    67727501,
    60953394,
    76044251,
    60875785,
    76016787,
    79900060,
    61382766,
    77880044,
    70888031,
    73134530,
    72664938,
    70846105,
    78079698,
    79466514,
    71611514,
    78136406,
    70921118,
    70978854,
    72111240,
]


def send_message_whatsapp(numbers: list, message: str):
    for number in numbers:
        web.open(f"https://web.whatsapp.com/send?phone=591{number}&text={message}")
        time.sleep(7)
        pg.click(1230, 964)
        time.sleep(1)
        pg.press("enter")


if __name__ == "__main__":
    send_message_whatsapp(
        phone_numbers, """Buenas tardes, recordarles que mañana martes 09 de Abril es la reunión en el Auditorio del Museo del Altillo "Beni" que queda ubicado en la Calle Beni entre Calle Bolívar y Calle Sucre, a horas 05:00 pm.%0AMe despido atentamente:%0ASecretaría Municipal de Tránsito y Transporte "SMTT".""",)
