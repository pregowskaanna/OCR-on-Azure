# OCR-on-Azure

## Opis projektu:
Celem naszego projektu jest stworzenie i wdrożenie aplikacji webowej, która będzie służyła do przetwarzania obrazów lub skanów dokumentów na tekst/formularz lub dokument cyfrowy. Aplikacja będzie umożliwiała stworzenie konta oraz zalogowanie się i przechowywanie obrazów, zeskanowanych dokumentów oraz ich cyfrowych odpowiedników.

## Funkcjonalności:
- Utworzenie konta użytkownika  
- Obługa logowania i przechowywania plików wcześniej przetwarzanych  
- Wgranie pliku wejściowego - zdjęcia/pdf z danymi tekstowymi w formie graficznej  
- Wyświetlenie tekstu rozpoznanego z pliku wejściowego  

## Architektura:
Projekt zostanie zrealizowany z użyciem języka Python w wersji 3 i frameworka FastAPI.  
Aplikacja webowa będzie działać w kontenerze postawionym za pomocą narzędzia Docker. Jej kod zostanie zapisany w publicznym repozytorium na stronie Github. Będzie wykorzystywała Azure Networking oraz komunikowała się z bazą danych. Weryfikacja użytkowników planowana jest poprzez Azure Key Vault.  
W ramach projektu użyte zostaną również Azure Cognitive Services (OCR, Form Recognizer) do obsługi plików wejściowych oraz inne serwisy związane z Azure Networking.

![Diagram serwisów](diagram_serwisow.png)

## Organizacja pracy:
Planujemy wykonać projekt przy wykorzystaniu zwinnej metodyki organizacji pracy. Spotkania będą odbywać się co najmniej raz w tygodniu i będą polegać na omówieniu bieżących postępów i zaplanowaniu zadań na następny sprint. Poniżej znajduje się wstępny harmonogram, który może jednak ulec zmianie w związku z niewielkim zespołem i co się z tym wiąże -- wysoką elastycznością.

### Harmonogram:
**23.11.20 - Spotkanie organizacyjne. Opracowanie dokumentacji.**  
25.11.20 - Rozszerzenie dokumentacji. Przygotowanie diagramu.  
30.11.20 - Zapoznanie się z działaniem poszczególnych serwisów Azure używanych w projekcie.  
07.12.20 - Przygotowanie środowiska - weryfikacja kosztów aplikacji, ustalenie polityk SLA.  
**14.12.20 - Przygotowanie mock-up'u aplikacji webowej.**  
21.12.20 - Implementacja bazy danych do przechowywania plików.  
**28.12.20 - Działająca aplikacja webowa, komunikująca się z Azure Cognitive Services, zdolna do wysłania pliku wejściowego i odebrania pliku JSON.**  
04.01.21 - Formatowanie pliku wyjściowego.  
11.01.21 - Implementacja systemu logowania użytkowników.  
**18.01.21 - Finalna wersja aplikacji.**  
25.01.21 - Testowanie bezpieczeństwa aplikacji. Przygotowanie prezentacji.  
**28.01.21 - Prezentacja projektów.**  




