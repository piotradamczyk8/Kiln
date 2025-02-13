print("test")

#import os
#import sys
#import django

# Dodanie ścieżki do katalogu głównego projektu
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#from app.gui import Desktop
#from app.sensors import MAX31855
#from app.sensors.ZCD import ZeroCrossDetector
#from app.sensors.PZEM_004T import PZEM_004T


# Dodanie ścieżki do katalogu głównego projektu
#sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Inicjalizacja GUI
#Desktop()

# Inicjalizacja PZEM-004T
#pzem = PZEM_004T()
 
# Inicjalizacja termopary
#thermocouple = MAX31855()

# Inicjalizacja detektora przejść przez zero
#zeroCrossDetector = ZeroCrossDetector()

# Ustawienie konfiguracji Django
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Kiln.settings')
#django.setup()

#from db.models import FiringCurve

#def main():
    # Przykład dodania nowego wpisu do bazy danych
    #new_curve = FiringCurve(time_point=10, temperature=150.0)
    #new_curve.save()

    # Przykład pobrania wszystkich wpisów z bazy danych
    #curves = FiringCurve.objects.all()
    #for curve in curves:
        #print(curve)

#if __name__ == "__main__":
    #main()

print("done")
