#!/usr/bin/env python3
"""
Random Username Generator
Generates creative usernames with 5-6 words without numbers
Uses multiple free APIs for word generation
"""

import requests
import random
import time
import sys
import json
from typing import List, Optional

class UsernameGenerator:
    """Generate random usernames using various word APIs"""
    
    # Free APIs for word generation
    RANDOM_WORD_API = "https://random-word-api.herokuapp.com/word"
    DATAMUSE_API = "https://api.datamuse.com/words"
    
    # Word categories for themed usernames
    ADJECTIVES = [
        "Cool", "Epic", "Pro", "Super", "Mega", "Ultra", "Legendary", "Supreme",
        "Golden", "Silver", "Diamond", "Royal", "Noble", "Mystic", "Shadow",
        "Cosmic", "Atomic", "Thunder", "Lightning", "Phoenix", "Dragon", "Tiger",
        "Swift", "Brave", "Wild", "Dark", "Bright", "Silent", "Loud", "Fast"
    ]
    
    NOUNS = [
        "Warrior", "Legend", "Master", "King", "Queen", "Hero", "Champion",
        "Knight", "Ninja", "Samurai", "Hunter", "Ranger", "Scout", "Wizard",
        "Mage", "Sage", "Lord", "Chief", "Captain", "Commander", "General",
        "Admiral", "Emperor", "Prince", "Duke", "Baron", "Guardian", "Defender"
    ]
    
    ACTIONS = [
        "Rising", "Flying", "Running", "Jumping", "Fighting", "Dancing", "Singing",
        "Blazing", "Shining", "Glowing", "Roaring", "Howling", "Striking", "Crushing",
        "Smashing", "Breaking", "Building", "Creating", "Winning", "Leading"
    ]
    
    ELEMENTS = [
        "Fire", "Water", "Earth", "Wind", "Ice", "Storm", "Light", "Shadow",
        "Thunder", "Lightning", "Frost", "Flame", "Spark", "Wave", "Stone",
        "Steel", "Iron", "Gold", "Silver", "Crystal", "Plasma", "Energy"
    ]
    
    ANIMALS = [
        "Wolf", "Lion", "Tiger", "Bear", "Eagle", "Hawk", "Falcon", "Dragon",
        "Phoenix", "Griffin", "Panther", "Cobra", "Viper", "Shark", "Raven",
        "Owl", "Fox", "Lynx", "Jaguar", "Leopard", "Cheetah", "Rhino"
    ]
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def get_random_words_from_api(self, count: int = 10) -> List[str]:
        """
        Fetch random words from Random Word API
        
        Args:
            count: Number of words to fetch
            
        Returns:
            List of random words
        """
        try:
            response = self.session.get(
                self.RANDOM_WORD_API,
                params={'number': count},
                timeout=10
            )
            
            if response.status_code == 200:
                words = response.json()
                # Filter out words with numbers or special characters
                clean_words = [w.capitalize() for w in words if w.isalpha() and len(w) >= 3]
                return clean_words
            
        except Exception as e:
            print(f"⚠️  API error: {e}")
        
        return []
    
    def get_related_words(self, word: str, rel_type: str = "syn") -> List[str]:
        """
        Get related words from Datamuse API
        
        Args:
            word: Seed word
            rel_type: Relation type (syn=synonyms, trg=triggers, etc.)
            
        Returns:
            List of related words
        """
        try:
            response = self.session.get(
                self.DATAMUSE_API,
                params={
                    'rel_' + rel_type: word,
                    'max': 10
                },
                timeout=10
            )
            
            if response.status_code == 200:
                words = response.json()
                clean_words = [
                    w['word'].capitalize() 
                    for w in words 
                    if w['word'].isalpha() and len(w['word']) >= 3
                ]
                return clean_words[:5]
            
        except Exception as e:
            print(f"⚠️  API error: {e}")
        
        return []
    
    def generate_local_username(self, word_count: int = 5) -> str:
        """
        Generate username using local word lists
        
        Args:
            word_count: Number of words (5 or 6)
            
        Returns:
            Generated username
        """
        all_words = []
        
        # Pick random words from different categories
        categories = [
            self.ADJECTIVES,
            self.NOUNS,
            self.ACTIONS,
            self.ELEMENTS,
            self.ANIMALS
        ]
        
        # Shuffle categories for variety
        random.shuffle(categories)
        
        for i in range(word_count):
            category = categories[i % len(categories)]
            word = random.choice(category)
            all_words.append(word)
        
        return ''.join(all_words)
    
    def generate_api_username(self, word_count: int = 5) -> Optional[str]:
        """
        Generate username using API words
        
        Args:
            word_count: Number of words (5 or 6)
            
        Returns:
            Generated username or None
        """
        words = self.get_random_words_from_api(word_count * 2)
        
        if len(words) >= word_count:
            # Filter words to reasonable length (3-8 characters)
            filtered = [w for w in words if 3 <= len(w) <= 8]
            
            if len(filtered) >= word_count:
                selected = random.sample(filtered, word_count)
                return ''.join(selected)
        
        return None
    
    def generate_hybrid_username(self, word_count: int = 5) -> str:
        """
        Generate username using both API and local words
        
        Args:
            word_count: Number of words (5 or 6)
            
        Returns:
            Generated username
        """
        username_parts = []
        
        # Try to get some words from API
        api_words = self.get_random_words_from_api(word_count)
        
        # Use local words as fallback
        local_words = []
        all_local = (
            self.ADJECTIVES + self.NOUNS + self.ACTIONS + 
            self.ELEMENTS + self.ANIMALS
        )
        
        # Mix API and local words
        available_words = api_words + random.sample(all_local, word_count * 2)
        
        # Filter and select words
        filtered = [w for w in available_words if w.isalpha() and 3 <= len(w) <= 8]
        
        if len(filtered) >= word_count:
            selected = random.sample(filtered, word_count)
            return ''.join(selected)
        
        # Fallback to local generation
        return self.generate_local_username(word_count)
    
    def generate_themed_username(self, theme: str, word_count: int = 5) -> str:
        """
        Generate themed username
        
        Args:
            theme: Theme name (fantasy, gaming, nature, etc.)
            word_count: Number of words
            
        Returns:
            Themed username
        """
        theme_words = {
            'fantasy': self.ADJECTIVES[:10] + ['Mystic', 'Magic', 'Spell', 'Quest'],
            'gaming': ['Pro', 'Epic', 'Legendary', 'Elite', 'Master', 'Champion'],
            'nature': self.ELEMENTS + self.ANIMALS,
            'warrior': self.ACTIONS + self.NOUNS + ['Battle', 'Combat', 'Fight'],
            'royal': ['Royal', 'Noble', 'King', 'Queen', 'Prince', 'Crown', 'Gold'],
            'tech': ['Cyber', 'Digital', 'Quantum', 'Nano', 'Virtual', 'Matrix'],
            'dark': ['Shadow', 'Dark', 'Night', 'Void', 'Raven', 'Phantom'],
            'light': ['Bright', 'Shine', 'Glow', 'Light', 'Solar', 'Radiant']
        }
        
        base_words = theme_words.get(theme.lower(), self.ADJECTIVES + self.NOUNS)
        all_words = base_words + random.sample(
            self.ADJECTIVES + self.NOUNS + self.ACTIONS, 
            word_count * 2
        )
        
        filtered = [w for w in all_words if w.isalpha()]
        selected = random.sample(filtered, min(word_count, len(filtered)))
        
        return ''.join(selected)
    
    def generate_batch(self, count: int, word_count: int = 5, 
                      method: str = 'hybrid', theme: Optional[str] = None) -> List[str]:
        """
        Generate multiple usernames
        
        Args:
            count: Number of usernames to generate
            word_count: Number of words per username
            method: Generation method (local, api, hybrid, themed)
            theme: Theme for themed generation
            
        Returns:
            List of generated usernames
        """
        usernames = []
        
        print(f"\n🎲 Generating {count} usernames with {word_count} words each...")
        print("-" * 60)
        
        for i in range(count):
            try:
                if method == 'local':
                    username = self.generate_local_username(word_count)
                elif method == 'api':
                    username = self.generate_api_username(word_count)
                    if not username:
                        username = self.generate_local_username(word_count)
                elif method == 'themed' and theme:
                    username = self.generate_themed_username(theme, word_count)
                else:  # hybrid
                    username = self.generate_hybrid_username(word_count)
                
                usernames.append(username)
                print(f"  [{i+1}/{count}] ✅ {username}")
                
                # Small delay for API calls
                if method in ['api', 'hybrid'] and i < count - 1:
                    time.sleep(0.3)
                
            except Exception as e:
                print(f"  [{i+1}/{count}] ❌ Error: {e}")
        
        return usernames


