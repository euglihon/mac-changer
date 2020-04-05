import subprocess
import optparse  # add user arguments

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='Interface to change its MAC address')
    parser.add_option('-m', '--mac', dest='new_mac', help='new MAC address')
    (options, arguments) = parser.parse_args()
    
    if not options.interface:
        parser.error('[-] Please specify an interface, use --help for more info')
    
    elif not options.new_mac:
        parser.error('[-] Please specify an new MAC, use --help for more info')
    
    return options

def change_mac(interface, mac_address):
    
    print('[+] Changing MAC adress for ' + interface + ' to ' + mac_address)
    
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', mac_address])
    subprocess.call(['ifconfig', interface, 'up'])
    subprocess.call(['service', 'network-manager', 'restart'])  # restart network connect


options = get_arguments()

change_mac(options.interface, options.new_mac)  # 'wlp2s0   '00:11:22:33:44:99'