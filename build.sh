if [ ! -d "venv" ]; then
  python3 -m venv venv
fi
source venv/bin/activate
apt-get install -y tesseract-ocr -y python3-venv python3-pip
pip install -r requirements.txt
