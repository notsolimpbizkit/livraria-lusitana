import os
import django
import datetime
import shutil
from pathlib import Path

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'livraria_project.settings')
django.setup()

from books.models import Book, Category
from django.conf import settings

# Get the base directory of the project
BASE_DIR = settings.BASE_DIR

def create_categories():
    """Create basic book categories"""
    categories = [
        {'name': 'Clássicos', 'description': 'Obras clássicas da literatura portuguesa'},
        {'name': 'Poesia', 'description': 'Obras poéticas portuguesas'},
        {'name': 'Teatro', 'description': 'Peças de teatro portuguesas'},
        {'name': 'Romance', 'description': 'Romances portugueses'},
        {'name': 'Ensaio', 'description': 'Ensaios e crítica literária'},
        {'name': 'Contemporâneo', 'description': 'Literatura portuguesa contemporânea'},
        {'name': 'Infantil', 'description': 'Literatura infantil portuguesa'},
        {'name': 'Medieval', 'description': 'Literatura portuguesa medieval'},
        {'name': 'Barroco', 'description': 'Literatura portuguesa do período barroco'},
    ]
    
    created_categories = {}
    for category_data in categories:
        category, created = Category.objects.get_or_create(
            name=category_data['name'],
            defaults={'description': category_data['description']}
        )
        created_categories[category_data['name']] = category
        if created:
            print(f"Categoria criada: {category.name}")
        else:
            print(f"Categoria já existe: {category.name}")
    
    return created_categories

