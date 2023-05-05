# Projekt-Sudoku_solver
#Úvod
Tato projektová dokumentace se bude zabývat implementací dvou různých programů. První program slouží k řešení sudoku a druhý klasifikuje ručně psané číslice pomocí neuronové sítě.

##Co program dělá
Tento program slouží k řešení sudoku. Program využívá backtracking algoritmus, který postupně prochází všechna políčka na hrací desce a snaží se nalézt vhodné číslo, které ještě není na řádku, sloupci ani v boxu. Program získává zadání sudoku ve formě dvourozměrného pole, kde nula reprezentuje prázdné pole. Pokud se program nedokáže dále posunout, tak vrátí výsledek.

##Popis použitých technologií
Technologie použité v programu řešícím Sudoku jsou Python a knihovna TensorFlow pro neuronové sítě.

Python je programovací jazyk použitý pro samotné řešení sudoku. Jedná se o vysokoúrovňový jazyk, který je snadno čitelný a psaní kódu je rychlé a efektivní. Python nabízí širokou škálu knihoven, které usnadňují implementaci programu.

TensorFlow je knihovna pro strojové učení. Používá se pro tvorbu a trénování neuronových sítí, kdy je vstupní data možné transformovat a použít k predikci. V tomto případě byla knihovna TensorFlow použita k trénování neuronové sítě, která má schopnost klasifikovat ručně psaná čísla na obrázcích. Výsledný model sítě byl uložen a použit pro klasifikaci čísel v Sudoku.

Dále byla použita knihovna OpenCV pro zpracování obrázků s čísly v Sudoku. Tato knihovna poskytuje mnoho funkcí pro práci s obrázky, jako jsou načítání, převod do šedotónového formátu, filtrace, segmentace, zvýraznění hran a mnoho dalšího. Pomocí knihovny OpenCV byly načteny obrázky čísel z Sudoku, které byly následně použity pro klasifikaci.

V programu byla také použita knihovna matplotlib pro vizualizaci výsledků. Pomocí této knihovny byly zobrazeny obrázky čísel z Sudoku spolu s predikovanými hodnotami. Dále byla knihovna scikit-learn použita pro výpočet přesnosti klasifikace a matice záměn. Tyto statistické údaje jsou užitečné pro hodnocení výkonnosti neuronové sítě.

##Stručný popis jak to funguje uvnitř
Vstupem programu je matice s čísly, které reprezentují vstupní sudoku. Tyto čísla mohou být z části vyplněna nebo mohou být všechna rovna 0. Pokud je číslo rovno 0, pak se jedná o prázdné políčko, které je potřeba vyplnit.

Program prochází prázdná políčka a postupně do nich vkládá čísla od 1 do 9. Poté ověří, zda je dané číslo platné, tzn. že se v řádku, sloupci a 3x3 bloku nevyskytuje žádné jiné stejné číslo. Pokud je číslo platné, program pokračuje v rekurzi a postupně vyplňuje další prázdná políčka. Pokud program nenalezne řešení, tak se vrací zpět a vyzkouší jiné číslo.

Funkce ‘find_empty’(sudo) prochází celou matici a hledá prázdné políčko. Pokud nalezne prázdné políčko, tak vrátí jeho souřadnice. Pokud žádné prázdné políčko nenalezne, tak vrátí hodnotu None.

Funkce ‘valid(sudo, num, pos)’ ověřuje, zda je dané číslo platné na daných souřadnicích (pos) v matici (sudo). Nejprve ověřuje, zda se číslo v daném řádku již nevyskytuje. Pokud se tam již vyskytuje, tak vrátí False. Stejně tak ověří, zda se číslo nevyskytuje v daném sloupci nebo v 3x3 bloku. Pokud se číslo nikde jinde v matici nevyskytuje, tak je číslo platné a funkce vrátí True.

