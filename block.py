import subprocess
import os

TAG = '# Blocked websites'
HOSTS_PATH = '/etc/hosts'
WEBSITES = "websites.txt"

def blacklistSite(file_name, site):
    with open(file_name, 'a') as f:
        f.write(site)

def whitelistSite(file_name, site):
    with open(file_name,"r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i != site:
                f.write(i)
        f.truncate()
        f.close()

whitelistSite("websites.txt", "www.fanfiction.net")

# Will block websites in websites.txt or a file given as param
def block(file_name):

    with open(file_name, 'r') as f:
        lines = f.read().split('\n')
        websites_to_block = [l.strip() for l in lines if len(l)>0]


    with open(HOSTS_PATH, 'r+') as h:
        lines = h.read().split('\n')

        try:
            i = lines.index(TAG)
            already_blocked = lines[i+1:]
            lines = lines[:i+1]
        #    print('These websites were blocked:')
        #    for w in already_blocked:
        #        if not w == '':
        #            print('- %s' %w.split()[1])
        #    print('')
        #    print('Updating list of blocked websites')

        except ValueError:
            lines.append(TAG)
        #    print('No websites were blocked')
        #    print('')

        for w in websites_to_block:
            lines.append('127.0.0.1 %s' %w)
        h.seek(0)
        h.write('\n'.join(lines))
        h.truncate()

    subprocess.call(['dscacheutil', '-flushcache'])

    #os.system("sudo killall -HUP mDNSResponder; sleep 2;")

#    print('These websites are now blocked:')
#    for w in websites_to_block:
    #    print('- %s' %w)
