# OCR-on-Azure

0. Wymagania
1. Spotkanie z product ownerem
2. Use Case'y - wymagania funkcjonalne i niefunkcjonalne
3. Kod - czestotliwość, jakość, kto
4. Dokumentacja - architektura, scrum, harmonogram, kamienie milowe, artefakty, kto kiedy i gdzie

Opis projektu
Funkcjonalności
Architektura
Organizacja pracy - kamienie milowe, scrum

# Co chcemy zrobić:
Aplikacja webowa działająca w kontenerze Docker (zapisana w Github), w wirtualnej sieci Azure, z bazą danych (?), weryfikacja użytkownika przez Azure Key Vault.
Azure Cognitive Services (OCR, Form Recogniser) do obsługi plików wejściowych i inne serwisy z Azure Networking Services.

# Funkcjonalności:
Utworzenie konta użytwnika
Obługa logowania i przechowywania plików wcześniej przetwarzanych
Wgranie pliku wejściowego - zdjęcia/pdf z danymi tekstowymi w formie graficznej
Wyświetlenie tesktu rozpoznanego z pliku wejściowego

# Harmonogram:
# 23.11.20 - Spotkanie organizacyjne. Opracowanie dokumentacji.
30.11.20 - Zapozanie się z działaniem poszczególnych serwisów Azure używanych w projekcie
07.12.20 - Przygotowanie środowiska - weryfikacja kosztów aplikacji - ustalenie polityk SLA
# 14.12.20 - Przygotowanie mock-up'u aplikacji webowej
21.12.20 - Implementacja bazy danych do przechowywania plików.
# 28.12.20 - Działająca aplikacja webowa, komunikująca się z Azure Cognitive Services, zdolna do wysłania pliku wejściowego i odebrania pliku JSON.
04.01.21 - Formatowanie pliku wyjściowego.
11.01.21 - Implementacja systemu logowania użytkowników.
# 18.01.21 - Finalna wersja aplikacji.
25.01.21 - Testowanie bezpieczeństwa aplikacji. Przygotowanie prezentacji.
# 28.01.21 - Prezentacja projektów