Funkce ‘solve(sudo)’ postupně volá funkci ‘find_empty(sudo)’, dokud nevyplní celou matici. Pokud je celá matici vyplněna, tak vrátí hodnotu True. Pokud není celá matici vyplněna, tak najde první prázdné políčko a postupně do něj vkládá čísla od 1 do 9. Pokud nějaké číslo není platné, tak se vrací zpět a zkouší jiné číslo.

Dále v programu je část, která načítá a klasifikuje obrázky. Program využívá knihovny Tensorflow a OpenCV pro načítání a úpravu obrázků, Keras pro tvorbu a trénování sítě a scikit-learn pro evaluaci výsledků. 

Program začíná načtením datasetu MNIST, což je soubor různých ručně psaných číslic. Dataset se následně normalizuje a převede na pole atributů. Z těchto dat se vytvoří model neuronové sítě pomocí knihovny Keras, který obsahuje několik vrstev konvolučních a plně propojených neuronů. Síť se trénuje na těchto datech po dobu 10 epoch a výsledný model se uloží do souboru s názvem 'handwritten.model'.

Když je načten uložený model, program využívá OpenCV pro načtení obrázků. Následně se každý obrázek převede na pole pixelů, které odpovídá formátu datasetu MNIST, a tak lze na něj aplikovat neuronovou síť. Síť pak predikuje číslo na obrázku a výsledek se uloží do seznamu. Pokud program zpracuje všechny obrázky, seznam se převede na matici 9x9.

Celkově tedy program funguje následovně: nejprve se načtou a předzpracují trénovací data, poté se vytvoří model sítě, síť se natrénuje, a nakonec se pomocí této sítě rozpoznávají obrázky ručně psaných čísel a výsledek je zapsán do matice 9x9.

##Návod na použití projektu
Projekt je implementován v jazyce Python. Pro použití projektu je nutné mít nainstalované Python 3.0 nebo novější a následující knihovny: OpenCV, TensorFlow, Matplotlib, Numpy a Scikit-learn.

###Použití projektu je následující:
Ručně nakreslete nebo stáhněte písmena, která se budou dosazovat do herního pole. Projekt je optimalizován pro rozpoznávání ručně psaných čísel v rozlišení 28x28 pixelů. Proto je důležité dodržet následující doporučení při vytváření vstupních obrázků: velikost obrázku musí být 28x28 pixelů, čísla musí být psána tmavou barvou na bílém pozadí. 
Otevřete příkazový řádek a přejděte do adresáře, ve kterém se nachází soubory pro sudoku solver.
Program spustíte příkazem: py main.py
Po spuštění programu se vám ukáže grafické rozhraní sudoku.
Pokud by čísla, která se v sudoku zobrazí neseděla s těmi ručně psanými, můžete je změnit kliknutím na políčko, ve kterém se nachází a následným zmáčknutím klávesy 1 - 9. Kdyby jste chtěli dané číslo odstranit klikněte na tlačítko ‘backspace’.
Jestliže všechna písmena sedí a je možné sudoku vyřešit zpáškněte klávesu ‘space’ a na herní ploše se automaticky zobrazí správné řešení. Pokud sudoku nebyli možno vyřešit program spadne a je nutné ho spustit znova.

##Možný rozvoj v budoucnu/popis reálného využití projektu
V programu by mohlo být vylepšena přesnost rozpoznávání číslic pomocí strojového učení, zejména využití rozšířené reality. Díky rozšířené realitě by bylo možné načíst fotografii sudoku a pomocí kamery na mobilním zařízení nebo jiného zařízení s kamerou zobrazit výsledek řešení sudoku. Další možností rozšíření projektu může být vylepšení grafického rozhraní a zajistit, aby při zadání inputu, který nejde vyřešit program nepřestal fungovat. Další rozšíření by mohlo být možnost vybrat obtížnost nebo velikost sudoku a program by pak vrátil sudoku s určitou velikostí a obtížností.