def print_banner():
    """Print application banner"""
    banner = """
╔═══════════════════════════════════════════════╗
║     RANDOM USERNAME GENERATOR                 ║
║     Create unique 5-6 word usernames          ║
║     No numbers, pure words!                   ║
╚═══════════════════════════════════════════════╝
    """
    print(banner)


def print_api_info():
    """Print information about free APIs used"""
    print("\n📡 FREE APIs USED:")
    print("-" * 60)
    print("1. Random Word API")
    print("   URL: https://random-word-api.herokuapp.com")
    print("   Purpose: Generate random English words")
    print("   Rate Limit: Generous, no key required")
    print()
    print("2. Datamuse API")
    print("   URL: https://api.datamuse.com")
    print("   Purpose: Get related words, synonyms")
    print("   Rate Limit: 100,000 requests/day, no key required")
    print("-" * 60)


def main():
    """Main function"""
    print_banner()
    
    generator = UsernameGenerator()
    
    print("\n🎯 GENERATION METHOD:")
    print("1. Local (Fast, uses built-in word lists)")
    print("2. API (Creative, uses online word APIs)")
    print("3. Hybrid (Best of both, recommended)")
    print("4. Themed (Choose a theme)")
    print("5. Show API Info")
    
    method_choice = input("\nSelect method (1-5): ").strip()
    
    if method_choice == "5":
        print_api_info()
        input("\nPress Enter to continue...")
        method_choice = input("\nSelect method (1-4): ").strip()
    
    # Map choice to method
    method_map = {
        '1': 'local',
        '2': 'api',
        '3': 'hybrid',
        '4': 'themed'
    }
    
    method = method_map.get(method_choice, 'hybrid')
    theme = None
    
    if method == 'themed':
        print("\n🎨 AVAILABLE THEMES:")
        print("1. Fantasy (mystic, magic, quest)")
        print("2. Gaming (pro, epic, legendary)")
        print("3. Nature (elements, animals)")
        print("4. Warrior (battle, combat)")
        print("5. Royal (king, noble, crown)")
        print("6. Tech (cyber, digital, quantum)")
        print("7. Dark (shadow, night, phantom)")
        print("8. Light (bright, shine, radiant)")
        
        theme_map = {
            '1': 'fantasy', '2': 'gaming', '3': 'nature', '4': 'warrior',
            '5': 'royal', '6': 'tech', '7': 'dark', '8': 'light'
        }
        
        theme_choice = input("\nSelect theme (1-8): ").strip()
        theme = theme_map.get(theme_choice, 'fantasy')
        print(f"✅ Selected theme: {theme.title()}")
    
    # Word count selection
    print("\n📝 WORD COUNT:")
    print("1. 5 words (shorter)")
    print("2. 6 words (longer)")
    print("3. Random (mix of 5 and 6)")
    
    word_choice = input("\nSelect word count (1-3): ").strip()
    
    if word_choice == '3':
        word_count = random.choice([5, 6])
        print(f"✅ Random: {word_count} words selected")
    else:
        word_count = 6 if word_choice == '2' else 5
    
    # Quantity
    try:
        count = int(input("\nHow many usernames to generate (1-100): ").strip())
        count = max(1, min(count, 100))
    except ValueError:
        print("⚠️  Invalid input, generating 10 usernames")
        count = 10
    
    # Generate usernames
    print("\n" + "="*60)
    usernames = generator.generate_batch(count, word_count, method, theme)
    
    # Display results
    print("\n" + "="*60)
    print("📋 GENERATED USERNAMES")
    print("="*60)
    
    for idx, username in enumerate(usernames, 1):
        print(f"{idx:3d}. {username}")
    
    print("\n" + "="*60)
    print(f"✅ Successfully generated {len(usernames)} usernames!")
    print(f"📊 Average length: {sum(len(u) for u in usernames) // len(usernames)} characters")
    print("="*60)
    
    # Save to file option
    save = input("\n💾 Save to file? (y/n): ").lower()
    
    if save == 'y':
        filename = input("Enter filename (default: usernames.txt): ").strip()
        if not filename:
            filename = f"usernames_{int(time.time())}.txt"
        
        if not filename.endswith('.txt'):
            filename += '.txt'
        
        try:
            with open(filename, 'w') as f:
                f.write("GENERATED USERNAMES\n")
                f.write("="*60 + "\n")
                f.write(f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Method: {method.title()}\n")
                if theme:
                    f.write(f"Theme: {theme.title()}\n")
                f.write(f"Word Count: {word_count}\n")
                f.write(f"Total: {len(usernames)}\n")
                f.write("="*60 + "\n\n")
                
                for idx, username in enumerate(usernames, 1):
                    f.write(f"{idx:3d}. {username}\n")
                
                f.write("\n" + "="*60 + "\n")
                f.write("Generated by Random Username Generator\n")
            
            print(f"✅ Saved to: {filename}")
        
        except Exception as e:
            print(f"❌ Error saving file: {e}")
    
    # Statistics
    print("\n📊 STATISTICS:")
    print("-" * 60)
    print(f"Total usernames: {len(usernames)}")
    print(f"Word count: {word_count}")
    print(f"Shortest: {min(usernames, key=len)} ({len(min(usernames, key=len))} chars)")
    print(f"Longest: {max(usernames, key=len)} ({len(max(usernames, key=len))} chars)")
    print("-" * 60)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Operation cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
