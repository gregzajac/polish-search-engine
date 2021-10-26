# polish-search-engine
Search engine with polish tokenization and stemming, based on pystempel package and article https://bart.degoe.de/building-a-full-text-search-engine-150-lines-of-code/.

## Setup

- Clone repository
```buildoutcfg
git clone https://github.com/gregzajac/polish-search-engine.git
```
- Create virtual environment and install requirements
```buildoutcfg
cd polish-search-engine
python -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
- Run main file with searching
```buildoutcfg
python run.py
```

## Technologies / Tools

- Python 3.8.10
- pystempel 1.2.0
