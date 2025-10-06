# Random Username Generator

Unique usernames composed of 5-6 words without any numbers. Uses multiple free APIs and built-in word lists to create memorable usernames perfect for gaming, social media, or any platform.

## 🌟 Features

✨ **Multiple Generation Methods**
- **Local**: Fast generation using built-in word lists
- **API**: Creative generation using online word APIs
- **Hybrid**: Best of both worlds (recommended)
- **Themed**: Generate usernames based on specific themes

🎯 **Customization Options**
- Choose 5 or 6 word usernames
- 8 different themes available
- Batch generation (1-100 usernames at once)
- No numbers, pure words only

📡 **Free APIs Used**
- Random Word API (no key required)
- Datamuse API (no key required)

💾 **Export Features**
- Save results to text file
- Detailed statistics
- Timestamped outputs

## 📋 Requirements

- Python 3.6 or higher
- `requests` library

## 🚀 Installation

1. **Navigate to the directory**

```bash
gitclone https://github.com/Hajjouz/generate-username
```

2. **Install dependencies**

```bash
pip install requests
```

Or using requirements file:

```bash
pip install -r requirements.txt
```

## 💡 Usage

### Basic Usage

Run the script:

```bash
python3 generate.py
```

### Generation Methods

#### 1. Local Generation (Fast)
Uses built-in word lists for instant generation.

**Pros:**
- Very fast (no network calls)
- Always works offline
- Consistent results

**Cons:**
- Limited variety
- Same word pool

**Example output:**
```
CoolWarriorFlyingFireWolf
EpicHeroRunningShadowTiger
LegendaryMasterBlazeGoldenEagle
```

#### 2. API Generation (Creative)
Uses online APIs to fetch random words.

**Pros:**
- Highly creative
- Endless variety
- Unique combinations

**Cons:**
- Requires internet
- Slightly slower
- API dependent

**Example output:**
```
SwiftMountainRiverStormSky
BraveForestOceanThunderCloud
WildDesertValleyCrystalWind
```

#### 3. Hybrid Generation (Recommended)
Combines both methods for optimal results.

**Pros:**
- Best of both worlds
- Good variety
- Reliable fallback

**Example output:**
```
MysticDragonPhoenixCosmicThunder
SilentHunterRapidGoldenFalcon
BrightChampionFierceRoyalLion
```

#### 4. Themed Generation
Generate usernames based on specific themes.

**Available Themes:**
- **Fantasy**: Mystic, Magic, Quest, Spell
- **Gaming**: Pro, Epic, Legendary, Elite
- **Nature**: Elements, Animals, Natural forces
- **Warrior**: Battle, Combat, Fight, Strike
- **Royal**: King, Noble, Crown, Prince
- **Tech**: Cyber, Digital, Quantum, Virtual
- **Dark**: Shadow, Night, Phantom, Void
- **Light**: Bright, Shine, Radiant, Solar

**Example themed outputs:**

Fantasy:
```
MysticQuestMagicSpellDragon
EnchantedWizardMysticPhoenix
```

Gaming:
```
ProEpicLegendaryEliteMaster
ChampionSupremeMegaUltra
```

Tech:
```
CyberDigitalQuantumMatrix
VirtualPlasmaAtomicNano
```

## 📖 Step-by-Step Tutorial

### Example Session 1: Quick Generation

```
Select method (1-5): 3
✅ Selected: Hybrid

Select word count (1-3): 1
✅ 5 words selected

How many usernames to generate (1-100): 10

🎲 Generating 10 usernames with 5 words each...
------------------------------------------------------------
  [1/10] ✅ SwiftGoldenEagleFlying
  [2/10] ✅ BraveDragonFireStorm
  [3/10] ✅ MysticShadowHunter
  ...

💾 Save to file? (y/n): y
Enter filename: my_usernames.txt
✅ Saved to: my_usernames.txt
```

### Example Session 2: Themed Generation

```
Select method (1-5): 4
✅ Selected: Themed

Select theme (1-8): 1
✅ Selected theme: Fantasy

Select word count (1-3): 2
✅ 6 words selected

How many usernames to generate: 5

🎲 Generating 5 usernames with 6 words each...
------------------------------------------------------------
  [1/5] ✅ MysticMagicQuestDragonEnchanted
  [2/5] ✅ PhoenixWizardSpellLegendaryMystic
  ...
```

