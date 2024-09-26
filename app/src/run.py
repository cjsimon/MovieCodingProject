from .flask_app import App, argparser
import os, sys

def main():
    args = argparser.get_args()
    
    # If requested to run as a daemon,
    # fork then close this process
    if args.daemon and os.fork():
        sys.exit()
    
    app = App(args.env)
    app.run(host=args.host, port=args.port, debug=False)

if __name__ == "__main__":
    main()
