from flask_app import argparser, create_app
import os, sys

def main():
    args = argparser.get_args()
    
    # If requested to run as a daemon,
    # fork then close this process
    if args.daemon and os.fork():
        sys.exit()
    
    app = create_app(
        name         ='MovieManager WebApp',
        env          =args.env,
        create_tables=args.create,
        use_database =args.database)
    
    app.run(
        host=args.host,
        port=args.port,
        debug=False)

if __name__ == '__main__':
    main()
