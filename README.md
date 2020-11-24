# OCR-on-Azure

## Co trzeba zrobić:
- Opis projektu  
- Funkcjonalności  
- Architektura  
- Organizacja pracy - kamienie milowe, Scrum  

## Funkcjonalności:
- Utworzenie konta użytkownika  
- Obługa logowania i przechowywania plików wcześniej przetwarzanych  
- Wgranie pliku wejściowego - zdjęcia/pdf z danymi tekstowymi w formie graficznej  
- Wyświetlenie tekstu rozpoznanego z pliku wejściowego  

## Architektura:
Aplikacja webowa będzie działać w kontenerze postawionym za pomocą narzędzia Docker. Jej kod zostanie zapisany w publicznym repozytorium na stronie Github. Będzie wykorzystywała wirtualne sieci Azure oraz komunikowała się z bazą danych. Weryfikacja użytkowników planowana jest poprzez Azure Key Vault.  
W ramach projektu użyte zostaną również Azure Cognitive Services (OCR, Form Recognizer) do obsługi plików wejściowych oraz inne serwisy związane z Azure Networking.

## Harmonogram:
**23.11.20 - Spotkanie organizacyjne. Opracowanie dokumentacji.**  
30.11.20 - Zapozanie się z działaniem poszczególnych serwisów Azure używanych w projekcie.  
07.12.20 - Przygotowanie środowiska - weryfikacja kosztów aplikacji, ustalenie polityk SLA.  
**14.12.20 - Przygotowanie mock-up'u aplikacji webowej.**  
21.12.20 - Implementacja bazy danych do przechowywania plików.  
**28.12.20 - Działająca aplikacja webowa, komunikująca się z Azure Cognitive Services, zdolna do wysłania pliku wejściowego i odebrania pliku JSON.**  
04.01.21 - Formatowanie pliku wyjściowego.  
11.01.21 - Implementacja systemu logowania użytkowników.  
**18.01.21 - Finalna wersja aplikacji.**  
25.01.21 - Testowanie bezpieczeństwa aplikacji. Przygotowanie prezentacji.  
**28.01.21 - Prezentacja projektów.**  




