# Kustosz installer - `kustosz.install` Ansible collection

🔨 🔧 Please bear with us until we have better documentation. 🐻 📖

Ensure you have Ansible and Ansible Galaxy installed

Install this collection:

    ansible-galaxy collection install kustosz.install

Create basic inventory file:

```
[kustosz]
fqdn.host.com

[kustosz:vars]
# variables required to connect to host, see:
# https://docs.ansible.com/ansible/latest/reference_appendices/special_variables.html#connection-variables
ansible_user=myuser

# variables used by playbook, see `roles/*/defaults/main.yml`
settings_local_path=/home/myuser/somedir/settings.yaml
web_user_name=kustoszuser
web_user_password=mysecretpassword
```

Run playbook:

    ansible-playbook kustosz.install.playbook -i ./myinventory
