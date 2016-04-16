import csv
import threading
import poplib
import argparse

# arguments
parser = argparse.ArgumentParser(description='Bulk verify pop3 mail accounts')
parser.add_argument('--host', dest='host', default='pop.mail.ru',
                    help='pop3 host address (default: pop.mail.ru)')
parser.add_argument('--port', dest='port', default=995,
                    help='pop3 port (default: 995)')
parser.add_argument('--ssl', dest='ssl', default=True,
                    help='(not used) Whether to use SSL (default: True)')
parser.add_argument('--output', dest='output_file', default='verified.csv',
                    help='output file to write verified accounts to (default: verified.csv)')
parser.add_argument('--input', dest='input_file', default='accounts.csv',
                    help='Source file (default: accounts.csv). Format: "account,password". First line is ignored. ')
args = parser.parse_args()


# clear verified file to start fresh
open(args.output_file, 'w').close()


def verify_account(_user, _password):
    try:
        mailbox = poplib.POP3_SSL(args.host, args.port)
        mailbox.user(_user)
        mailbox.pass_(_password)
        f = open(args.output_file, 'a')
        f.write("{},{},{},{},{}\n".format(_user, _password, args.host, args.port, args.ssl))
        f.close()
        print("{} success.".format(_user))
    except poplib.error_proto:
        print("{} failed.".format(_user))

threads = []
index = 0

# verify each account from input file in a new thread
with open(args.input_file, 'rb') as accounts:
    reader = csv.reader(accounts)
    for row in reader:
        if index == 0:
            index += 1
            continue
        user = row[0]
        password = row[1]

        # threading
        t = threading.Thread(target=verify_account, args=(user, password))
        t.daemon = True
        t.start()

        threads.append(t)

for t in threads:
    t.join()
print('done.')
