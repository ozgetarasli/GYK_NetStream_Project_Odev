"""
Sample movie data for Netflix recommendation system
"""

movies = [
    {
        "id": 1,
        "title": "Stranger Things",
        "genres": ["Sci-Fi", "Horror", "Drama"],
        "description": "When a young boy vanishes, a small town uncovers a mystery involving secret experiments, terrifying supernatural forces and one strange little girl.",
        "year": 2016,
        "director": "The Duffer Brothers",
        "rating": 8.7,
        "duration": "50m",
        "image_url": "https://example.com/stranger_things.jpg",
        "features": [0.9, 0.8, 0.7, 0.5, 0.2]  # Example embedding vector for content-based filtering
    },
    {
        "id": 2,
        "title": "The Crown",
        "genres": ["Drama", "History", "Biography"],
        "description": "Based on an award-winning play, this drama follows the life of Queen Elizabeth II from her youth to the present day.",
        "year": 2016,
        "director": "Peter Morgan",
        "rating": 8.6,
        "duration": "58m",
        "image_url": "https://example.com/the_crown.jpg",
        "features": [0.2, 0.9, 0.6, 0.4, 0.7]
    },
    {
        "id": 3,
        "title": "Money Heist",
        "genres": ["Crime", "Drama", "Thriller"],
        "description": "Eight thieves take hostages and lock themselves in the Royal Mint of Spain as a criminal mastermind manipulates the police to carry out his plan.",
        "year": 2017,
        "director": "Álex Pina",
        "rating": 8.3,
        "duration": "70m",
        "image_url": "https://example.com/money_heist.jpg",
        "features": [0.4, 0.3, 0.9, 0.8, 0.1]
    },
    {
        "id": 4,
        "title": "The Witcher",
        "genres": ["Fantasy", "Action", "Adventure"],
        "description": "Geralt of Rivia, a mutated monster-hunter for hire, journeys toward his destiny in a turbulent world where people often prove more wicked than beasts.",
        "year": 2019,
        "director": "Lauren Schmidt Hissrich",
        "rating": 8.2,
        "duration": "60m",
        "image_url": "https://example.com/the_witcher.jpg",
        "features": [0.8, 0.2, 0.5, 0.7, 0.9]
    },
    {
        "id": 5,
        "title": "Breaking Bad",
        "genres": ["Crime", "Drama", "Thriller"],
        "description": "A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine in order to secure his family's future.",
        "year": 2008,
        "director": "Vince Gilligan",
        "rating": 9.5,
        "duration": "49m",
        "image_url": "https://example.com/breaking_bad.jpg",
        "features": [0.3, 0.4, 0.9, 0.7, 0.2]
    },
    {
        "id": 6,
        "title": "Black Mirror",
        "genres": ["Sci-Fi", "Drama", "Thriller"],
        "description": "An anthology series exploring a twisted, high-tech multiverse where humanity's greatest innovations and darkest instincts collide.",
        "year": 2011,
        "director": "Charlie Brooker",
        "rating": 8.8,
        "duration": "60m",
        "image_url": "https://example.com/black_mirror.jpg",
        "features": [0.9, 0.5, 0.6, 0.3, 0.2]
    },
    {
        "id": 7,
        "title": "The Queen's Gambit",
        "genres": ["Drama"],
        "description": "In a 1950s orphanage, a young girl reveals an astonishing talent for chess and begins an unlikely journey to stardom while grappling with addiction.",
        "year": 2020,
        "director": "Scott Frank",
        "rating": 8.6,
        "duration": "60m",
        "image_url": "https://example.com/queens_gambit.jpg",
        "features": [0.1, 0.9, 0.5, 0.3, 0.6]
    },
    {
        "id": 8,
        "title": "Dark",
        "genres": ["Crime", "Drama", "Mystery"],
        "description": "A family saga with a supernatural twist, set in a German town where the disappearance of two young children exposes the relationships among four families.",
        "year": 2017,
        "director": "Baran bo Odar",
        "rating": 8.8,
        "duration": "60m",
        "image_url": "https://example.com/dark.jpg",
        "features": [0.7, 0.6, 0.8, 0.5, 0.4]
    },
    {
        "id": 9,
        "title": "Narcos",
        "genres": ["Biography", "Crime", "Drama"],
        "description": "A chronicled look at the criminal exploits of Colombian drug lord Pablo Escobar, as well as the many other drug kingpins who plagued the country through the years.",
        "year": 2015,
        "director": "Chris Brancato",
        "rating": 8.8,
        "duration": "49m",
        "image_url": "https://example.com/narcos.jpg",
        "features": [0.3, 0.7, 0.9, 0.4, 0.2]
    },
    {
        "id": 10,
        "title": "The Umbrella Academy",
        "genres": ["Action", "Adventure", "Comedy"],
        "description": "A family of former child heroes, now grown apart, must reunite to continue to protect the world.",
        "year": 2019,
        "director": "Steve Blackman",
        "rating": 8.0,
        "duration": "60m",
        "image_url": "https://example.com/umbrella_academy.jpg",
        "features": [0.6, 0.3, 0.5, 0.8, 0.7]
    }
] 