## 🔧 Advanced Usage

### Use as Python Module

You can import and use the generator in your own scripts:

```python
from username_generator import UsernameGenerator

# Create generator instance
generator = UsernameGenerator()

# Generate single username
username = generator.generate_local_username(word_count=5)
print(username)  # CoolWarriorFireDragon

# Generate themed username
username = generator.generate_themed_username('gaming', 6)
print(username)  # ProEpicLegendaryChampionMasterElite

# Generate batch
usernames = generator.generate_batch(
    count=20,
    word_count=5,
    method='hybrid'
)

# Generate with specific theme
usernames = generator.generate_batch(
    count=10,
    word_count=6,
    method='themed',
    theme='fantasy'
)
```

### Custom Word Lists

You can extend the built-in word lists:

```python
generator = UsernameGenerator()

# Add custom words
generator.ADJECTIVES.extend(['Awesome', 'Amazing', 'Incredible'])
generator.NOUNS.extend(['Titan', 'Deity', 'Immortal'])

# Generate with custom words
username = generator.generate_local_username(5)
```

## 📡 Free APIs Information

### 1. Random Word API

**URL**: https://random-word-api.herokuapp.com

**Features:**
- Generates random English words
- No API key required
- No rate limiting (reasonable use)
- Returns JSON array

**Example Request:**
```bash
curl "https://random-word-api.herokuapp.com/word?number=5"
# Returns: ["dragon", "swift", "mystic", "brave", "storm"]
```

**Documentation**: Available at the API URL

---

### 2. Datamuse API

**URL**: https://api.datamuse.com

**Features:**
- Word-finding query engine
- Get synonyms, related words
- No API key required
- Rate limit: 100,000 requests/day
- Free for all uses

**Example Request:**
```bash
curl "https://api.datamuse.com/words?rel_syn=warrior"
# Returns related words to "warrior"
```

**Documentation**: https://www.datamuse.com/api/

**Use Cases:**
- Find synonyms: `?rel_syn=word`
- Find triggers: `?rel_trg=word`
- Find rhymes: `?rel_rhy=word`
- Find similar: `?ml=word`

---

### API Comparison

| Feature | Random Word API | Datamuse API |
|---------|----------------|--------------|
| **Cost** | Free | Free |
| **API Key** | Not required | Not required |
| **Rate Limit** | Generous | 100k/day |
| **Response** | Simple array | Detailed JSON |
| **Speed** | Fast | Fast |
| **Reliability** | High | Very High |

## 📊 Output Examples

### Sample Generated Usernames (5 words)

```
1. SwiftGoldenEagleFire
2. BraveDragonStormShadow
3. MysticPhoenixThunderLight
4. WildLionFrostCrystal
5. EpicWolfBlazeRoyal
6. SilentHawkFlameNoble
7. RapidTigerSparkShine
8. FierceCobraWaveDiamond
9. MightyBearWindIron
10. ProudFalconBoltSupreme
```

### Sample Generated Usernames (6 words)

```
1. LegendaryChampionCrystalPhoenixGoldenThunder
2. SupremeWarriorMysticDragonFireStorm
3. UltimateHeroNobleEagleSilverLight
4. CosmicMasterRoyalTigerDiamondBlaze
5. AtomicKnightShadowWolfBrightFlame
```

### Themed Examples

**Fantasy Theme:**
```
MysticQuestEnchantedDragonSpell
MagicWizardPhoenixLegendaryMystic
SorcererMysticQuestMagicDragon
```

**Gaming Theme:**
```
ProEpicLegendaryChampionMaster
EliteSupremeMegaUltraKing
ChampionProEpicLegendaryElite
```

**Nature Theme:**
```
FireWaterEarthWindStorm
ThunderLightningFrostFlameWave
OceanMountainForestRiverSky
```

## 💾 Output File Format

When saving to file, the format is:

```
GENERATED USERNAMES
============================================================
Generated: 2025-10-06 14:30:45
Method: Hybrid
Word Count: 5
Total: 20
============================================================

  1. SwiftGoldenEagleFire
  2. BraveDragonStormShadow
  3. MysticPhoenixThunderLight
  ...
 20. ProudFalconBoltSupreme

============================================================
Generated by Random Username Generator
```