def add_books(categories):
    """Add books to the database"""
    books_data = [
        {
            'title': 'Os Lusíadas',
            'author': 'Luís Vaz de Camões',
            'isbn': '9789720727602',
            'synopsis': 'Os Lusíadas contam a história da viagem do caminho marítimo para a Índia por Vasco da Gama na época dos Descobrimentos, mas é muito mais do que isso. Carregada de simbolismo e de um claro orgulho patriótico, esta narrativa exalta os vários desafios superados pelo Herói – o Povo Português – cuja coragem e dedicação são inabaláveis, mesmo contra todas as adversidades.',
            'price_cents': 3000,
            'publication_date': datetime.date(2021, 9, 1),
            'publisher': 'Porto Editora',
            'language': 'Português',
            'dimensions': '128 x 198 x 21 mm',
            'binding_type': 'Capa mole',
            'pages': 304,
            'category_name': 'Clássicos',
            'stock': 15
        },
        {
            'title': 'Mensagem',
            'author': 'Fernando Pessoa',
            'isbn': '9789720726599',
            'synopsis': 'Originalmente intitulada Portugal, a única obra de Fernando Pessoa publicada em vida continua tão atual no século XXI como em 1934. Revisitando o passado - os heróis e as conquistas da História - encontramos uma mensagem para o futuro, porque hoje: Tudo é incerto e derradeiro. Tudo é disperso, nada é inteiro. Ó Portugal, hoje és nevoeiro… É a Hora!',
            'price_cents': 885,
            'publication_date': datetime.date(2016, 1, 1),
            'publisher': 'Porto Editora',
            'language': 'Português',
            'dimensions': '128 x 198 x 7 mm',
            'binding_type': 'Capa mole',
            'pages': 96,
            'category_name': 'Poesia',
            'stock': 20
        },
        {
            'title': 'Os Maias',
            'author': 'Eça de Queirós',
            'isbn': '9789720727251',
            'synopsis': 'Na pequenez da Baixa e do Aterro, onde todos se acotovelam, os dois fatalmente se cruzam: e com o seu brilho pessoal, muito fatalmente se atraem! Há nada mais natural? Se ela fosse feia e trouxesse aos ombros uma confeção barata da Loja da América, se ele fosse um mocinho encolhido de chapéu-coco, nunca se notariam e seguiriam diversamente nos seus destinos diversos. Assim, o conhecerem-se era certo, o amarem-se era provável… Nem só das histórias de amor dos Maias vive o romance mais completo e brilhante de Eça de Queirós.',
            'price_cents': 1110,
            'publication_date': datetime.date(2016, 1, 1),
            'publisher': 'Porto Editora',
            'language': 'Português',
            'dimensions': '128 x 198 x 40 mm',
            'binding_type': 'Capa mole',
            'pages': 736,
            'category_name': 'Clássicos',
            'stock': 10
        },
        {
            'title': 'Memorial do Convento',
            'author': 'José Saramago',
            'isbn': '9789720745989',
            'synopsis': 'No século XVIII, enquanto D. João V mandava construir o convento de Mafra, Baltasar e Blimunda encontravam-se, e o padre Bartolomeu de Gusmão procurava maneiras de voar. A história que aqui se conta não está nos livros de história, quase como se as memórias de um amor entre dois seres humanos comuns, mas invulgares, pudesse ser mais duradoura e mais impressionante que as memórias da construção de um enorme convento.',
            'price_cents': 1590,
            'publication_date': datetime.date(2019, 6, 1),
            'publisher': 'Porto Editora',
            'language': 'Português',
            'dimensions': '128 x 198 x 28 mm',
            'binding_type': 'Capa mole',
            'pages': 392,
            'category_name': 'Romance',
            'stock': 12
        },
        {
            'title': 'Frei Luís de Sousa',
            'author': 'Almeida Garrett',
            'isbn': '9789720731968',
            'synopsis': 'Uma das obras maiores do teatro português, Frei Luís de Sousa conta uma história de desencontros, reencontros, espera, conflitos morais e religiosos, com um desfecho dramático. A descrição do ambiente de aparente normalidade, de início, vai dando lugar a uma crescente tensão dramática, onde questões históricas como o sebastianismo, o domínio filipino, e também os traumas daí resultantes, vão surgindo como um fundo que dá maior intensidade aos dilemas dos personagens.',
            'price_cents': 755,
            'publication_date': datetime.date(2021, 7, 1),
            'publisher': 'Porto Editora',
            'language': 'Português',
            'dimensions': '128 x 198 x 9 mm',
            'binding_type': 'Capa mole',
            'pages': 144,
            'category_name': 'Teatro',
            'stock': 8
        },
        {
            'title': 'O Ano da Morte de Ricardo Reis',
            'author': 'José Saramago',
            'isbn': '9789720736437',
            'synopsis': 'Em 1936, Ricardo Reis - um dos heterónimos de Fernando Pessoa - decide regressar a Portugal após dezasseis anos no Brasil. Regressa a Lisboa para encontrar um país oprimido pela ditadura e para se confrontar com a morte do seu criador. Perdido, estranhando uma cidade que já não reconhece, procura recuperar uma identidade e reconstruir uma vida que, na verdade, nunca foi a sua. Neste extraordinário romance de busca e de fantasmas, Saramago convida-nos também a um exercício de reflexão sobre a relação entre o criador e a criatura.',
            'price_cents': 1590,
            'publication_date': datetime.date(2020, 7, 30),
            'publisher': 'Porto Editora',
            'language': 'Português',
            'dimensions': '128 x 198 x 26 mm',
            'binding_type': 'Capa mole',
            'pages': 424,
            'category_name': 'Romance',
            'stock': 7
        },
        {
            'title': 'Livro do Desassossego',
            'author': 'Fernando Pessoa',
            'isbn': '9789720732033',
            'synopsis': 'Um dos textos mais importantes e enigmáticos de Fernando Pessoa, o Livro do Desassossego é um projeto inacabado e fragmentário, escrito sob o heterónimo de Bernardo Soares. Apresenta reflexões profundas sobre a existência, a identidade, o tédio e a melancolia da vida moderna, compondo um diário íntimo de sensações e pensamentos.',
            'price_cents': 1420,
            'publication_date': datetime.date(2019, 11, 13),
            'publisher': 'Porto Editora',
            'language': 'Português',
            'dimensions': '128 x 198 x 30 mm',
            'binding_type': 'Capa mole',
            'pages': 496,
            'category_name': 'Clássicos',
            'stock': 9
        },
        {
            'title': 'Auto da Barca do Inferno',
            'author': 'Gil Vicente',
            'isbn': '9789720728845',
            'synopsis': 'Na Barca do Inferno, o Diabo e o seu companheiro preparam uma viagem, para a qual vão embarcar diversas personagens. Umas, pela sua conduta, estão já condenadas, outras reúnem-se com o Anjo, que levará os justos para a Glória, "terra que dá pão". Estas personagens são a representação da sociedade do tempo - membros do clero, da nobreza, do povo, e figuras cujo comportamento Gil Vicente pretendia criticar ou elogiar.',
            'price_cents': 790,
            'publication_date': datetime.date(2021, 4, 1),
            'publisher': 'Porto Editora',
            'language': 'Português',
            'dimensions': '128 x 198 x 8 mm',
            'binding_type': 'Capa mole',
            'pages': 112,
            'category_name': 'Teatro',
            'stock': 15
        },
        {
            'title': 'Sermões',
            'author': 'Padre António Vieira',
            'isbn': '9789720728067',
            'synopsis': 'Os Sermões do Padre António Vieira são considerados a obra-prima da oratória barroca em língua portuguesa. Com grande engenho e extraordinário domínio da linguagem, Vieira utiliza os sermões para criticar os costumes da sociedade do seu tempo e defender causas como a liberdade dos índios no Brasil.',
            'price_cents': 1250,
            'publication_date': datetime.date(2018, 5, 15),
            'publisher': 'Porto Editora',
            'language': 'Português',
            'dimensions': '128 x 198 x 25 mm',
            'binding_type': 'Capa mole',
            'pages': 312,
            'category_name': 'Barroco',
            'stock': 6
        },
        {
            'title': 'Cartas Portuguesas',
            'author': 'Mariana Alcoforado',
            'isbn': '9789720728883',
            'synopsis': 'As Cartas Portuguesas são uma coleção de cinco cartas apaixonadas, atribuídas à freira portuguesa Mariana Alcoforado, que expressam o sofrimento amoroso pela separação do seu amante, um oficial francês. Este conjunto de cartas representa um importante documento do Barroco português e é considerado uma das mais belas expressões literárias do amor não correspondido.',
            'price_cents': 850,
            'publication_date': datetime.date(2019, 2, 10),
            'publisher': 'Assírio & Alvim',
            'language': 'Português',
            'dimensions': '130 x 200 x 10 mm',
            'binding_type': 'Capa mole',
            'pages': 96,
            'category_name': 'Barroco',
            'stock': 8
        },
        {
            'title': 'Carta de Guia de Casados',
            'author': 'D. Francisco Manuel de Melo',
            'isbn': '9789720730206',
            'synopsis': 'Publicado em 1651, este é um texto didático que pretende ensinar os maridos a conviver com as suas esposas. Embora reflita ideias sobre o casamento e a condição feminina próprias do século XVII, é também um documento importante para entender as relações conjugais na sociedade barroca portuguesa.',
            'price_cents': 980,
            'publication_date': datetime.date(2017, 8, 5),
            'publisher': 'Porto Editora',
            'language': 'Português',
            'dimensions': '128 x 198 x 15 mm',
            'binding_type': 'Capa mole',
            'pages': 160,
            'category_name': 'Barroco',
            'stock': 7
        },
    ]
    
    # Ensure media directory exists
    media_root = Path(settings.MEDIA_ROOT)
    os.makedirs(media_root, exist_ok=True)
    
    # Create directory for book images
    books_dir = media_root / 'books'
    os.makedirs(books_dir, exist_ok=True)
    
    # Create or check for placeholder image
    placeholder_dir = Path(BASE_DIR) / 'static' / 'images'
    os.makedirs(placeholder_dir, exist_ok=True)
    
    placeholder_path = placeholder_dir / 'book_placeholder.jpg'
    
    # If placeholder doesn't exist, create a simple one
    if not placeholder_path.exists():
        try:
            # Try to create a very simple placeholder image using Python
            # This requires Pillow (PIL) library
            try:
                from PIL import Image, ImageDraw
                
                # Create a simple placeholder image (200x300 pixels)
                img = Image.new('RGB', (200, 300), color='#f5f2e9')
                d = ImageDraw.Draw(img)
                d.rectangle([(10, 10), (190, 290)], outline='#8b5e3b', width=2)
                d.text((35, 140), "Livraria Lusitana", fill='#8b5e3b')
                d.text((60, 160), "Livro", fill='#8b5e3b')
                
                img.save(placeholder_path)
                print(f"Placeholder image created at {placeholder_path}")
            except ImportError:
                print("Pillow not installed. Cannot create placeholder image.")
                print("Please add a placeholder image to static/images/book_placeholder.jpg")
        except Exception as e:
            print(f"Could not create placeholder: {str(e)}")
            print("Please add a placeholder image to static/images/book_placeholder.jpg")
    
    # Add books
    for book_data in books_data:
        # Get category
        category = categories.get(book_data['category_name'])
        if not category:
            print(f"Categoria não encontrada: {book_data['category_name']}")
            continue
        
        # Check if book already exists
        if Book.objects.filter(isbn=book_data['isbn']).exists():
            print(f"Livro já existe: {book_data['title']}")
            continue
        
        # Create book
        book = Book(
            isbn=book_data['isbn'],
            title=book_data['title'],
            author=book_data['author'],
            synopsis=book_data['synopsis'],
            price_cents=book_data['price_cents'],
            publication_date=book_data['publication_date'],
            publisher=book_data['publisher'],
            language=book_data['language'],
            dimensions=book_data['dimensions'],
            binding_type=book_data['binding_type'],
            pages=book_data['pages'],
            stock=book_data['stock'],
            category=category
        )
        
        # Save the book to generate an ID
        book.save()
        
        # Add the placeholder image
        try:
            if placeholder_path.exists():
                # Destination path for the book image
                dest_filename = f"{book_data['isbn']}.jpg"
                dest_path = books_dir / dest_filename
                
                # Copy the placeholder to the book's image path
                shutil.copy(placeholder_path, dest_path)
                
                # Set the image field with the relative path
                book.image = f'books/{dest_filename}'
                book.save()
                print(f"Imagem aplicada para: {book_data['title']}")
            else:
                print(f"Placeholder não encontrado. Livro {book_data['title']} sem imagem.")
        except Exception as e:
            print(f"Erro ao processar imagem para {book_data['title']}: {str(e)}")
        
        print(f"Livro adicionado: {book.title}")

if __name__ == "__main__":
    print("Iniciando importação de livros...")
    categories = create_categories()
    add_books(categories)
    print("Importação concluída!")