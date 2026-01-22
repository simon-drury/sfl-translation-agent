# SFL Translation Agent

A linguistically-informed translation system based on Systemic Functional Linguistics (SFL) principles, designed to preserve semantic fidelity, register appropriateness, and cultural context across multiple languages.

## Overview

This translation agent leverages SFL theory to analyze and transform text between languages while maintaining meaning at three metafunctional levels:

- **Ideational**: Preserving experiential content and logical relationships
- **Interpersonal**: Maintaining register, tenor, and evaluative stance
- **Textual**: Ensuring coherence, cohesion, and information flow

Unlike surface-level machine translation, this agent performs deep semantic analysis to ensure that translations reflect not just lexical equivalents, but functionally equivalent meanings adapted to target language and culture.

## Core Features

### Semantic Fidelity
- Transitivity-aware translation (preserving process types, participants, and circumstances)
- Mood and modality preservation across languages
- Theme-rheme structure adaptation for target language norms

### Register Adaptation
- Automatic register detection and appropriate translation (formal/informal, technical/lay)
- Field-specific terminology handling
- Tenor adjustment based on power and solidarity relationships

### Multilingual Support

Supported languages include:
- **European**: English, French, German, Spanish, Italian, Portuguese
- **Asian**: Mandarin Chinese, Japanese, Korean
- **Additional**: Arabic, Russian, Hindi

### Translation Modes

1. **Standard Translation**  
   General-purpose translation with semantic fidelity

2. **Register-Matched Translation**  
   Explicit register control (academic, business, conversational, technical)

3. **Cultural Localization**  
   Adaptation of idioms, cultural references, and pragmatic markers

4. **Back-Translation Quality Check**  
   Automated validation via round-trip translation analysis

## Technical Architecture

### SFL Analysis Pipeline

```
Source Text
  → Tokenization & Parsing
  → SFL Feature Extraction
     - Transitivity analysis
     - Mood & modality detection
     - Theme-rheme structure
     - Cohesive resources (reference, ellipsis, conjunction, lexical cohesion)
  → Semantic Representation (metafunction vectors)
  → Cross-Linguistic Mapping
  → Target Language Generation
     - Register-appropriate lexis
     - Target-language grammar
     - Culturally appropriate forms
  → Post-processing & Validation
```

### Integration Methods

**Standalone Mode**
```python
from sfl_translation import SFLTranslator

translator = SFLTranslator(
    source_lang='en',
    target_lang='fr',
    register='formal'
)

result = translator.translate(
    text="The committee will review the proposal next week.",
    preserve_register=True,
    cultural_adaptation=True
)

print(result.translation)
print(result.sfl_analysis)  # Detailed linguistic breakdown
```

**Agent Mode (Multiagent Systems)**
```python
from sfl_translation import TranslationAgent

agent = TranslationAgent(
    agent_id="translator-01",
    supported_languages=['en', 'fr', 'de', 'es'],
    mode='orchestrated'
)

agent.register_callback(
    on_translation_complete=route_to_next_agent
)

agent.start()
```

## Installation

```bash
# Clone repository
git clone https://github.com/simon-drury/sfl-translation-agent.git
cd sfl-translation-agent

# Install dependencies
pip install -r requirements.txt

# Optional: Install language-specific models
python setup.py install --lang=all
```

## Usage Examples

### Basic Translation

```python
translator = SFLTranslator('en', 'de')
translation = translator.translate(
    "Machine learning has revolutionized data analysis."
)
# Output: "Maschinelles Lernen hat die Datenanalyse revolutioniert."
```

### Register-Controlled Translation

```python
translator = SFLTranslator('en', 'ja', register='business-formal')
translation = translator.translate(
    "We appreciate your continued support."
)
# Output: "平素より格別のご愛顧を賜り、厚く御礼申し上げます。"
```

### Cultural Localization

```python
translator = SFLTranslator('en', 'es', localize=True)
translation = translator.translate(
    "It's raining cats and dogs.",
    region='es-MX'  # Mexican Spanish
)
# Output: "Está lloviendo a cántaros." (culturally appropriate idiom)
```

### SFL Analysis Output

```python
result = translator.translate("The CEO announced the merger.", analyze=True)

print(result.sfl_analysis)
# {
#   'transitivity': {
#     'process_type': 'verbal',
#     'sayer': 'The CEO',
#     'verbiage': 'the merger'
#   },
#   'mood': 'declarative',
#   'theme': 'The CEO',
#   'register': {
#     'field': 'business',
#     'tenor': 'neutral',
#     'mode': 'written'
#   }
# }
```

## Evaluation Metrics

Translation quality assessed via:

- **BLEU Score**: Lexical overlap with reference translations
- **Semantic Similarity**: Embedding-based meaning preservation
- **Register Consistency**: SFL-based register feature matching
- **Human Evaluation**: Fluency, adequacy, and appropriateness ratings

## CV/Portfolio Context

This repository demonstrates:

- **Multilingual Competence**: Operational knowledge of 10+ languages with linguistic awareness of structural and pragmatic differences
- **Linguistic Theory Application**: Practical implementation of SFL framework in NLP systems
- **Semantic Preservation**: Deep understanding of meaning beyond surface forms
- **Cultural Adaptation**: Recognition of language as culturally situated practice
- **Software Engineering**: Clean architecture, modular design, and agent-based systems

Ideal for roles requiring:
- Computational linguistics expertise
- Multilingual NLP system development
- Translation quality engineering
- International AI product localization

## Roadmap

- [ ] Extend language support to 20+ languages
- [ ] Add speech-to-speech translation with prosody preservation
- [ ] Implement multimodal translation (text + image context)
- [ ] Develop specialized domain models (legal, medical, technical)
- [ ] Create translation memory integration
- [ ] Build web interface for real-time translation

## License

MIT License

## Citation

If using this system in research, please cite:

```
@software{sfl_translation_agent,
  author = {Drury, Simon James},
  title = {SFL Translation Agent: Linguistically-Informed Machine Translation},
  year = {2026},
  url = {https://github.com/simon-drury/sfl-translation-agent}
}
```

## Contact

For questions, collaboration, or consulting inquiries:
- Email: simondrury2010@gmail.com
- LinkedIn: [simon-drury-60b881293](https://www.linkedin.com/in/simon-drury-60b881293)
- GitHub: [@simon-drury](https://github.com/simon-drury)
