pip install --upgrade pip
if [ -f "scripts/update-packages.sh" ]; then
    scripts/update-pacages.sh
    pip install --upgrade -r packages.txt
else
    echo "You're not in the app base directory, go back there and rerun the script"
fi