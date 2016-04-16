# verifypop
Bulk verify pop3 mail accounts (multi-threaded).

    usage: verifypop.py [-h] [--host HOST] [--port PORT] [--ssl SSL]
                        [--output OUTPUT_FILE] [--input INPUT_FILE]

    optional arguments:
      -h, --help            show this help message and exit
      --host HOST           pop3 host address (default: pop.mail.ru)
      --port PORT           pop3 port (default: 995)
      --ssl SSL             (not used) Whether to use SSL (default: True)
      --output OUTPUT_FILE  output file to write verified accounts to (default:
                            verified.csv)
      --input INPUT_FILE    Source file (default: accounts.csv). Format:
                            "account,password". First line is ignored.