## 🎮 Use Cases

### Gaming Platforms
Perfect for:
- Xbox Gamertags
- PlayStation IDs
- Steam usernames
- Discord names
- Roblox (check availability separately)
- Minecraft usernames

### Social Media
Great for:
- Twitter handles (if available)
- Instagram usernames
- TikTok names
- YouTube channels
- Twitch streamers

### Professional
Can be used for:
- Brand names
- Project codenames
- Avatar names
- Character names (RPG games)
- Pet names
- Team names

## ⚙️ Configuration

### Modify Word Count Range

Edit the script to allow different word counts:

```python
# In generate_batch function
word_count = random.randint(4, 7)  # 4-7 words instead of 5-6
```

### Adjust Character Length Filter

Change the word length filter:

```python
# In generate_api_username function
filtered = [w for w in words if 2 <= len(w) <= 10]  # Allow 2-10 char words
```

### Add API Delay

Increase delay for slower connections:

```python
# In generate_batch function
time.sleep(1.0)  # 1 second delay instead of 0.3
```

## 🐛 Troubleshooting

### Issue: API timeout errors

```
⚠️  API error: Connection timeout
```

**Solution:**
- Check internet connection
- Use "Local" method instead
- Try again later
- Increase timeout in code:

```python
response = self.session.get(url, timeout=30)  # Increase from 10 to 30
```

### Issue: No words returned from API

```
⚠️  API error: Empty response
```

**Solution:**
- API might be down
- Use "Local" or "Hybrid" method
- Script will automatically fallback to local words

### Issue: Generated names too long

**Solution:**
- Use 5 words instead of 6
- Modify character length filter in code
- Use words with fewer characters

### Issue: Not creative enough

**Solution:**
- Use "API" or "Hybrid" method
- Try different themes
- Generate larger batches and pick favorites

## 📈 Statistics & Performance

### Generation Speed

| Method | Speed (usernames/sec) | Network Required |
|--------|----------------------|------------------|
| Local | ~1000 | No |
| API | ~2-3 | Yes |
| Hybrid | ~3-5 | Yes (preferred) |
| Themed | ~500 | No |

### Average Length

- **5 words**: 25-35 characters
- **6 words**: 30-45 characters

### Character Distribution

- Typical range: 20-50 characters
- Average: 32 characters
- Suitable for most platforms (under 50 char limit)

## 🔒 Privacy & Ethics

✅ **What this tool does:**
- Generates random word combinations
- Uses public, free APIs
- Creates unique usernames

❌ **What this tool doesn't do:**
- Check username availability on platforms
- Register accounts
- Store any user data
- Send data to third parties

⚠️ **Usage Guidelines:**
- Use generated names ethically
- Check availability before using
- Respect platform terms of service
- Don't use for spam or abuse

## 🤝 Contributing

Contributions welcome! Ideas:
- Add more word categories
- Integrate more free APIs
- Add more themes
- Improve word filtering
- Add language support

## 📝 License

This tool is provided as-is for personal and educational use.

## 🆘 Support

If you encounter issues:

1. Check internet connection (for API methods)
2. Verify Python version (3.6+)
3. Update requests library: `pip install --upgrade requests`
4. Try "Local" method if APIs fail
5. Check API status manually

## 🎯 Tips for Best Results

1. **Use Hybrid method** for best creativity
2. **Try different themes** to match your style
3. **Generate 20-50 names** and pick favorites
4. **Combine themes** by editing word lists
5. **Save results** for future reference
6. **Check availability** on target platform before committing

## 📚 Additional Resources

### More Free Word APIs

- **Wordnik API**: https://developer.wordnik.com/ (requires free API key)
- **Words API**: https://www.wordsapi.com/ (free tier available)
- **Oxford Dictionaries API**: https://developer.oxforddictionaries.com/ (free tier)

### Related Tools

- Roblox Username Checker (included in this repo)
- Name availability checkers
- Domain name generators

---

**Happy Username Generating! 🎮**

Created for creative minds who need unique, memorable usernames.
