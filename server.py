from src import app
import sys
sys.dont_write_bytecode = True

if __name__=="__main__":
    app.run(host="0.0.0.0", port=6060, debug=True)