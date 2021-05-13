from netmiko import ConnectHandler

username = 'admin'
password = 'cisco'

for device_num in range(1, 2):
    device_ip = '10.0.15.115'
    device_par = {'device_type': 'cisco_ios',
                  'ip': device_ip,
                  'username': username,
                  'password': password,
                  }

    with ConnectHandler(**device_par) as ssh:
        """config loopback / ACL for ssh / CDP interface description"""
        if device_num == 1:
            file_config = 'R0.txt'
            config_sent = ssh.send_config_from_file(config_file=file_config)
            print(config_sent)

        """show interface brief and save config"""
        result = ssh.send_command('sh ip int br')
        print(result)
        ssh.send_command('write')  